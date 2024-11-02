import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

i, n, sn, a = INT.define_int("i"), INT.define_int("n"), INT.define_int("sn"), INT.define_int("a")

loop = CFG.define_loop([[i <= n]], [
    (
        (sn, sn + a),
        (i, i + 1),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()
i_pre = z3.Int('i_0')
n_pre = z3.Int('n_0')
sn_pre = z3.Int('sn_0')
sn_post = z3.Int('sn')
n_post = z3.Int('n')
a_post = z3.Int('a')
summarizer.check_after_loop([i_pre == 1, sn_pre == 0, n_pre < 1000, n_pre >= -1000, z3.Int("a_0") == z3.Int("a_1")],
                            {"sn": sn_post, "n": n_post, "a": a_post},
                            [z3.Or(sn_post == n_post * a_post, sn_post == 0)])
