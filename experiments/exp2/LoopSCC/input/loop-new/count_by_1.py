from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

i = INT.define_int("i")

loop = CFG.define_loop([[i < 1000000]], [
    (
        (i, i + 1),
    )
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

result = summarizer.solve([(i,0)])
for symbol_val in result:
    if symbol_val[0] == 'i':
        if int(symbol_val[1]) == 1000000:
            print("SUCCESS")
        else:
            print("FAILED")