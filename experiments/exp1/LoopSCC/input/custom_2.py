from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x, i = INT.define_int("x"), INT.define_int("i")

loop = CFG.define_loop([[i < 100]], [
    [
        ([[x > 5]], [
            (
                (x, x - 5),
                (i, i + 3),
            )
        ]),
        ([[x < -5]], [
            (
                (x, x + 3),
                (i, i + 5),
            )
        ]),
        ([[x >= -5, x <= 5]], [
            (
                (x, x + 2),
                (i, i + 7),
            )
        ]),
    ]
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()
tests = [
    [(i, -4792848), (x, -45974), ],
    [(i, -6895048), (x, -1782595), ],
]
for test in tests:
    result = summarizer.solve(test)
    for symbol_val in result:
        print(f"{symbol_val[0]} = {symbol_val[1]}")
