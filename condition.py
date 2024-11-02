import copy

import z3

from constraint import Constraint, Comparison
from int import INT
from node import Assign


class Condition:
    def __init__(self, constraints: list[list[Constraint]]):
        self.conjunctions: list[list[Constraint]] = copy.deepcopy(constraints)

    def __repr__(self):
        res = ""
        for conjunction in self.conjunctions:
            res += "("
            res += " and ".join([str(constraint) for constraint in conjunction])
            res += ")"
            if conjunction != self.conjunctions[-1]:
                res += " or "
        return res

    # (A or B) and (C or d) = (A and C) or (A and D) or (B and C) or (B and D)
    def __add__(self, other: "Condition"):
        if type(other) is not Condition:
            raise ValueError("Can only add Condition type to Condition type")
        new_conjunctions = []
        if self.conjunctions == []:
            new_conjunctions = other.conjunctions
        elif other.conjunctions == []:
            new_conjunctions = self.conjunctions
        else:
            for conjunction1 in self.conjunctions:
                for conjunction2 in other.conjunctions:
                    new_conjunctions.append(conjunction1 + conjunction2)
        return Condition(new_conjunctions)

    def get_symbols(self):
        symbols: set[str] = set()
        for conjunction in self.conjunctions:
            for constraint in conjunction:
                for value in [constraint.lvalue, constraint.rvalue]:
                    if type(value) is INT:
                        for symbol in value.symbols:
                            symbols.add(symbol.name)
        return symbols

    def to_z3(self, z3_symbols: dict[str, z3.Int]):
        def constraint_value_to_z3(value, symbols: dict[str, z3.Int]):
            if type(value) is not INT:
                new_value = value
            else:
                new_value = value.addends
                for symbol, multiplier in zip(value.symbols, value.multipliers):
                    if symbol.name not in symbols:
                        raise Exception(f"Symbol {symbol.name} not found in z3 symbols")
                    new_value += symbols[symbol.name] * multiplier
            return new_value

        res = []
        for conjunction in self.conjunctions:
            conj = []
            for constraint in conjunction:
                lvalue = constraint_value_to_z3(constraint.lvalue, z3_symbols)
                rvalue = constraint_value_to_z3(constraint.rvalue, z3_symbols)
                match constraint.comparison:
                    case Comparison.EQUAL:
                        conj.append(lvalue == rvalue)
                    case Comparison.NOT_EQUAL:
                        conj.append(lvalue != rvalue)
                    case Comparison.LESS_THAN:
                        conj.append(lvalue < rvalue)
                    case Comparison.GREATER_THAN:
                        conj.append(lvalue > rvalue)
                    case Comparison.LESS_THAN_OR_EQUAL:
                        conj.append(lvalue <= rvalue)
                    case Comparison.GREATER_THAN_OR_EQUAL:
                        conj.append(lvalue >= rvalue)
            res.append(z3.And(conj))
        return z3.Or(res)

    def is_sat(self):
        z3_symbols: dict[str, z3.Int] = {}
        extend_z3_symbols_from_condition(z3_symbols, self)
        solver = z3.Solver()
        solver.add(self.to_z3(z3_symbols))
        if solver.check() == z3.sat:
            return True
        else:
            return False


def extend_z3_symbols_from_condition(z3_symbols: dict[str, z3.Int], condition: Condition):
    symbols = condition.get_symbols()
    for symbol in symbols:
        if symbol not in z3_symbols:
            z3_symbols[symbol] = z3.Int(symbol)


def extend_z3_symbols_from_assigns(z3_symbols: dict[str, z3.Int], assigns: list[Assign]):
    for assign in assigns:
        lvalue_symbol = assign.lvalue.symbols[0]
        if lvalue_symbol.name not in z3_symbols.keys():
            z3_symbols[lvalue_symbol.name] = z3.Int(lvalue_symbol.name)
        if type(assign.rvalue) is INT:
            for symbol in assign.rvalue.symbols:
                if symbol.name not in z3_symbols.keys():
                    z3_symbols[symbol.name] = z3.Int(symbol.name)
