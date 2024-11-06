from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer
import z3

# Define symbolic variables
i, j, r = INT.define_int("i"), INT.define_int("j"), INT.define_int("r")

# Define the input and output variables using z3
i_pre = z3.Int('i_0')
i_post = z3.Int('i')
j_pre = z3.Int('j_0')
j_post = z3.Int('j')
r_pre = z3.Int('r_0')
r_post = z3.Int('r')

# Define the loop
loop = CFG.define_loop([[i > 0]], [
    (
        (i, i - 1),
        (j, j + 1),
    )
])

# Analyze the loop
spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

# Define the preconditions
preconditions = [r_pre > i_pre + j_pre]

# Define the postconditions
postconditions = [r_post > i_post + j_post]

# Check the postconditions after the loop
summarizer.check_after_loop(preconditions, {"i": i_post, "j": j_post, "r": r_post}, postconditions)
