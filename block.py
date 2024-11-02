import copy

from cfg import CFG
from condition import Condition
from constraint import Constraint
from int import INT
from node import Assign


class Block:
    def __init__(self, start_node: int, end_node: int, cfg: CFG):
        self.start_node = start_node
        self.end_node = end_node
        self.paths: list[Path] = []
        self.branches: list[Branch] = []
        if start_node == end_node:
            raise Exception("start node and end node are the same")
        else:
            self.branch_num = len(cfg.arcs[start_node])
        if self.branch_num > 1:
            for start_node_child in cfg.arcs[start_node]:
                self.branches.append(Branch(start_node_child, end_node, cfg))

                # sub-branch has at lease one path
                new_paths = self.branches[-1].paths
                for new_path in new_paths:
                    append_path = Path()
                    append_path.chain += [start_node_child]
                    # the branch head node has assigns
                    if (len(cfg.nodes[start_node_child].assigns) > 0 and
                            cfg.nodes[start_node_child].assigns[0].rvalue
                            is not None):
                        append_path.assigns = copy.deepcopy(cfg.nodes[start_node_child].assigns)
                    if (start_node, start_node_child) in cfg.arcs_desc:
                        append_path.precond += cfg.arcs_desc[(start_node, start_node_child)]

                    # begin to merge
                    append_path.chain += new_path.chain
                    append_path.concat_precond(new_path.precond)
                    for assign in new_path.assigns:
                        Assign.merge_list(append_path.assigns, assign)
                    if append_path.precond.is_sat():
                        self.paths.append(append_path)

        # exit node path generate
        if self.branch_num == 1:
            self.paths.append(Path())
            self.paths[0].chain += [end_node]
            for assign in cfg.nodes[end_node].assigns:
                Assign.merge_list(self.paths[0].assigns, assign)

            if (start_node, end_node) in cfg.arcs_desc:
                self.paths[0].precond += cfg.arcs_desc[(start_node, end_node)]


class Branch:
    def __init__(self, start_node: int, end_node: int, cfg: CFG):
        self.start_node = start_node
        self.end_node = end_node
        self.paths: list[Path] = []
        self.blocks: list[Block] = []
        if start_node == end_node:
            raise Exception("start node and end node are the same")
        else:
            self.dominators = cfg.get_dominators(start_node, end_node)
            for i in range(len(self.dominators) - 1):
                self.blocks.append(Block(self.dominators[i], self.dominators[i + 1], cfg))

        # get paths from blocks
        # branch has at least one block
        index = 0
        append_paths: list[list[Path]] = [[], []]
        append_paths[index]: list[Path] = self.blocks[0].paths.copy()
        for i in range(1, len(self.blocks)):
            append_paths[1 - index].clear()

            for prev_path in append_paths[index]:
                for next_path in self.blocks[i].paths:
                    append_path = copy.copy(prev_path)
                    append_path.chain += next_path.chain
                    append_path.concat_precond(next_path.precond)
                    for next_path_assign in next_path.assigns:
                        Assign.merge_list(append_path.assigns, next_path_assign)
                    if append_path.precond.is_sat():
                        append_paths[1 - index].append(append_path)
            index = 1 - index

        self.paths = append_paths[index]


class Path:
    def __init__(self):
        self.chain: list[int] = []
        self.assigns: list[Assign] = []
        self.precond: Condition = Condition([])

    def __copy__(self):
        res = Path()
        res.chain = self.chain.copy()
        res.assigns = copy.deepcopy(self.assigns)
        res.precond = copy.deepcopy(self.precond)
        return res

    def __repr__(self):
        res = (f"{[node for node in self.chain]}: "
               f"{self.precond} -> {[assign for assign in self.assigns]}")
        return res

    def concat_precond(self, precond: Condition):
        post_var: dict[str, Assign] = {}
        for assign in self.assigns:
            post_var[assign.lvalue.symbols[0].name] = assign

        def symbol_substitute(value, symbols: dict[str, Assign]):
            if type(value) is not INT:
                return value
            else:
                new_value = value.addends
                for symbol, multiplier in zip(value.symbols, value.multipliers):
                    if symbol.name in symbols.keys():
                        new_value += symbols[symbol.name].rvalue * multiplier
                    else:
                        new_value += INT.define_int(symbol.name) * multiplier
                return new_value

        new_condition = []
        for conjunction in precond.conjunctions:
            new_conjunction = []
            for constraint in conjunction:
                new_conjunction.append(Constraint(
                    symbol_substitute(constraint.lvalue, post_var),
                    constraint.comparison,
                    symbol_substitute(constraint.rvalue, post_var)
                ))
            new_condition.append(new_conjunction)
        self.precond += Condition(new_condition)
