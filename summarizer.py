import z3

from block import Path
from int import INT, MUL_INT
from node import Assign
from recurrence import Oscillation, PiecewiseRecurrenceRelation, RecurrenceRelation
from spath_graph import SCC, SPath_Graph


class Summarizer:
    def __init__(self, spg: SPath_Graph):
        self.spg = spg
        self.scc_summary: dict[int, Summary] = {}
        self.traces_summary: list = []
        self.traces_symbols: list[dict[str, z3.Int]] = []

    def __len__(self):
        constraint_num = 0
        for trace_summary in self.traces_summary:
            for i in trace_summary:
                for j in i:
                    if type(j) is list:
                        constraint_num += len(j)
                    else:
                        constraint_num += 1
        return constraint_num

    def solver_check_trace(self, solver, trace_summary, trace_symbols: dict[str, z3.Int]):
        res = []
        from_break = False
        for summary in trace_summary:
            # type 2 scc is the end of the trace
            if type(summary[0]) is list:
                for sub_summary in summary:
                    inside_oscillation = False
                    solver.push()
                    # end inside oscillation interval
                    if type(sub_summary[-1]) is Oscillation:
                        inside_oscillation = True
                        solver.add(sub_summary[:-1])
                    else:
                        solver.add(sub_summary)
                    if solver.check() == z3.unsat:
                        solver.pop()
                        continue
                    if not inside_oscillation:
                        model = solver.model()
                        for symbol_name, z3_var in trace_symbols.items():
                            res.append((symbol_name, str(model[z3_var])))
                        return res
                    else:
                        oscillation: Oscillation = sub_summary[-1]
                        model = solver.model()
                        main_var_val = model[trace_symbols[oscillation.main_var]].as_long()
                        for val_cycle_index in range(len(oscillation.val_cycle)):
                            if main_var_val in oscillation.val_cycle[val_cycle_index]:
                                iter_cycle = []
                                cycle_num = len(oscillation.val_cycle[val_cycle_index])
                                iter_cycle_start = oscillation.val_cycle[val_cycle_index].index(main_var_val)
                                iter_shift = []
                                if iter_cycle_start == 0:
                                    iter_shift = [0, 0]
                                else:
                                    base_iter = oscillation.iter_cycle[val_cycle_index][iter_cycle_start - 1]
                                    iter_shift.append(-base_iter[0])
                                    iter_shift.append(-base_iter[1])
                                iter_cycle_current = iter_cycle_start
                                for i in range(cycle_num):
                                    if iter_cycle_current >= cycle_num:
                                        iter_shift[0] = iter_shift[0] + oscillation.iter_cycle[val_cycle_index][-1][
                                            0]
                                        iter_shift[1] = iter_shift[1] + oscillation.iter_cycle[val_cycle_index][-1][
                                            1]
                                        iter_cycle_current = 0
                                    iter_cycle.append(
                                        (
                                            oscillation.iter_cycle[val_cycle_index][iter_cycle_current][0] +
                                            iter_shift[0],
                                            oscillation.iter_cycle[val_cycle_index][iter_cycle_current][1] +
                                            iter_shift[1],
                                        )
                                    )
                                    iter_cycle_current += 1

                                symbols = {}
                                temp_solver = z3.Solver()
                                for name in trace_symbols.keys():
                                    symbols[name] = z3.Int(f"{name}_0")
                                for name in trace_symbols.keys():
                                    value = model[trace_symbols[name]].as_long()
                                    temp_solver.add(symbols[name] == value)
                                iter1 = z3.Int("N1")
                                temp_solver.add(iter1 >= 0)
                                for var in oscillation.var_operation.keys():
                                    new_symbol = z3.Int(f"{var}_1")
                                    value = (iter_cycle[-1][0] * oscillation.var_operation[var][0]
                                             + iter_cycle[-1][1] * oscillation.var_operation[var][1])
                                    temp_solver.add(new_symbol == symbols[var] + value * iter1)
                                    symbols[var] = new_symbol
                                temp_solver.add(self.spg.cfg.arcs_desc[(0, 1)].to_z3(symbols))
                                temp_symbols = symbols.copy()
                                for var in oscillation.var_operation.keys():
                                    new_symbol = z3.Int(f"{var}_2")
                                    value = (iter_cycle[-1][0] * oscillation.var_operation[var][0]
                                             + iter_cycle[-1][1] * oscillation.var_operation[var][1])
                                    temp_solver.add(new_symbol == z3.Int(f"{var}_0") + value * (iter1 + 1))
                                    symbols[var] = new_symbol
                                temp_solver.add(
                                    z3.Not(
                                        z3.And(
                                            self.spg.cfg.arcs_desc[(0, 1)].to_z3(symbols)
                                        )
                                    )
                                )
                                symbols = temp_symbols.copy()
                                if temp_solver.check() == z3.unsat:
                                    raise Exception("No solution found")
                                model = temp_solver.model()
                                res = []
                                for symbol_name, z3_var in symbols.items():
                                    res.append((symbol_name, str(model[z3_var])))
                                for i in range(cycle_num):
                                    temp_solver.push()
                                    for var in oscillation.var_operation.keys():
                                        new_symbol = z3.Int(f"{var}_3")
                                        value = (iter_cycle[i][0] * oscillation.var_operation[var][0]
                                                 + iter_cycle[i][1] * oscillation.var_operation[var][1])
                                        temp_solver.add(new_symbol == temp_symbols[var] + value)
                                        symbols[var] = new_symbol
                                    temp_solver.push()
                                    temp_solver.add(
                                        self.spg.cfg.arcs_desc[(0, 1)].to_z3(symbols)
                                    )
                                    if temp_solver.check() == z3.sat:
                                        temp_solver.pop()
                                        temp_solver.pop()
                                        continue
                                    else:
                                        res = []
                                        temp_solver.pop()
                                        if temp_solver.check() == z3.unsat:
                                            raise Exception("Error finding solution")
                                        model = temp_solver.model()
                                        for symbol_name, z3_var in symbols.items():
                                            if symbol_name == oscillation.main_var:
                                                res.append((symbol_name, str(oscillation.val_cycle[val_cycle_index]
                                                                             [(iter_cycle_start + i + 1) % cycle_num])))
                                            else:
                                                res.append((symbol_name, str(model[z3_var])))
                                        return res
                                break
                    break
            else:
                solver.add(summary)
                if solver.check() == z3.unsat:
                    from_break = True
                    break
        if not from_break:
            model = solver.model()
            for symbol_name, z3_var in trace_symbols.items():
                res.append((symbol_name, str(model[z3_var])))
            return res
        else:
            return None

    def solve(self, init_values: list[tuple[INT, int]]):
        solver = z3.Solver()
        symbols = {}
        for init_value in init_values:
            symbol = init_value[0].symbols[0]
            z3_var = z3.Int(f"{symbol.name}_0")
            symbols[symbol.name] = z3_var
            solver.add(z3_var == init_value[1])
        solver.push()
        solver.add(self.spg.cfg.arcs_desc[(0, 1)].to_z3(symbols))
        if solver.check() == z3.unsat:
            return [(init_value[0].symbols[0].name, init_value[1]) for init_value in init_values]
        solver.pop()
        for trace_summary, trace_symbols in zip(self.traces_summary, self.traces_symbols):
            solver.push()
            res = self.solver_check_trace(solver, trace_summary, trace_symbols)
            solver.pop()
            if res is not None:
                return res
        raise Exception("No solution found")

    def summarize(self):
        visited = set()
        for trace in self.spg.scc_paths:
            for scc_index in trace:
                if scc_index in visited:
                    continue
                visited.add(scc_index)
                self.scc_summary[scc_index] = self.scc_summarize(self.spg.scc[scc_index])
        for trace in self.spg.scc_paths:
            trace_summary = self.trace_summarize(trace)
            self.traces_summary.append(trace_summary[0])
            self.traces_symbols.append(trace_summary[1])

    def get_scc_type(self, scc: SCC):
        node_num = len(scc.nodes)
        if node_num > 2:
            raise Exception("SCC has more than 2 nodes, summarize is not implemented yet")
        elif node_num == 2:
            return 2
        elif node_num == 1:
            if scc.is_scc:
                return 1
            else:
                return 0
        else:
            raise Exception("Invalid scc")

    def scc_summarize(self, scc: SCC):
        match self.get_scc_type(scc):
            case 2:
                return self.summarize_two_node_scc(scc)
            case 1:
                return self.summarize_one_node_scc(scc)
            case 0:
                return self.summarize_one_node(scc)

    def trace_summarize(self, trace: list[int]):
        # if summary has multiple conditions, then use push pop to check z3 sat, find proper path
        summary = []
        # get all symbols used in trace
        symbols: dict[str, z3.Int] = {}
        loop_cond_symbols = self.spg.cfg.arcs_desc[(0, 1)].get_symbols()
        for symbol_name in loop_cond_symbols:
            symbols[symbol_name] = z3.Int(f"{symbol_name}_0")
        for trace_index in trace:
            for path_index in self.spg.scc[trace_index].nodes:
                path = self.spg.paths[path_index]

                for assign in path.assigns:
                    symbols[assign.lvalue.symbols[0].name] = z3.Int(f"{assign.lvalue.symbols[0].name}_0")

                cond_symbols = path.precond.get_symbols()
                for symbol_name in cond_symbols:
                    symbols[symbol_name] = z3.Int(f"{symbol_name}_0")

        # add constraints for the first scc
        if len(trace) > 0:
            match self.get_scc_type(self.spg.scc[trace[0]]):
                case 2 | 1 | 0:
                    summary.append([])
                    for symbol_name in symbols.keys():
                        if symbol_name in self.scc_summary[trace[0]].pre_var:
                            summary[-1].append(
                                self.scc_summary[trace[0]].pre_var[symbol_name]
                                ==
                                symbols[symbol_name]
                            )
                        if symbol_name in self.scc_summary[trace[0]].next_var:
                            symbols[symbol_name] = self.scc_summary[trace[0]].next_var[symbol_name]

        # connect previous scc to next scc, also connect scc to end
        for trace_index in range(len(trace)):
            match self.get_scc_type(self.spg.scc[trace[trace_index]]):
                case 2:
                    if trace_index != len(trace) - 1:
                        raise Exception("Two node scc should execute forever unless exit")
                    summary.append([])
                    summary[-1] = self.scc_summary[trace[trace_index]].summary.copy()
                    for s in summary[-1]:
                        if type(s[-1]) is not Oscillation:
                            s.append(
                                z3.Not(
                                    self.spg.cfg.arcs_desc[(0, 1)].to_z3(self.scc_summary[trace[trace_index]].next_var)
                                )
                            )
                case 1 | 0:
                    summary.append([])
                    summary[-1] = self.scc_summary[trace[trace_index]].summary[0].copy()
                    if trace_index == len(trace) - 1:
                        for symbol_name in self.scc_summary[trace[trace_index]].next_var.keys():
                            if symbol_name in symbols.keys():
                                if not symbols[symbol_name].eq(
                                        self.scc_summary[trace[trace_index]].next_var[symbol_name]):
                                    symbols[symbol_name] = self.scc_summary[trace[trace_index]].next_var[symbol_name]
                        summary[-1].append(
                            z3.Not(
                                self.spg.cfg.arcs_desc[(0, 1)].to_z3(symbols)
                            )
                        )
                        tmp_symbols = symbols.copy()
                        from_break = False
                        for symbol_name in self.spg.cfg.arcs_desc[(0, 1)].get_symbols():
                            if f"T{symbol_name}" in self.scc_summary[trace[trace_index]].pre_var.keys():
                                tmp_symbols[symbol_name] = self.scc_summary[trace[trace_index]].pre_var[
                                    f"T{symbol_name}"]
                                from_break = True
                        if from_break:
                            summary[-1].append(
                                self.spg.cfg.arcs_desc[(0, 1)].to_z3(tmp_symbols)
                            )
                    else:
                        next_scc = self.spg.scc[trace[trace_index + 1]]
                        match self.get_scc_type(next_scc):
                            case 2 | 1 | 0:
                                for symbol_name in self.scc_summary[trace[trace_index + 1]].pre_var.keys():
                                    if symbol_name in symbols.keys():
                                        summary[-1].append(
                                            self.scc_summary[trace[trace_index + 1]].pre_var[symbol_name]
                                            ==
                                            symbols[symbol_name]
                                        )
                                        if symbol_name in self.scc_summary[trace[trace_index + 1]].next_var:
                                            symbols[symbol_name] = self.scc_summary[trace[trace_index + 1]].next_var[
                                                symbol_name]
        return [summary, symbols]

    def summarize_one_node(self, scc: SCC) -> "Summary":
        node: Path = self.spg.paths[scc.nodes[0]]
        summary = Summary()
        summary.append_assigns(node.assigns)
        cond_symbols = node.precond.get_symbols()
        if len(cond_symbols) > 0:
            for symbol_name in cond_symbols:
                if symbol_name not in summary.pre_var.keys():
                    summary.pre_var[symbol_name] = Summary.get_next_z3_var_by_name(symbol_name)
            summary.summary[-1].append(node.precond.to_z3(summary.pre_var))
        return summary

    # contains closed form with iteration number symbol
    # eliminate iteration number symbol when analyse scc list (also called trace)
    def summarize_one_node_scc(self, scc: SCC) -> "Summary":
        node: Path = self.spg.paths[scc.nodes[0]]
        recurrences: list[RecurrenceRelation] = [RecurrenceRelation(assign) for assign in node.assigns]
        summary = Summary()
        summary.append_assigns([recurrence.closed_form for recurrence in recurrences])
        summary.summary[-1].append(summary.pre_var["N"] > 0)
        cond_symbols = node.precond.get_symbols()
        if len(cond_symbols) > 0:
            for symbol_name in cond_symbols:
                if symbol_name not in summary.pre_var.keys():
                    summary.pre_var[symbol_name] = Summary.get_next_z3_var_by_name(symbol_name)
            summary.summary[-1].append(node.precond.to_z3(summary.pre_var))

        # get n-1 iteration post var
        symbols = set()
        for recurrence in recurrences:
            symbol = recurrence.pre_n_iteration.lvalue.symbols[0].name
            symbols.add(symbol)
            name = f"T{symbol}"
            summary.pre_var[name] = Summary.get_next_z3_var_by_name(name)
            assign = recurrence.pre_n_iteration
            lz3 = summary.pre_var[name]
            if type(assign.rvalue) is INT:
                rz3 = assign.rvalue.addends
                for symbol, multiplier in zip(assign.rvalue.symbols, assign.rvalue.multipliers):
                    rz3 += summary.pre_var[symbol.name] * multiplier
            elif type(assign.rvalue) is MUL_INT:
                rz3 = assign.rvalue.to_z3(summary.pre_var)
            else:
                rz3 = assign.rvalue
            summary.summary[-1].append(lz3 == rz3)
        # n-1 interation post var satisfy the condition
        precond_symbols = {}
        for symbol_name in symbols:
            precond_symbols[symbol_name] = summary.pre_var[f"T{symbol_name}"]
        cond_symbols = node.precond.get_symbols()
        if len(cond_symbols) > 0:
            for symbol_name in cond_symbols:
                if symbol_name not in precond_symbols.keys():
                    precond_symbols[symbol_name] = summary.pre_var[symbol_name]
            summary.summary[-1].append(node.precond.to_z3(precond_symbols))

        return summary

    # noinspection PyTypeChecker
    def summarize_two_node_scc(self, scc: SCC):
        piecewise_recurrence = PiecewiseRecurrenceRelation(self.spg, scc.nodes)
        summary = Summary()
        # init pre_var and next_var
        for subDomain in piecewise_recurrence.subDomains:
            for assign in subDomain.path.assigns:
                summary.assign_to_z3(assign)

        # add constraint of start inside of oscillation interval
        summary.summary.append([])
        main_var = piecewise_recurrence.oscillation.main_var
        expr = piecewise_recurrence.oscillation.interval_to_inequalities(main_var)
        expr_need = z3.substitute(expr, (z3.Int(main_var), summary.pre_var[main_var]))
        # x inside oscillation interval
        summary.summary[-1].append(expr_need)
        # i' = i
        for next_var_name in summary.next_var.keys():
            if next_var_name in summary.pre_var.keys():
                summary.summary[-1].append(
                    summary.next_var[next_var_name]
                    ==
                    summary.pre_var[next_var_name]
                )
        summary.summary[-1].append(piecewise_recurrence.oscillation)

        # add constraint of start inside of oscillation interval
        for subDomain in piecewise_recurrence.subDomains:
            recurrences: list[RecurrenceRelation] = [RecurrenceRelation(assign) for assign in subDomain.path.assigns]
            used_symbols = set()
            for recurrence in recurrences:
                used_symbols.add(recurrence.closed_form.lvalue.symbols[0].name)
            # first add end inside of oscillation interval
            summary.summary.append([])
            # x inside subDomain interval
            summary.summary[-1].append(subDomain.path.precond.to_z3(summary.pre_var))
            # y' = y if y not appear
            for symbol_name in summary.next_var.keys():
                if symbol_name not in used_symbols:
                    summary.summary[-1].append(
                        summary.next_var[symbol_name] == summary.pre_var[symbol_name]
                    )
            # append recurrences closed form
            for recurrence in recurrences:
                summary.summary[-1].append(summary.assign_to_z3(recurrence.closed_form))
            # these closed form should inside of the oscillation interval
            expr_need = z3.substitute(expr, (z3.Int(main_var), summary.next_var[main_var]))
            summary.summary[-1].append(expr_need)
            # N > 0
            summary.summary[-1].append(summary.pre_var['N'] > 0)
            # pre n variables
            pre_n_var: dict[str, z3.Int] = {}
            for recurrence in recurrences:
                if (recurrence.pre_n_iteration.lvalue.symbol_num != 1 or
                        recurrence.pre_n_iteration.lvalue.multipliers[0] != 1):
                    raise Exception("lvalue should be a single symbol")
                symbol_name = recurrence.pre_n_iteration.lvalue.symbols[0].name
                pre_n_var[symbol_name] = Summary.get_next_z3_var_by_name(f"T{symbol_name}")
                match recurrence.pre_n_iteration.rvalue:
                    case INT() | MUL_INT():
                        r_expr = sum(recurrence.pre_n_iteration.rvalue.to_z3(summary.pre_var))
                    case _:
                        r_expr = recurrence.pre_n_iteration.rvalue
                summary.summary[-1].append(pre_n_var[symbol_name] == r_expr)
            # pre main var outside of oscillation interval
            expr_need = z3.substitute(expr, (z3.Int(main_var), pre_n_var[main_var]))
            summary.summary[-1].append(z3.Not(expr_need))
            # pre n variables satisfied the loop condition
            summary.summary[-1].append(self.spg.cfg.arcs_desc[(0, 1)].to_z3(pre_n_var))
            summary.summary[-1].append(piecewise_recurrence.oscillation)

            # then add end outside of oscillation interval
            summary.summary.append([])
            # x inside subDomain interval
            summary.summary[-1].append(subDomain.path.precond.to_z3(summary.pre_var))
            # y' = y if y not appear
            for symbol_name in summary.next_var.keys():
                if symbol_name not in used_symbols:
                    summary.summary[-1].append(
                        summary.next_var[symbol_name] == summary.pre_var[symbol_name]
                    )
            # append recurrences closed form
            for recurrence in recurrences:
                summary.summary[-1].append(summary.assign_to_z3(recurrence.closed_form))
            # these closed form should outside of the oscillation interval
            expr_need = z3.substitute(expr, (z3.Int(main_var), summary.next_var[main_var]))
            summary.summary[-1].append(z3.Not(expr_need))
            # N > 0
            summary.summary[-1].append(summary.pre_var['N'] > 0)
            # todo: add pre n variables satisfied the loop condition

        return summary

    def check_after_loop(self, pre_val: list[z3.BoolRef], post_symbols: dict[str, z3.Int],
                         assertions: list[z3.BoolRef]):
        solver = z3.Solver()
        for pre_val_item in pre_val:
            solver.add(pre_val_item)
        if solver.check() == z3.unsat:
            raise Exception("Error checking assert")
        for trace_summary, trace_symbols in zip(self.traces_summary, self.traces_symbols):
            solver.push()
            expr = z3.Not(z3.And(assertions))
            for symbol_name, z3_var in post_symbols.items():
                if symbol_name not in trace_symbols.keys():
                    print("Symbol not found")
                    expr = z3.substitute(expr, (z3_var, z3.Int(f"{symbol_name}_0")))
                else:
                    expr = z3.substitute(expr, (z3_var, trace_symbols[symbol_name]))
            solver.add(expr)
            res = self.solver_check_trace(solver, trace_summary, trace_symbols)
            solver.pop()
            if res is not None:
                print("FAILED")
                return res
        print("SUCCESS")


