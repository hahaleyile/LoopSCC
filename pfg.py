import copy

import z3

from block import Branch, Path
from cfg import CFG
from condition import Condition, extend_z3_symbols_from_condition, extend_z3_symbols_from_assigns
from int import INT


def execute_path(path: Path, solver: z3.Solver, pre_symbols: dict[str, z3.Int], next_symbols):
    assigned: dict[str:int] = {symbol_name: 0 for symbol_name in pre_symbols.keys()}
    for assign in path.assigns:
        assigned[assign.lvalue.symbols[0].name] = 1
        lvalue = next_symbols[assign.lvalue.symbols[0].name]
        if type(assign.rvalue) is not INT:
            rvalue = assign.rvalue
        else:
            rvalue = assign.rvalue.addends
            for symbol, multiplier in zip(assign.rvalue.symbols, assign.rvalue.multipliers):
                rvalue += pre_symbols[symbol.name] * multiplier
        solver.add(lvalue == rvalue)

    for symbol_name, value in assigned.items():
        if value == 0:
            solver.add(next_symbols[symbol_name] == pre_symbols[symbol_name])


def path_can_jump(pre_path: Path, next_path: Path, loop_cond: Condition):
    solver = z3.Solver()
    pre_constraints = pre_path.precond
    next_constraints = next_path.precond

    pre_symbols: dict[str, z3.Int] = {}
    extend_z3_symbols_from_condition(pre_symbols, pre_constraints + next_constraints + loop_cond)
    extend_z3_symbols_from_assigns(pre_symbols, pre_path.assigns)
    next_symbols = {symbol: z3.Int(symbol + "'") for symbol in pre_symbols.keys()}
    solver.add((pre_constraints + loop_cond).to_z3(pre_symbols))
    solver.add((next_constraints + loop_cond).to_z3(next_symbols))
    execute_path(pre_path, solver, pre_symbols, next_symbols)

    if solver.check() == z3.sat:
        return True
    else:
        return False


def path_to_end(path: Path, loop_cond: Condition):
    solver = z3.Solver()
    symbols: dict[str, z3.Int] = {}
    extend_z3_symbols_from_condition(symbols, path.precond + loop_cond)
    extend_z3_symbols_from_assigns(symbols, path.assigns)
    solver.add((path.precond + loop_cond).to_z3(symbols))
    next_symbols = {symbol: z3.Int(symbol + "'") for symbol in symbols.keys()}
    execute_path(path, solver, symbols, next_symbols)
    solver.add(z3.Not(loop_cond.to_z3(next_symbols)))

    if solver.check() == z3.sat:
        return True
    else:
        return False


