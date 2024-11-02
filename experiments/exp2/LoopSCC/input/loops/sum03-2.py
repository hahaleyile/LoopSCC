import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

i, n, x, sn, a = INT.define_int("i"), INT.define_int("n"), INT.define_int("x"), INT.define_int("sn"), INT.define_int(
    "a")

loop = CFG.define_loop([[i <= n]], [
    (
        (sn, sn + a),
        (x, x + 1),
        (i, i + 1),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()
x_pre = z3.Int('x_0')
sn_pre = z3.Int('sn_0')
sn_post = z3.Int('sn')
x_post = z3.Int('x')
a_post = z3.Int('a')
summarizer.check_after_loop([sn_pre == 0, x_pre == 0, z3.Int("a_0") == z3.Int("a_1")],
                            {"sn": sn_post, "x": x_post, "a": a_post},
                            [z3.Or(sn_post == x_post * a_post, sn_post == 0)])
