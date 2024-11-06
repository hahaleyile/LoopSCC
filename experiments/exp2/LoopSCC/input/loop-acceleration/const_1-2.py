from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

# Step 1: Define Symbolic Variables
x, y = INT.define_int("x"), INT.define_int("y")

# Step 2: Loop Definition
loop = CFG.define_loop([[y < 1024]], [
    (
        (x, 0),
        (y, y+1),
    )
])

# Step 3: Loop Analysis
spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

# Result Verification
# Type 2: Loops with Initial Values
test = [(x, 1), (y, 0)]
result = summarizer.solve(test)
for symbol_val in result:
    if symbol_val[0] == "x":
        if int(symbol_val[1]) == 1:
            print("SUCCESS")
        else:
            print("FAILED")
