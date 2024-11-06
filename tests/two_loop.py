from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, i = INT.define_int("x"), INT.define_int("i")

loop = CFG.define_loop([[i < 100]], [
    [
        ([[x <= 5]], [
            (
                # lvalue, rvalue
                (x, x + 1),
            )
        ]),
        ([[x > 5]], [
            (
                (x, x - 4),
            )
        ]),
    ], [
        ([[x < 8]], [
            (
                (x, x + 2),
            )
        ]),
        ([[x >= 8]], [
            (
                (x, x - 3),
            )
        ]),
    ], (
        (i, i + 1),
    )
])

print(loop.to_dot())
print(loop.get_dominators(1, len(loop.nodes) - 1))
spg = SPath_Graph(loop)
print(len(spg.paths))
summarizer = Summarizer(spg)
summarizer.summarize_two_node_scc(summarizer.spg.scc[0])
