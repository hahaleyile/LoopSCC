import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

i, x, y, w, z, det = INT.define_int("i"), INT.define_int("x"), INT.define_int("y"), INT.define_int("w"), INT.define_int(
    "z"), INT.define_int("det")

loop = CFG.define_loop([[i > 0]], [
    (
        (y, y + 1),
        (z, z + 1),
        (i, i - 1),
    )
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

x_pre = z3.Int('x_0')
y_pre = z3.Int('y_0')
z_pre = z3.Int('z_0')
w_pre = z3.Int('w_0')
x_post = z3.Int('x')
y_post = z3.Int('y')
z_post = z3.Int('z')
w_post = z3.Int('w')

summarizer.check_after_loop([x_pre == w_pre, y_pre == w_pre + 1, z_pre == x_pre + 1],
                            {"x": x_post, "y": y_post, "z": z_post, "w": w_post},
                            [z_post == y_post])
