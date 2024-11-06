from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer
import z3

# Define symbolic variables
x, y, z = INT.define_int("x"), INT.define_int("y"), INT.define_int("z")
i = INT.define_int("i")
# Define loop
loop = CFG.define_loop([[i<z]], [
    [
        ([[x > 0]], [
            (
                (x, x + 1),
            )
        ]),
        ([[x <= 0]], [
            (
            )
        ]),
    ],
    [
        ([[y > 0]], [
            (
                (y, y + 1),
            )
        ]),
        ([[y <= 0]], [
            (
                (z, z + 1),
            )
        ]),
    ],
    (
        (i,i+1),
    )
])

# Loop analysis
spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

# Define input and output variables using z3
x_pre = z3.Int('x_0')
x_post = z3.Int('x')
y_pre = z3.Int('y_0')
y_post = z3.Int('y')
z_pre = z3.Int('z_0')
z_post = z3.Int('z')

# Result verification
summarizer.check_after_loop([z3.Or(y_pre > 0, x_pre > 0, z_pre > 0)], {"x": x_post, "y": y_post, "z": z_post}, [z3.Or(x_post > 0, y_post > 0, z_post > 0)])
