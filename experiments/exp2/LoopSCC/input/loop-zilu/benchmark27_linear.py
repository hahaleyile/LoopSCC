import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

i, j, k = INT.define_int("i"), INT.define_int("j"), INT.define_int("k")

loop = CFG.define_loop([[i < j]], [
    (
        (k, k + 1),
        (i, i + 1),
    ),
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()
i_pre = z3.Int('i_0')
j_pre = z3.Int('j_0')
k_pre = z3.Int('k_0')
k_post = z3.Int('k')
summarizer.check_after_loop([i_pre < j_pre, k_pre > i_pre - j_pre],
                            {"k": k_post},
                            [k_post > 0])
