import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

i, s = INT.define_int("i"), INT.define_int("s")

loop = CFG.define_loop([[i > 0]], [
    [
        ([[s != 0]], [
            (
                (s, s + 1),
            )
        ]),
    ],
    (
        (i, i - 1),
    )
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

s_pre = z3.Int('s_0')
i_pre = z3.Int('i_0')
s_post = z3.Int('s')

summarizer.check_after_loop([s_pre == 0, i_pre > 0], {"s": s_post}, [s_post == 0])
