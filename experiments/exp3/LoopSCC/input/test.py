from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x0, x1, i = INT.define_int("x0"), INT.define_int("x1"), INT.define_int("i")

loop = CFG.define_loop([[i < 100]], [
    [
        ([[x0 > 5]], [
            (
                (x0, x0 - 1),
                (i, i + 3),
            )
        ]),
        ([[x0 <= 5]], [
            (
                (x0, x0 + 1),
                (i, i + 7),
            )
        ]),
    ],
    [
        ([[x1 > 0]], [
            (
                (x1, x1 + 3),
                (i, i + 2),
            )
        ]),
        ([[x1 <= 0]], [
            (
                (x1, x1 - 2),
                (i, i + 3),
            )
        ]),
    ],
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()
print(len(summarizer))
