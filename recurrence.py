import copy

import sympy
import z3
from sympy import And, Eq, Ge, Gt, Le, Lt, Ne, Not, Or

from block import Path
from constraint import Comparison
from int import INT, Symbol
from node import Assign
from spath_graph import SPath_Graph


class RecurrenceRelation:
    def __init__(self, relation: Assign):
        self.relation: Assign = relation
        self.iter_num: INT = INT.define_int('N')
        self.closed_form: Assign = None
        self.pre_n_iteration: Assign = None
        self.solve()

    def solve(self):
        self.closed_form = copy.deepcopy(self.relation)
        self.pre_n_iteration = copy.deepcopy(self.relation)
        lvalue_symbol: Symbol = self.relation.lvalue.symbols[0]
        rvalue = self.relation.rvalue
        if type(rvalue) is INT and rvalue.symbol_num > 0:
            if rvalue.symbol_num > 1:
                if rvalue.multipliers[rvalue.symbol_index[lvalue_symbol.name]] != 1:
                    raise Exception("Recurrence relation can only process plus and minus operation")
                constant = rvalue - INT.define_int(lvalue_symbol.name)
                self.closed_form = Assign(None, (
                    self.relation.lvalue,
                    constant * self.iter_num + INT.define_int(lvalue_symbol.name))
                                          )
                self.pre_n_iteration = Assign(None, (
                    self.relation.lvalue,
                    constant * (self.iter_num - 1) + INT.define_int(lvalue_symbol.name))
                                              )
                return
            if rvalue.symbols[0].name != lvalue_symbol.name:
                self.closed_form.rvalue = rvalue
                self.pre_n_iteration.rvalue = rvalue
                return
            if rvalue.multipliers[0] != 1:
                raise Exception("Recurrence relation can only process plus and minus operation")
            addends = self.closed_form.rvalue.addends
            self.closed_form.rvalue.addends = 0
            self.closed_form.rvalue = self.closed_form.rvalue + addends * self.iter_num
            self.pre_n_iteration.rvalue = self.closed_form.rvalue - addends
        # else:
        #     self.closed_form.rvalue = rvalue
        #     self.pre_n_iteration.rvalue = rvalue


class PiecewiseRecurrenceRelation:
    def __init__(self, spg: SPath_Graph, scc: list[int]):
        self.subDomains: list[PiecewiseSubDomain] = []
        self.oscillation: Oscillation = None

        for index in scc:
            self.subDomains.append(PiecewiseSubDomain(spg.paths[index]))
        if len(self.subDomains) > 2:
            raise Exception("Cannot process more than two nodes scc")
        if not self.subDomains[0].interval.is_disjoint(self.subDomains[1].interval):
            raise Exception("Two subdomains are not disjoint")
        self.subDomains = sorted(self.subDomains, key=lambda x: x.interval.inf)
        assign0 = self.subDomains[0].related_operations[0]
        assign1 = self.subDomains[1].related_operations[0]
        if type(assign0.rvalue) is INT and type(assign1.rvalue) is INT:
            if (assign0.rvalue.multipliers[0] != 1 or
                    assign0.rvalue.addends <= 0 or
                    assign1.rvalue.multipliers[0] != 1 or
                    assign1.rvalue.addends >= 0):
                raise Exception("Subdomains are not monotonic")
        self.oscillation = Oscillation(self.subDomains[0].related_operations[0].lvalue, self.subDomains)


