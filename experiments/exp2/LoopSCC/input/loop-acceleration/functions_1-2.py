from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer
import z3

x = INT.define_int("x")
x_pre = z3.Int('x_0')
x_post = z3.Int('x')

loop = CFG.define_loop([[x < 0x0fffffff]], [
    (
        (x, x + 2),
    )
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

result = summarizer.solve([(x, 0)])
if int(result[0][1]) % 2 == 1:
    print("SUCCESS")
else:
    print("FAILED")

