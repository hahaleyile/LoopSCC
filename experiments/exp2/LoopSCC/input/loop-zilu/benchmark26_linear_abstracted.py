import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop([[x < y]], [
    (
        (x, x + 1),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

x_pre = z3.Int('x_0')
y_pre = z3.Int('y_0')
x_post = z3.Int('x')
y_post = z3.Int('y')

summarizer.check_after_loop([x_pre < y_pre],
                            {"x": x_post, "y": y_post},
                            [x_post == y_post])
