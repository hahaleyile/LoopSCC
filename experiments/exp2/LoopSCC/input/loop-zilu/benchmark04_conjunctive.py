import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

k, j, n = INT.define_int("k"), INT.define_int("j"), INT.define_int("n")

loop = CFG.define_loop([[j <= n - 1]], [
    (
        (j, j + 1),
        (k, k - 1),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()
k_pre = z3.Int('k_0')
j_pre = z3.Int('j_0')
n_pre = z3.Int('n_0')
k_post = z3.Int('k')
summarizer.check_after_loop([n_pre >= 1, k_pre >= n_pre, j_pre == 0], {"k": k_post}, [k_post >= 0])
