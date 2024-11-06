import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, n = INT.define_int("x"), INT.define_int("n")

loop = CFG.define_loop([[x < n]], [
    (
        (x, x + 1),
    ),
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()
x_pre = z3.Int('x_0')
n_pre = z3.Int('n_0')
x_post = z3.Int('x')
n_post = z3.Int('n')
summarizer.check_after_loop([x_pre == 0, n_pre > 0], {"x": x_post, "n": n_post}, [x_post == n_post])
