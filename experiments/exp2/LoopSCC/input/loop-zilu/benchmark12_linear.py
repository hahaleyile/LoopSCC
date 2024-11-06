import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, y, t, i = INT.define_int("x"), INT.define_int("y"), INT.define_int("t"), INT.define_int("i")

loop = CFG.define_loop([[i < t]], [
    [
        ([[x > 0]], [
            (
                (y, y + x),
            )
        ]),
        ([[x < 0]], [
            ()
        ]),
    ],
    (
        (i, i + 1),
    ),
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()
x_pre = z3.Int('x_0')
y_pre = z3.Int('y_0')
t_pre = z3.Int('t_0')
y_post = z3.Int('y')
t_post = z3.Int('t')
summarizer.check_after_loop([x_pre != y_pre, y_pre == t_pre], {"y": y_post, "t": t_post}, [y_post >= t_post])
