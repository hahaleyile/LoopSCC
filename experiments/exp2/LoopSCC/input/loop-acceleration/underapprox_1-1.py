# can;t handle
from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop([[x < 6]], [
    (
        (x, x + 1),
        (y, y * 2),
    )
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

# Define initial values
test = [(x, 0), (y, 1)]

# Solve and assert results
result = summarizer.solve(test)
for symbol_val in result:
    if symbol_val[0] == "y":
        if int(symbol_val[1]) != 64:
            print("SUCCESS")
        else:
            print("FAILED")