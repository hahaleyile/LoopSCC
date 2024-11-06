# can;t handle
from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop([[x < 6]], [
    (
        (x, x + 1),
        (y, y * 2),
    )
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

# Define initial values
test = [(x, 0), (y, 1)]

# Solve and assert results
result = summarizer.solve(test)
for symbol_val in result:
    if symbol_val[0] == "x":
        if int(symbol_val[1]) != 6:
            print("SUCCESS")
        else:
            print("FAILED")