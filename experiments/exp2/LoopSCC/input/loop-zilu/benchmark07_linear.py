import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

i, n, k, flag = INT.define_int("i"), INT.define_int("n"), INT.define_int("k"), INT.define_int("flag")

loop = CFG.define_loop([[i < n]], [
    (
        (i, i + 1),
    ),
    [
        ([[flag != 0]], [
            (
                (k, k + 4000),
            )
        ]),
        ([[flag == 0]], [
            (
                (k, k + 2000),
            )
        ]),
    ],
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()
i_pre = z3.Int('i_0')
n_pre = z3.Int('n_0')
k_post = z3.Int('k')
n_post = z3.Int('n')
summarizer.check_after_loop([i_pre == 0, n_pre > 0, n_pre < 10], {"k": k_post, "n": n_post}, [k_post > n_post])
