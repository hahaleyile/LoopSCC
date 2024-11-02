from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer
import z3

n,m = INT.define_int("n"), INT.define_int("m")
k = INT.define_int("k")
i = INT.define_int("i")
j = INT.define_int("j")


loop = CFG.define_loop([[i < n]], [
    (
        (j,0),
    ),
    [
        ([[j < m]], [
            (
                (k, k+m),
                (j, m),
            )
        ]),
        ([[j >= m]], [
            (
  
            )
        ])
    ]
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)

i_pre = z3.Int('i_0')
i_post = z3.Int('i')
n_pre = z3.Int('n_0')
n_post = z3.Int('n')
m_pre = z3.Int('m_0')
m_post = z3.Int('m')
k_pre = z3.Int('k_0')
k_post = z3.Int('k')
summarizer.check_after_loop([n_pre >= 10, n_pre <= 10000, m_pre >= 10, m_pre <= 10000, i_pre == 0, k_pre==0],
                              {"n": n_post, "m": m_post, "k": k_post},
                              [k_post >= 100])