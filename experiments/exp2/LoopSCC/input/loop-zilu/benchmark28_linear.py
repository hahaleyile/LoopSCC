import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

i, j = INT.define_int("i"), INT.define_int("j")

loop = CFG.define_loop([[i < j]], [
    (
        (j, j - i),
    ),
    [
        ([[j < i]], [
            (
                (j, j + i),
                (i, j - i),
                (j, j - i),
            )
        ]),
        ([[j >= i]], [
            ()
        ]),
    ],
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

i_pre = z3.Int('i_0')
j_pre = z3.Int('j_0')
i_post = z3.Int('i')
j_post = z3.Int('j')

summarizer.check_after_loop([i_pre * i_pre < j_pre * j_pre],
                            {"i": i_post, "j": j_post},
                            [i_post == j_post])
