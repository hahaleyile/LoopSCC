from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer
import z3

# Define symbolic variables
x, y = INT.define_int("x"), INT.define_int("y")
i = INT.define_int("i")
# Define loop with conditions and body
loop = CFG.define_loop([[i<x]], [
    [
        ([[x > 0]], [
            (
                (x, x + 1),
            )
        ]),
        ([[x <= 0]], [
            (
                (y, y + 1),
            ),
        ]),
    ],
    (
        (i,i+1),
    )
])

# Analyze the loop
pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

# Define input and output variables for verification
x_pre = z3.Int('x_0')
x_post = z3.Int('x')
y_pre = z3.Int('y_0')
y_post = z3.Int('y')

# Check the verification condition
summarizer.check_after_loop([z3.Or(y_pre > 0 , x_pre > 0)], {"x": x_post, "y": y_post}, [z3.Or(x_post > 0 , y_post > 0)])
