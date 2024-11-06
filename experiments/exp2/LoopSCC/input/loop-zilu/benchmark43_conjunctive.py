from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer
import z3

# Define symbolic variables
x, y = INT.define_int("x"), INT.define_int("y")

# Define loop
loop = CFG.define_loop([[x < 100, y < 100]], [
    (
        (x, x + 1),
        (y, y + 1),
    )
])

# Analyze loop
spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

# Result verification (Type 1: Non-deterministic Variables)
x_pre = z3.Int('x_0')
x_post = z3.Int('x')
y_pre = z3.Int('y_0')
y_post = z3.Int('y')
summarizer.check_after_loop([x_pre < 100, y_pre < 100],
                            {"x": x_post, "y": y_post},
                            [z3.Or(x_post == 100 , y_post == 100)])
