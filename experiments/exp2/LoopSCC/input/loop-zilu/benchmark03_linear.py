import z3

from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x, y, i, j, a, b, flag = (INT.define_int("x"), INT.define_int("y"), INT.define_int("i"), INT.define_int("j"),
                          INT.define_int("a"), INT.define_int("b"), INT.define_int("flag"))

loop = CFG.define_loop([[a < b]], [
    (
        (x, x + 1),
        (y, y + 1),
        (i, i + x),
        (j, j + y),
    ),
    [
        ([[flag != 0]], [
            (
                (j, j + 1),
            )
        ]),
        ([[flag == 0]], [
            ()
        ]),
    ],
    (
        (a, a + 1),
    ),
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

x_pre = z3.Int('x_0')
y_pre = z3.Int('y_0')
i_pre = z3.Int('i_0')
j_pre = z3.Int('j_0')
i_post = z3.Int('i')
j_post = z3.Int('j')

summarizer.check_after_loop([x_pre == 0, y_pre == 0, i_pre == 0, j_pre == 0],
                            {"i": i_post, "j": j_post},
                            [j_post >= i_post])
