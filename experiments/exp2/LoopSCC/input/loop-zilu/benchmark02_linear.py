import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

n, i, l = INT.define_int("n"), INT.define_int("i"), INT.define_int("l")

loop = CFG.define_loop([[i < n]], [
    (
        (i, i + 1),
    ),
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()
i_pre = z3.Int('i_0')
l_pre = z3.Int('l_0')
l_post = z3.Int('l')
summarizer.check_after_loop([l_pre > 0, i_pre == l_pre], {"l": l_post}, [l_post >= 1])
