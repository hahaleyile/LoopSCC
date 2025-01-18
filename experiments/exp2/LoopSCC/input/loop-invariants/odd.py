import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

i, x = INT.define_int("i"), INT.define_int("x")

loop = CFG.define_loop([[i > 0]], [
    (
        (x, x + 2),
        (i, i - 1),
    )
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

x_pre = z3.Int('x_0')
i_pre = z3.Int('i_0')
x_post = z3.Int('x')

summarizer.check_after_loop([x_pre == 1], {"x": x_post}, [x_post % 2 != 0])
