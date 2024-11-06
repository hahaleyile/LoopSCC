from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer
import z3

# Define symbolic variables
x = INT.define_int("x")

# Define the loop
loop = CFG.define_loop([[x < 0x0fffffff]], [
    (
        (x, x + 2),
    )
])

# Analyze the loop
spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

# Result verification
result = summarizer.solve([(x, 0)])
if int(result[0][1]) % 2 == 0:
    print("SUCCESS")
else:
    print("FAILED")
