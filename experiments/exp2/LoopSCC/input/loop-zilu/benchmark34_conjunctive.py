import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

n, j, k = INT.define_int("n"), INT.define_int("j"), INT.define_int("k")

loop = CFG.define_loop([[j < n, n > 0]], [
    (
        (j, j + 1),
        (k, k - 1),
    ),
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

k_pre = z3.Int('k_0')
j_pre = z3.Int('j_0')
n_pre = z3.Int('n_0')
k_post = z3.Int('k')

summarizer.check_after_loop([j_pre == 0, k_pre == n_pre, n_pre > 0],
                            {"k": k_post},
                            [k_post == 0])
