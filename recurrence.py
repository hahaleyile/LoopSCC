import copy

import sympy

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
                    inequalities.append(lvalue == rvalue)
                case Comparison.NOT_EQUAL:
                    inequalities.append(lvalue != rvalue)
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
        self.intersection: int = 0
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

        match oper_type:
            case INT():
                if sub_domains[0].interval.args[1] != sub_domains[1].interval.args[0]:
                    raise Exception("Invalid oscillation interval")
                lhs = sub_domains[1].interval.args[0]
                if sub_domains[1].interval.left_open:
                    lhs += 1
                lhs += sub_domains[1].related_operations[0].rvalue.addends
                rhs = sub_domains[0].interval.args[1]
                if sub_domains[0].interval.right_open:
                    rhs -= 1
                rhs += sub_domains[0].related_operations[0].rvalue.addends
                if not sub_domains[0].interval.contains(lhs) or not sub_domains[1].interval.contains(rhs):
                    raise Exception("Invalid oscillation interval")
                self.interval = sympy.Interval(lhs, rhs, False, False)
                self.intersection = int(sub_domains[0].interval.args[1])
                if not sub_domains[0].interval.right_open:
                    self.intersection += 1

                # get other variables operation
                for assign in sub_domains[0].path.assigns:
                    if (type(assign.rvalue) is not INT
                            or assign.rvalue.multipliers[0] != 1
                            or assign.rvalue.symbols[0].name != assign.lvalue.symbols[0].name):
                        raise Exception("Invalid assign format")
                    self.var_operation[assign.lvalue.symbols[0].name] = []
                    self.var_operation[assign.lvalue.symbols[0].name].extend([assign.rvalue.addends, 0])
                for assign in sub_domains[1].path.assigns:
                    if (type(assign.rvalue) is not INT
                            or assign.rvalue.multipliers[0] != 1
                            or assign.rvalue.symbols[0].name != assign.lvalue.symbols[0].name):
                        raise Exception("Invalid assign format")
                    if assign.lvalue.symbols[0].name not in self.var_operation.keys():
                        self.var_operation[assign.lvalue.symbols[0].name] = []
                        self.var_operation[assign.lvalue.symbols[0].name].extend([0, assign.rvalue.addends])
                    else:
                        self.var_operation[assign.lvalue.symbols[0].name][1] = assign.rvalue.addends

                lhs_int = int(lhs)
                cur_val = lhs_int
                left_addon = sub_domains[0].related_operations[0].rvalue.addends
                right_addon = sub_domains[1].related_operations[0].rvalue.addends
                cnt = 0
                visted = set()
                while cnt != int(rhs - lhs + 1):
                    for value in range(lhs_int, int(rhs + 1)):
                        if value not in visted:
                            start_val = value
                            cur_val = value
                            break
                    self.val_cycle.append([])
                    self.iter_cycle.append([])
                    left_iter = 0
                    right_iter = 0
                    while True:
                        self.val_cycle[-1].append(cur_val)
                        visted.add(cur_val)
                        if cur_val < self.intersection:
                            cur_val += left_addon
                            left_iter += 1
                        else:
                            cur_val += right_addon
                            right_iter += 1
                        if cur_val != start_val and cur_val in visted:
                            raise Exception("Invalid oscillation cycle")
                        self.iter_cycle[-1].append((left_iter, right_iter))
                        cnt += 1
                        if cur_val == start_val:
                            break
            case _:
                raise Exception("Only INT type can handle right now")
