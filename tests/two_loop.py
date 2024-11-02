from cfg import CFG
from int import INT
from pfg import PFG
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
pfg = PFG(loop)
print(len(pfg.paths))
summarizer = Summarizer(pfg)
summarizer.summarize_two_node_scc(summarizer.pfg.scc[0])