class PiecewiseSubDomain:
    def __init__(self, path: Path):
        self.interval: sympy.Interval = None
        self.related_operations: list[Assign] = []
        self.path = path

        symbols = path.precond.get_symbols()
        only_symbols = []
        for assign in path.assigns:
            if assign.lvalue.symbols[0].name in symbols:
                only_symbols.append(assign.lvalue.symbols[0].name)
        # if len(only_symbols) != 1:
        #     raise Exception("Only one symbol is allowed in subdomain's conditions")
        only_symbol = Symbol(only_symbols[0])

        for assign in path.assigns:
            if assign.lvalue.symbols[0].name == only_symbol.name:
                if type(assign.rvalue) is INT:
                    for symbol in assign.rvalue.symbols:
                        if symbol.name != only_symbol.name:
                            raise Exception("Only one symbol is allowed in subdomain's assignments")
                self.related_operations.append(assign)
        if len(self.related_operations) != 1:
            raise Exception("Invalid subdomain format")

        def sympy_value(Value, X):
            if type(Value) is not INT:
                return Value
            else:
                if Value.symbols[0].name != X.name:
                    return None
                Res = Value.addends
                Res += X * Value.multipliers[0]
                return Res

        x = sympy.Symbol(only_symbol.name)
        inequalities = []
        if len(path.precond.conjunctions) != 1:
            raise Exception("pre condition should not have or condition")
        for constraint in path.precond.conjunctions[0]:
            lvalue = sympy_value(constraint.lvalue, x)
            rvalue = sympy_value(constraint.rvalue, x)
            if lvalue is None or rvalue is None:
                continue
            match constraint.comparison:
                case Comparison.EQUAL:
                    inequalities.append(sympy.Eq(lvalue, rvalue))
                case Comparison.NOT_EQUAL:
                    self.interval = sympy.Interval.open(-float('inf'), rvalue).union(
                        sympy.Interval.open(rvalue, float('inf')))
                    return
                case Comparison.LESS_THAN:
                    inequalities.append(lvalue < rvalue)
                case Comparison.GREATER_THAN:
                    inequalities.append(lvalue > rvalue)
                case Comparison.LESS_THAN_OR_EQUAL:
                    inequalities.append(lvalue <= rvalue)
                case Comparison.GREATER_THAN_OR_EQUAL:
                    inequalities.append(lvalue >= rvalue)

        res = sympy.reduce_inequalities(inequalities, x)
        if len(res.args) != 2:
            raise Exception("Invalid inequality format")
        relations = [(i.lhs, i.rel_op, i.rhs) for i in
                     [i.canonical for i in res.atoms(sympy.core.relational.Relational)]]
        relations_sorted = sorted(relations, key=lambda x: float(x[2]))
        if len(relations_sorted) == 1:
            if relations_sorted[0][1] == '==':
                self.interval = sympy.Interval(relations_sorted[0][2], relations_sorted[0][2], False, False)
                return
            else:
                raise Exception("Invalid inequality format")
        if relations_sorted[0][2] > relations_sorted[1][2]:
            raise Exception("Invalid inequality format")
        if relations_sorted[0][1] == '>=':
            left_open = False
        elif relations_sorted[0][1] == '>':
            left_open = True
        else:
            raise Exception("Invalid inequality format")
        if relations_sorted[1][1] == '<=':
            right_open = False
        elif relations_sorted[1][1] == '<':
            right_open = True
        else:
            raise Exception("Invalid inequality format")
        self.interval = sympy.Interval(relations_sorted[0][2], relations_sorted[1][2],
                                       left_open, right_open)


