import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

i, k, x, y = INT.define_int("i"), INT.define_int("k"), INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop([[x <= y]], [
    (
        (i, i + 1),
        (k, k - 1),
        (x, x + 1),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

i_pre = z3.Int('i_0')
k_pre = z3.Int('k_0')
i_post = z3.Int('i')
k_post = z3.Int('k')

summarizer.check_after_loop([i_pre == 1, k_pre >= 0, k_pre <= 1],
                            {"i": i_post, "k": k_post},
                            [i_post + k_post >= 1, i_post + k_post <= 2, i_post >= 1])
