import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

i, k, n = INT.define_int("i"), INT.define_int("k"), INT.define_int("n")

loop = CFG.define_loop([[i < n]], [
    (
        (k, k - 1),
        (i, i + 2),
    ),
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()
i_pre = z3.Int('i_0')
k_pre = z3.Int('k_0')
n_pre = z3.Int('n_0')
k_post = z3.Int('k')
n_post = z3.Int('n')
summarizer.check_after_loop([i_pre == 0, k_pre == n_pre, n_pre >= 0],
                            {"k": k_post, "n": n_post},
                            [2 * k_post >= n_post - 1])
