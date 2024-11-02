# can't handle
from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer
import z3

a,b = INT.define_int("a"), INT.define_int("b")
c = INT.define_int("c")
d = INT.define_int("d")
e = INT.define_int("e")


loop = CFG.define_loop([[a<0xffffffff]], [
    [
        ([[b < 0xffffffff]], [
            ([[c < 0xffffffff]], [
                ([[d < 0xffffffff]], [
                    ([[e < 0xffffffff]], [
                        (
                            (e,e+1),
                        )
                    ]),
                    ([[e >= 0xffffffff]], [
                        ()
                    ])
                    (
                        (d,d+1),
                    )
                ]),
                ([[d >= 0xffffffff]], [
                    ()
                ])
                (
                    (c,c+1),
                )
            ]),
            ([[c >= 0xffffffff]], [
                ()
            ])
            (
                (b,b+1),
            )
        ]),
        ([[b >= 0xffffffff]], [
            ()
        ])
    ],
    (
        (a, a+1)
    )
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)

a_pre = z3.Int('a_0')
a_post = z3.Int('a')
b_pre = z3.Int('b_0')
b_post = z3.Int('b')
c_pre = z3.Int('c_0')
c_post = z3.Int('c')
d_pre = z3.Int('d_0')
d_post = z3.Int('d')
e_pre = z3.Int('e_0')
e_post = z3.Int('e')
summarizer.check_after_loop([n_pre >= 10, n_pre <= 10000, m_pre >= 10, m_pre <= 10000, i_pre == 0, k_pre==0],
                              {"n": n_post, "m": m_post, "k": k_post},
                              [k_post >= 100])