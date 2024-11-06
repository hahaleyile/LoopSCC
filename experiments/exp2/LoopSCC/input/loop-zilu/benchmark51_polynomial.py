from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

# Step 1: Define symbolic variables
x,i = INT.define_int("x"), INT.define_int("i")

# Step 2: Loop definition
loop = CFG.define_loop([[i<x]], [
    [
        ([[x > 50]], [
            (
                (x, x + 1),
            )
        ]),
        ([[x <= 50]], [
            (
            )
        ]),
    ],
    [
        ([[x == 0]], [
        
            (
                (x, x + 1),
            )
        ]),
        ([[x < 0]], [
            (
                (x, x - 1),
            )
        ]),
        ([[x > 0]], [
            (
                (x, x - 1),
            )
        ]),
    ],
    (
        (i,i+1),
    ),
])

# Step 3: Loop analysis
spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

# Result verification for non-deterministic variables
import z3
x_pre = z3.Int('x_0')
x_post = z3.Int('x')
summarizer.check_after_loop([x_pre>=0, x_pre<=50],
                            {"x": x_post},
                            [0 <= x_post, x_post <= 50])
