import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, y, i, k = INT.define_int("x"), INT.define_int("y"), INT.define_int("i"), INT.define_int("k")

loop = CFG.define_loop([[i < k]], [
    (
        (x, x + 1),
        (y, y + 1),
        (i, i + 1),
    ),
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

x_pre = z3.Int('x_0')
y_pre = z3.Int('y_0')
x_post = z3.Int('x')
y_post = z3.Int('y')

summarizer.check_after_loop([x_pre == y_pre],
                            {"x": x_post, "y": y_post},
                            [x_post == y_post])