class Summary:
    var_index: dict[str, int] = {}

    def __init__(self):
        self.pre_var: dict[str, z3.Int] = {}
        self.next_var: dict[str, z3.Int] = {}
        # if xxx, x'=f(x)
        # elif xxx, x'=g(x)
        # use push pop to check z3 sat
        self.summary: list[list[z3.ExprRef]] = []

    def append_assigns(self, assigns: list[Assign]):
        self.summary.append([])
        for assign in assigns:
            self.summary[-1].append(self.assign_to_z3(assign))

    def assign_to_z3(self, assign: Assign) -> z3.BoolRef:
        lvalue_symbol = assign.lvalue.symbols[0]
        if type(assign.rvalue) is INT:
            for symbol in assign.rvalue.symbols:
                if symbol.name not in self.pre_var.keys():
                    self.pre_var[symbol.name] = Summary.get_next_z3_var_by_name(symbol.name)
        elif type(assign.rvalue) is MUL_INT:
            for i in range(assign.rvalue.dimension):
                for symbol in assign.rvalue.multipliers[i].symbols:
                    if symbol.name not in self.pre_var.keys():
                        self.pre_var[symbol.name] = Summary.get_next_z3_var_by_name(symbol.name)
            for symbol in assign.rvalue.base_int.symbols:
                if symbol.name not in self.pre_var.keys():
                    self.pre_var[symbol.name] = Summary.get_next_z3_var_by_name(symbol.name)
        if lvalue_symbol.name not in self.pre_var.keys():
            self.pre_var[lvalue_symbol.name] = Summary.get_next_z3_var_by_name(lvalue_symbol.name)
        if lvalue_symbol.name not in self.next_var.keys():
            self.next_var[lvalue_symbol.name] = Summary.get_next_z3_var_by_name(lvalue_symbol.name)

        lz3: z3.ArithRef = self.next_var[assign.lvalue.symbols[0].name]
        if type(assign.rvalue) is INT:
            rz3 = assign.rvalue.addends
            for symbol, multiplier in zip(assign.rvalue.symbols, assign.rvalue.multipliers):
                rz3 += self.pre_var[symbol.name] * multiplier
        elif type(assign.rvalue) is MUL_INT:
            rz3 = assign.rvalue.to_z3(self.pre_var)
        else:
            rz3 = assign.rvalue
        return lz3 == rz3

    @classmethod
    def get_next_z3_var_by_name(cls, name):
        if name not in cls.var_index.keys():
            cls.var_index[name] = 0
        index = cls.var_index[name]
        index += 1
        cls.var_index[name] = index
        return z3.Int(f"{name}_{index}")

    @classmethod
    def get_z3_var_by_name(cls, name):
        if name not in cls.var_index.keys():
            cls.var_index[name] = 1
        index = cls.var_index[name]
        return z3.Int(f"{name}_{index}")
