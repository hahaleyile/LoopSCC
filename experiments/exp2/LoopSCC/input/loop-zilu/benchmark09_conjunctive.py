import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop([[x > 0, y >= 0]], [
    (
        (x, x - 1),
        (y, y - 1),
    ),
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()
x_pre = z3.Int('x_0')
y_pre = z3.Int('y_0')
y_post = z3.Int('y')
summarizer.check_after_loop([x_pre == y_pre, y_pre >= 1], {"y": y_post}, [y_post == 0])
