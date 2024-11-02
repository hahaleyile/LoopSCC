import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x = INT.define_int("x")

loop = CFG.define_loop([[x < 100, x >= 0]], [
    (
        (x, x + 1),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

x_pre = z3.Int('x_0')
x_post = z3.Int('x')

summarizer.check_after_loop([x_pre >= 0],
                            {"x": x_post},
                            [x_post >= 100])
