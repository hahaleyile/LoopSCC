import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, y, i, j, k, a, b = (INT.define_int("x"), INT.define_int("y"), INT.define_int("i"), INT.define_int("j"),
                       INT.define_int("k"), INT.define_int("a"), INT.define_int("b"))

loop = CFG.define_loop([[a < b]], [
    [
        ([[j == i]], [
            (
                (x, x + 1),
                (y, y - 1),
            )
        ]),
        ([[j < i]], [
            (
                (x, x - 1),
                (y, y + 1),
            )
        ]),
        ([[j > i]], [
            (
                (x, x - 1),
                (y, y + 1),
            )
        ]),
    ],
    (
        (a, a + 1),
        (j, j + 1),
    ),
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

j_pre = z3.Int('j_0')
x_pre = z3.Int('x_0')
y_pre = z3.Int('y_0')
k_pre = z3.Int('k_0')
x_post = z3.Int('x')
y_post = z3.Int('y')
k_post = z3.Int('k')

summarizer.check_after_loop([x_pre + y_pre == k_pre, j_pre == 0],
                            {"x": x_post, "y": y_post, "k": k_post},
                            [x_post + y_post == k_pre])
