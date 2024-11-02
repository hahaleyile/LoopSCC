# can't handle
from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

i, n, k,t = INT.define_int("i"), INT.define_int("n"), INT.define_int("k"), INT.define_int("t")

loop = CFG.define_loop([[i < 2*k]], [
    [
        ([[i == 2*t]], [
            (
                (n, n + 1),
            )
        ]),
        ([[i != 2*t]], [
            (
            )
        ]),
    ],
    (
        (i, i + 1),
    )
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

import z3
k_pre = z3.Int('k_0')
k_post = z3.Int('k')
n_pre = z3.Int('n_0')
n_post = z3.Int('n')
i_pre = z3.Int('i_0')
i_post = z3.Int('i')
t_pre = z3.Int('t_0')
t_post = z3.Int('t')
summarizer.check_after_loop([i_pre == 0, k_pre>=-1000000,k_pre<=1000000,t_pre==i_pre/2],
                            {"k": k_post, "n": n_post, "i":i_post, "t":t_post},
                            [z3.Or(k<0, k==n)])
