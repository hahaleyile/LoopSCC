import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, y, k = INT.define_int("x"), INT.define_int("y"), INT.define_int("k")

loop = CFG.define_loop([[x < 99]], [
    [
        ([[y == k * 2]], [
            (
                (x, x + 2),
            )
        ]),
        ([[y != k * 2]], [
            (
                (x, x + 1),
            )
        ]),
    ],
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

x_pre = z3.Int('x_0')
y_pre = z3.Int('y_0')
k_pre = z3.Int('k_0')
x_post = z3.Int('x')
y_post = z3.Int('y')

summarizer.check_after_loop([x_pre == 0, k_pre == y_pre / 2], {"x": x_post, "y": y_post}, [x_post % 2 == y_post % 2])
