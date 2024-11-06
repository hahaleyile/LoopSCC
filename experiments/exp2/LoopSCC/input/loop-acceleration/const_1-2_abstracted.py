from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

test = [(x, 1), (y, 0)]
loop = None  # No explicit loop in the original C code

# Since the loop is not explicitly defined, create a dummy loop that doesn't change variables.
loop = CFG.define_loop([[True]], [
    [
        ([[True]], [
            (
                (x, x),  # x remains the same
                (y, y + 1024 - y),  # Update y directly as per the original code block.
            )
        ]),
    ]
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)

result = summarizer.solve(test)
for symbol_val in result:
    if symbol_val[0] == "x":
        if int(symbol_val[1]) == 1:
            **print**("SUCCESS")
        else:
            **print**("FAILED")
