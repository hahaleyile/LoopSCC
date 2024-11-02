from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop([[y < 1024]], [
    (
        (x, 0),
        (y, y + 1),
    )
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

# Define initial values
test = [(x, 1), (y, 0)]

# Solve and assert results
result = summarizer.solve(test)
for symbol_val in result:
    if symbol_val[0] == 'x':
        if int(symbol_val[1]) == 0:
            print("SUCCESS")
        else:
            print("FAILED")
