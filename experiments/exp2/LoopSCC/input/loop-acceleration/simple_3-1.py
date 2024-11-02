from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer
import z3

x = INT.define_int("x")
N = INT.define_int("N")

loop = CFG.define_loop([[x < N]], [
        (
            (x, x + 2),
        ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

N_pre = z3.Int('N_0')
N_post = z3.Int('N')
x_pre = z3.Int('x_0')
x_post = z3.Int('x')

summarizer.check_after_loop([x_pre==0], {"N": N_post, "x": x_post}, [x_post % 2 != 0])