from condition import Condition
from constraint import Constraint
from node import Node, Assign


class CFG:
    def __init__(self):
        self.nodes: list[Node] = []
        self.arcs: dict[int, set[int]] = {}
        self.arcs_desc: dict[tuple[int, int], Condition] = {}
        self.finish_node = 0

    @classmethod
    def define_loop(cls, loop_cond: list[list[Constraint]], body):
        cfg = cls()
        cfg.new_node(instr="")
        cfg.new_node(instr="")
        cfg.arcs[0].add(1)
        cfg.arcs_desc[(0, 1)] = Condition(loop_cond)
        cfg.finish_node = handle_body(cfg, 1, body)
        # cfg.edges[finish_node].add(0)
        # cfg.edges_desc[(finish_node, 0)] = ""
        # cfg.nodes.append(Node("end"))
        # cfg.edges.append((0, len(cfg.nodes) - 1, ""))

        if cfg.topological_sort() is False:
            print(f"cycle detected")
            exit(1)

        return cfg

    def new_node(self, instr=None, block: tuple = None):
        node = Node()
        if instr is not None:
            node.assigns.append(Assign(instr=instr))
        else:
            for assign in block:
                Assign.merge_list(node.assigns, Assign(assign=assign))
        self.nodes.append(node)
        self.arcs[len(self.nodes) - 1] = set()

    def to_dot(self):
        dot = "digraph cfg {\n"
        for i, node in enumerate(self.nodes):
            if str(node):
                dot += f"    {i} [label=\"{i}\\n{node}\"]\n"
            else:
                dot += f"    {i} [label=\"{i}\"]\n"
        for head, tails in self.arcs.items():
            for tail in tails:
                if (head, tail) in self.arcs_desc:
                    # dot += f"    {head} -> {tail} [label=\"{self.arcs_desc[(head, tail)]}\"]\n"
                    dot += f"    {head} -> {tail} [label=\""
                    dot += f"{self.arcs_desc[(head, tail)]}"
                    dot += "\"]\n"
                else:
                    dot += f"    {head} -> {tail}\n"
        dot += "}"
        return dot

    # topological sort for the cfg
    def topological_sort(self):
        visited = [False] * len(self.nodes)
        visited[0] = True
        stack = [1]
        visited[1] = True
        indegree = [0] * len(self.nodes)
        for head, tails in self.arcs.items():
            for tail in tails:
                indegree[tail] += 1

        # topological sort
        while stack:
            node = stack[-1]
            stack.pop()
            for tail in self.arcs[node]:
                indegree[tail] -= 1
                if indegree[tail] == 0:
                    stack.append(tail)
                    visited[tail] = True

        # detect circle
        for i in visited:
            if not i:
                return False
        return True

    # use data-flow equation
    def get_dominators(self, begin, end):
        # use typological sort to get a sequence
        # this method is different
        # because it is a subgraph typological sort
        # use reverse post-order dfs instead
        # dfs can ensure every node is needed
        visited = [False] * len(self.nodes)
        sequence = []
        self.post_order_dfs(begin, visited, sequence, end)

        new_sequence = list(reversed(sequence))
        assert new_sequence[0] == begin
        dominators = [set() for _ in range(len(self.nodes))]
        for node in new_sequence:
            dominators[node].add(node)
            for tail in self.arcs[node]:
                if not dominators[tail]:
                    dominators[tail] = dominators[node].copy()
                else:
                    dominators[tail] = dominators[tail].intersection(dominators[node])

        dominators_list = []
        for node in new_sequence:
            if node in dominators[end]:
                dominators_list.append(node)
        dominators_list.append(end)
        return dominators_list

    # https://eli.thegreenplace.net/2015/directed-graph-traversal-orderings-and-applications-to-data-flow-analysis
    def post_order_dfs(self, node, visited, sequence, end):
        visited[node] = True
        if node == end:
            return
        for tail in self.arcs[node]:
            if not visited[tail]:
                self.post_order_dfs(tail, visited, sequence, end)
        sequence.append(node)


# desc is the description of the last node point to the body
def handle_body(cfg: CFG, last_node, body, desc=""):
    for block in body:
        # loop, not consider now
        if type(block) is CFG:
            print("loop in cfg")
            pass

        # sequence
        elif type(block) is tuple:
            index = len(cfg.nodes)
            cfg.new_node(block=block)
            cfg.arcs[last_node].add(index)
            if type(desc) is list:
                cfg.arcs_desc[(last_node, index)] = Condition(desc)
            last_node = index

        # branch
        elif type(block) is list:
            finish_nodes = []
            for branch in block:
                index = len(cfg.nodes)
                if type(branch[1][0]) is tuple:
                    finish_nodes.append(handle_body(cfg, last_node, branch[1], branch[0]))

                # nested branch
                else:
                    cfg.new_node(instr="")
                    cfg.arcs[last_node].add(index)
                    if type(branch[0]) is list:
                        cfg.arcs_desc[(last_node, index)] = Condition(branch[0])
                    finish_nodes.append(handle_body(cfg, index, branch[1]))

            index = len(cfg.nodes)
            cfg.new_node(instr="")
            for finish_node in finish_nodes:
                cfg.arcs[finish_node].add(index)
            last_node = index

        # undefined
        else:
            print("undefined structure in cfg")
            pass

    return last_node
