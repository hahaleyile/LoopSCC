import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x, i, k = INT.define_int("x"), INT.define_int("i"), INT.define_int("k")

loop = CFG.define_loop([[i < k]], [
    [
        ([[x == 1]], [
            (
                (x, 2),
            )
        ]),
        ([[x == 2]], [
            (
                (x, 1),
            )
        ]),
        ([[x != 1, x != 2]], [
            ()
        ]),
    ],
    (
        (i, i + 1),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

x_pre = z3.Int('x_0')
x_post = z3.Int('x')

summarizer.check_after_loop([z3.Or(x_pre == 1, x_pre == 2)],
                            {"x": x_post},
                            [x_post <= 8])
