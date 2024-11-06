from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer
import z3

x = INT.define_int("x")

loop = CFG.define_loop([[x < 0x0fffffff]], [
    [
        ([[x < 0xfff0]], [
            (
                (x, x + 1),
            )
        ]),
        ([[x >= 0xfff0]], [
            (
                (x, x + 2),
            )
        ]),
    ]
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

result = summarizer.solve([(x, 0)])
for symbol_val in result:
    if symbol_val[0] == "x":
        if int(symbol_val[1]) % 2 == 0:
            print("SUCCESS")
        else:
            print("FAILED")
