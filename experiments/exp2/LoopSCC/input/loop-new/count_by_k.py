import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

i, k, LARGE_INT = INT.define_int("i"), INT.define_int("k"), INT.define_int("LARGE_INT")

loop = CFG.define_loop([[i < 1000000 * k]], [
    (
        (i, i + k),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

i_pre = z3.Int('i_0')
k_pre = z3.Int('k_0')
i_post = z3.Int('i')
k_post = z3.Int('k')

summarizer.check_after_loop([i_pre == 0, k_pre >= 0, k_pre <= 10],
                            {"i": i_post, "k": k_post},
                            [i_post == k_post * 1000000])