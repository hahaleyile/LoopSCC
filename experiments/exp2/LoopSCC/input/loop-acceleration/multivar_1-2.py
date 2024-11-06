from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer
import z3

x, y = INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop([[x < 1024]], [
    (
        (x, x + 1),
        (y, y + 1),
    )
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

x_pre = z3.Int('x_0')
x_post = z3.Int('x')
y_pre = z3.Int('y_0')
y_post = z3.Int('y')

summarizer.check_after_loop([y_pre == x_pre+1], {"x": x_post, "y": y_post}, [x_post == y_post])
