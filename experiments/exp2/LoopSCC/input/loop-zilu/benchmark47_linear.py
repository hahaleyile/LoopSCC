from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop([[x < y]], [
    [
        ([[x < 0]], [
            (
                (x, x + 7),
            )
        ]),
        ([[x >= 0]], [
            (
                (x, x + 10),
            )
        ]),
    ],
    [
        ([[y < 0]], [
            (
                (y, y - 10),
            )
        ]),
        ([[y >= 0]], [
            (
                (y, y + 3),
            )
        ]),
    ]
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

import z3
x_pre = z3.Int('x_0')
x_post = z3.Int('x')
y_pre = z3.Int('y_0')
y_post = z3.Int('y')

summarizer.check_after_loop([y_pre > x_pre], {"x": x_post, "y": y_post}, [x_post >= y_post, x_post <= y_post + 16])
