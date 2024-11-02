from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer
import z3

# Define symbolic variables
x = INT.define_int("x")

# Define loop
loop = CFG.define_loop([[x < 0x0fffffff]], [
    (
        (x, x + 1),
    )
])

# Analyze loop
pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

# Define input and output variables
x_pre = z3.Int('x_0')
x_post = z3.Int('x')

# Result verification
summarizer.check_after_loop([], {"x": x_post}, [x_post > 0x0fffffff])