class Oscillation:
    def __init__(self, oper_type, sub_domains: list[PiecewiseSubDomain]):
        self.interval: sympy.Interval = None
        # iteration in cycle
        # for example, [1, 2, 3, 4, 5, 1, ...] is stored as [(0, 1), (1, 1), (2, 1), (2, 2), (2, 3)]
        self.iter_cycle: list[list[tuple[int, int]]] = []
        # value in cycle
        # for example, [1, 2, 3, 4, 5, 1, ...] is stored as [1, 2, 3, 4, 5]
        self.val_cycle: list[list[int]] = []
        self.main_var: str = sub_domains[0].related_operations[0].lvalue.symbols[0].name
        # only represent int plus operation
        # for example, i = i + 1 in left subdomain and i = i - 2 in right subdomain
        # then the data is {i: [1, -2]}
        self.var_operation: dict[str, list[int, int]] = {}

        # calculate oscillation interval
        init_interval = sympy.FiniteSet()
        x = sympy.symbols(self.main_var)
        funcs: dict[any, sympy.Interval] = {}
        for sub_domain in sub_domains:
            for operation in sub_domain.related_operations:
                rvalue = operation.rvalue
                func = None
                match rvalue:
                    case INT():
                        func = rvalue.to_sympy()
                    case int():
                        func = rvalue
                funcs[func] = sub_domain.interval
                interval = sympy.imageset(x, func, sub_domain.interval)
                for other_domain in sub_domains:
                    if other_domain != sub_domain:
                        init_interval = init_interval.union(interval.intersect(other_domain.interval))
        self.interval = init_interval

        def image_piecewise(interval, funcs, x):
            image = sympy.FiniteSet()
            for func, sub_interval in funcs.items():
                t = interval.intersect(sub_interval)
                i = sympy.imageset(x, func, t)
                image = image.union(i)
            return image

        image = image_piecewise(self.interval, funcs, x)
        while not image.is_subset(self.interval):
            self.interval = self.interval.union(image)
            image = image_piecewise(self.interval, funcs, x)

        visited = set()
        discrete_interval = list(self.interval.intersect(sympy.S.Integers))
        for value in discrete_interval:
            cur_val = int(value)
            if cur_val not in visited:
                self.val_cycle.append([])
                self.iter_cycle.append([])
                iternum = [0, 0]
                while cur_val not in visited:
                    self.val_cycle[-1].append(cur_val)
                    visited.add(cur_val)
                    index = 0
                    for func, interval in funcs.items():
                        if cur_val in interval:
                            iternum[index] += 1
                            func = sympy.sympify(func)
                            cur_val = int(func.subs(x, cur_val))
                            break
                        index += 1
                    else:
                        raise Exception("Error")
                    self.iter_cycle[-1].append(tuple(iternum))

        symbols = set()
        for sub_domain in sub_domains:
            for assign in sub_domain.path.assigns:
                if assign.lvalue.symbols[0].name == self.main_var:
                    continue
                match assign.rvalue:
                    case INT():
                        symbol_name = assign.lvalue.symbols[0].name
                        if (assign.rvalue.multipliers[0] != 1
                                or assign.rvalue.symbols[0].name != symbol_name):
                            raise Exception("Invalid assign format")
                        symbols.add(symbol_name)
                    case _:
                        raise Exception("Only INT type can handle right now")
        for symbol in symbols:
            self.var_operation[symbol] = [0] * len(sub_domains)
        index = 0
        for sub_domain in sub_domains:
            for assign in sub_domain.path.assigns:
                if assign.lvalue.symbols[0].name == self.main_var:
                    continue
                match assign.rvalue:
                    case INT():
                        symbol = assign.lvalue.symbols[0].name
                        self.var_operation[symbol][index] = assign.rvalue.addends
                    case _:
                        raise Exception("Only INT type can handle right now")
            index += 1

    def interval_to_inequalities(self, var: str):
        x = sympy.symbols(var)
        expr = self.interval.as_relational(x)
        z3_symbol = z3.Int(var)

        def convert(expr):
            match expr:
                case sympy.Symbol():
                    if expr != x:
                        raise Exception("Error")
                    return z3_symbol
                case sympy.Integer():
                    return int(expr)
                case And():
                    arg0 = convert(expr.args[0])
                    arg1 = convert(expr.args[1])
                    return z3.And(arg0, arg1)
                case Or():
                    arg0 = convert(expr.args[0])
                    arg1 = convert(expr.args[1])
                    return z3.Or(arg0, arg1)
                case Not():
                    arg0 = convert(expr.args[0])
                    return z3.Not(arg0)
                case Eq():
                    arg0 = convert(expr.args[0])
                    arg1 = convert(expr.args[1])
                    return arg0 == arg1
                case Ge():
                    arg0 = convert(expr.args[0])
                    arg1 = convert(expr.args[1])
                    return arg0 >= arg1
                case Gt():
                    arg0 = convert(expr.args[0])
                    arg1 = convert(expr.args[1])
                    return arg0 > arg1
                case Le():
                    arg0 = convert(expr.args[0])
                    arg1 = convert(expr.args[1])
                    return arg0 <= arg1
                case Lt():
                    arg0 = convert(expr.args[0])
                    arg1 = convert(expr.args[1])
                    return arg0 < arg1
                case Ne():
                    arg0 = convert(expr.args[0])
                    arg1 = convert(expr.args[1])
                    return arg0 != arg1
                case _:
                    raise Exception("Error")

        return convert(expr)
