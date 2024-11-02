import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x, y, n = INT.define_int("x"), INT.define_int("y"), INT.define_int("n")

loop = CFG.define_loop([[x > 0]], [
    (
        (x, x - 1),
        (y, y + 1),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()
x_pre = z3.Int('x_0')
y_pre = z3.Int('y_0')
n_pre = z3.Int('n_0')
y_post = z3.Int('y')
n_post = z3.Int('n')
summarizer.check_after_loop([x_pre == n_pre, y_pre == 0], {"y": y_post, "n": n_post}, [y_post != n_post])
