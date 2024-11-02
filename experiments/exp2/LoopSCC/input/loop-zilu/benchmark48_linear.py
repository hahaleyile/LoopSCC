from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer
import z3

# Define symbolic variables
i, j, k = INT.define_int("i"), INT.define_int("j"), INT.define_int("k")

# Define input and output variables using z3
i_pre = z3.Int('i_0')
i_post = z3.Int('i')
j_pre = z3.Int('j_0')
j_post = z3.Int('j')
k_pre = z3.Int('k_0')
k_post = z3.Int('k')

# Loop definition
loop = CFG.define_loop([[i < j]],[
        (
            (k, k + 1),
            (i, i + 1),
        )
    ]
)

# Loop analysis
pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

# Result verification (Type 1: Non-deterministic Variables)
summarizer.check_after_loop(
    [i_pre < j_pre, k_pre > 0],
    {"i": i_post, "j": j_post, "k": k_post},
    [k_post > j_post - i_post]
)
