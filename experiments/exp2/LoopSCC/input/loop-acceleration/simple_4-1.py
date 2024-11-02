from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x = INT.define_int("x")

loop = CFG.define_loop([[x > 1]], [
    (
        (x, x - 2),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

test = [(x, 0x0ffffff1)]
result = summarizer.solve(test)
for symbol_val in result:
    if symbol_val[0] == "x":
        if int(symbol_val[1]) % 2 == 0:
            print("SUCCESS")
        else:
            print("FAILED")