import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop([[x > 0]], [
    (
        (x, x - 1),
        (y, y - 1),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

x_pre = z3.Int('x_0')
y_pre = z3.Int('y_0')
y_post = z3.Int('y')

summarizer.check_after_loop([x_pre == y_pre, x_pre >= 0],
                            {"y": y_post},
                            [y_post >= 0])
