import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop([[x + y <= -2]], [
    [
        ([[x > 0]], [
            (
                (x, x + 1),
            )
        ]),
        ([[x <= 0]], [
            (
                (y, y + 1),
            )
        ]),
    ],
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

x_pre = z3.Int('x_0')
y_pre = z3.Int('y_0')
x_post = z3.Int('x')
y_post = z3.Int('y')

summarizer.check_after_loop([z3.Or(x_pre > 0, y_pre > 0)],
                            {"x": x_post, "y": y_post},
                            [z3.Or(x_post > 0, y_post > 0)])
