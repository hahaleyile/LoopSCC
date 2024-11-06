import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

low, mid, high = INT.define_int("low"), INT.define_int("mid"), INT.define_int("high")

loop = CFG.define_loop([[mid > 0]], [
    (
        (low, low + 1),
        (mid, mid - 1),
        (high, high - 1),
    ),
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

low_pre = z3.Int('low_0')
mid_pre = z3.Int('mid_0')
high_pre = z3.Int('high_0')
low_post = z3.Int('low')
high_post = z3.Int('high')

summarizer.check_after_loop([low_pre == 0, mid_pre >= 1, high_pre == 2 * mid_pre],
                            {"low": low_post, "high": high_post},
                            [low_post == high_post])
