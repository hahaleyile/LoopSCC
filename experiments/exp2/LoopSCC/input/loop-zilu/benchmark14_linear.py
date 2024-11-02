import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

i = INT.define_int("i")

loop = CFG.define_loop([[i > 0]], [
    (
        (i, i - 1),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

i_pre = z3.Int('i_0')
i_post = z3.Int('i')

summarizer.check_after_loop([i_pre >= 0, i_pre <= 200],
                            {"i": i_post},
                            [i_post >= 0])
