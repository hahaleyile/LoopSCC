import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

i, n, sum = INT.define_int("i"), INT.define_int("n"), INT.define_int("sum")

loop = CFG.define_loop([[i < n]], [
    (
        (sum, sum + i),
        (i, i + 1),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

i_pre = z3.Int('i_0')
sum_pre = z3.Int('sum_0')
n_pre = z3.Int('n_0')
sum_post = z3.Int('sum')

summarizer.check_after_loop([i_pre == 0, n_pre >= 0, n_pre <= 100,sum_pre==0],
                            {"sum": sum_post},
                            [sum_post >= 0])