class PFG:
    def __init__(self, cfg: CFG):
        self.cfg = cfg
        self.branch = Branch(1, cfg.finish_node, cfg)
        self.path_arcs: dict[Path, set[Path]] = {}
        self.paths: list[Path] = []
        self.scc: list[SCC] = []
        # remember which node belongs to which scc
        self.belong_to_scc: list[int] = []
        # represent graph condensation
        self.scc_paths: list[list[int]] = []

        for path in self.branch.paths:
            new_path = copy.copy(path)
            new_path.chain.insert(0, 1)
            self.paths.append(new_path)

        for path in self.paths:
            self.path_arcs[path] = set()

        for pre_path in self.paths:
            for next_path in self.paths:
                if path_can_jump(pre_path, next_path, self.cfg.arcs_desc[(0, 1)]):
                    self.path_arcs[pre_path].add(next_path)

        self.end_paths_index: list[int] = []
        for path in self.paths:
            if path_to_end(path, self.cfg.arcs_desc[(0, 1)]):
                self.end_paths_index.append(self.paths.index(path))

        self.find_scc()
        for end_path_index in self.end_paths_index:
            self.scc[self.belong_to_scc[end_path_index]].to_end = True

        def dfs(u: int, stack: list[int]):
            stack.append(u)
            if self.scc[u].to_end:
                self.scc_paths.append(stack.copy())
            for next_scc in self.scc[u].next_scc:
                dfs(self.scc.index(next_scc), stack)
            stack.pop()

        # calculate all paths from start to end, under graph condensation situation
        for i in range(len(self.scc)):
            dfs(i, [])
        ranks = {}
        i = 0
        for scc_path in self.scc_paths:
            rank = 0
            for scc in scc_path:
                if len(self.scc[scc].nodes) > 1:
                    rank -= 100
                elif self.scc[scc].is_scc:
                    rank += 1
                else:
                    rank += 10
            ranks[i] = rank
            i += 1
        ranks = sorted(ranks.items(), key=lambda x: x[1], reverse=True)
        new_scc_paths = []
        for rank in ranks:
            new_scc_paths.append(self.scc_paths[rank[0]])
        self.scc_paths = new_scc_paths

    def to_dot(self):
        dot = "digraph pfg {\n"
        dot += "    start [label=\"start\"]\n"
        for i in range(len(self.paths)):
            label = "->".join([str(x) for x in self.paths[i].chain])
            dot += f"    {i} [label=\"{label}\"]\n"
        dot += "    end [label=\"end\"]\n"
        for i in range(len(self.paths)):
            dot += f"    start -> {i}\n"
        for pre_path, next_paths in self.path_arcs.items():
            for next_path in next_paths:
                dot += f"    {self.paths.index(pre_path)} -> {self.paths.index(next_path)}\n"
        for end_path_index in self.end_paths_index:
            dot += f"    {end_path_index} -> end\n"
        dot += "}"
        return dot

    # Use tarjan algorithm
    def find_scc(self):
        self.scc: list[SCC] = []
        visited: list[bool] = [False] * len(self.paths)
        stack: list[int] = []
        low: list[int] = [-1] * len(self.paths)
        dfs_num: list[int] = [-1] * len(self.paths)
        dfs_cnt = 0
        visit_cnt = 0
        self.belong_to_scc = [-1] * len(self.paths)

        def tarjan(u):
            nonlocal dfs_cnt, visit_cnt
            visited[u] = True
            visit_cnt += 1
            dfs_num[u] = dfs_cnt
            low[u] = dfs_cnt
            dfs_cnt += 1
            stack.append(u)
            for next_path in self.path_arcs[self.paths[u]]:
                v = self.paths.index(next_path)
                if v == u:
                    continue
                if not visited[v]:
                    tarjan(v)
                    low[u] = min(low[u], low[v])
                elif v in stack:
                    low[u] = min(low[u], low[v])

            if low[u] == dfs_num[u]:
                scc = []
                is_scc = True
                while stack[-1] != u:
                    scc.append(stack.pop())
                scc.append(stack.pop())
                self_path = self.paths[scc[0]]
                # a path can recursively jump to itself is a scc
                if len(scc) == 1 and self_path not in self.path_arcs[self_path]:
                    is_scc = False
                new_scc = SCC(scc, is_scc)
                scc_index = len(self.scc)
                for node in scc:
                    self.belong_to_scc[node] = scc_index
                self.scc.append(new_scc)

        while visit_cnt < len(self.paths):
            dfs_cnt = 0
            for i in range(len(self.paths)):
                if not visited[i]:
                    tarjan(i)

        for pre_path, next_paths in self.path_arcs.items():
            pre_scc_index = self.belong_to_scc[self.paths.index(pre_path)]
            for next_path in next_paths:
                next_scc_index = self.belong_to_scc[self.paths.index(next_path)]
                if pre_scc_index != next_scc_index:
                    self.scc[pre_scc_index].next_scc.add(self.scc[next_scc_index])


class SCC:
    def __init__(self, nodes: list[int], is_scc: bool):
        self.nodes: list[int] = nodes
        self.is_scc: bool = is_scc
        self.next_scc: set[SCC] = set()
        self.to_end: bool = False

    def __repr__(self):
        return str(sorted(self.nodes))
