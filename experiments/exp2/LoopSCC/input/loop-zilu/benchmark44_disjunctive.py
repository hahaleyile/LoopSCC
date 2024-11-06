from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer
import z3

x, y = INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop([[x < y]], [
    [
        ([[x < 0, y < 0]], [
            (
                (x, x + 7),
                (y, y - 10),
            )
        ]),
        ([[x < 0, y >= 0]], [
            (
                (x, x + 7),
                (y, y + 3),
            )
        ]),
        ([[x>=0]], [
            (
                (x, x + 10),
                (y, y + 3),
            )
        ]),
    ]
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

x_pre = z3.Int('x_0')
x_post = z3.Int('x')
y_pre = z3.Int('y_0')
y_post = z3.Int('y')

summarizer.check_after_loop([x_pre < y_pre], {"x": x_post, "y": y_post}, [x_post >= y_post, x_post <= y_post + 16])
