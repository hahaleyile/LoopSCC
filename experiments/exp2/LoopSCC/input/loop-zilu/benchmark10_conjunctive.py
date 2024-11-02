import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

i, c = INT.define_int("i"), INT.define_int("c")

loop = CFG.define_loop([[i < 100, i > 0]], [
    (
        (c, c + i),
        (i, i + 1),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()
i_pre = z3.Int('i_0')
c_pre = z3.Int('c_0')
c_post = z3.Int('c')
summarizer.check_after_loop([i_pre == 0, c_pre == 0],
                            {"c": c_post},
                            [c_post >= 0])
