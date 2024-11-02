from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer
import z3

a = INT.define_int("a")

loop = CFG.define_loop([[a < 6]], [
    (
        (a, a + 1),
    )
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()


result = summarizer.solve([(a, 0)])
for symbol_val in result:
    if symbol_val[0] == "a":
        if int(symbol_val[1]) == 6:
            print("SUCCESS")
        else:
            print("FAILED")