from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer
import z3

# Define symbolic variables
x, y, z = INT.define_int("x"), INT.define_int("y"), INT.define_int("z")

# Define the loop
loop = CFG.define_loop([[x > 0]], [
    (
        (x, x - 1),
        (y, y - 1),
        (z, z + 2),
    )
])

# Initialize the spg and Summarizer
spg = SPath_Graph(loop)
summarizer = Summarizer(spg)

# Summarize the loop
summarizer.summarize()

# Define input and output variables for verification
x_pre = z3.Int('x_0')
x_post = z3.Int('x')
y_pre = z3.Int('y_0')
y_post = z3.Int('y')
z_pre = z3.Int('z_0')
z_post = z3.Int('z')

# Verify the result
summarizer.check_after_loop([y_pre == x_pre, x_pre >= 0, x_pre + y_pre + z_pre == 0], {"x": x_post, "y": y_post, "z": z_post}, [z_post <= 0])