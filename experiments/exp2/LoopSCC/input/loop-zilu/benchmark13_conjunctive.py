import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

i, j, k = INT.define_int("i"), INT.define_int("j"), INT.define_int("k")

loop = CFG.define_loop([[i <= k]], [
    (
        (i, i + 1),
        (j, j + 1),
    ),
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

i_pre = z3.Int('i_0')
j_pre = z3.Int('j_0')
i_post = z3.Int('i')
j_post = z3.Int('j')

summarizer.check_after_loop([i_pre == 0, j_pre == 0],
                            {"i": i_post, "j": j_post},
                            [i_post == j_post])
