from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, i, flag = INT.define_int("x"), INT.define_int("i"), INT.define_int("flag")

loop = CFG.define_loop([[i < 100]], [
    [
        ([[flag != 0]], [
            [
                ([[x > 5]], [
                    (
                        (x, x - 5),
                        (i, i + 3),
                    )
                ]),
                ([[x <= 5]], [
                    (
                        (x, x + 2),
                        (i, i + 7),
                    )
                ]),
            ],
        ]),
        ([[flag == 0]], [
            (
                (x, x - 7),
                (flag, 1),
            )
        ]),
    ]
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()
tests = [
    [(x, 0), (i, 0), ],
    [(x, 1), (i, 0), ],
    [(x, 2), (i, 0), ],
    [(x, 3), (i, 0), ],
    [(x, -1), (i, 0), ],
    [(x, -2), (i, 0), ],
    [(x, -3), (i, 0), ],
    [(x, 4), (i, 0), ],
    [(x, -4), (i, 0), ],
    [(x, 5), (i, 0), ],
    [(x, -5), (i, 0), ],
    [(x, 6), (i, 0), ],
    [(x, -6), (i, 0), ],
    [(x, 7), (i, 0), ],
    [(x, -7), (i, 0), ],
    [(x, 8), (i, 0), ],
    [(x, -8), (i, 0), ],
    [(x, 9), (i, 0), ],
    [(x, -9), (i, 0), ],
    [(x, 10), (i, 0), ],
    [(x, -10), (i, 0), ],
    [(x, 11), (i, 0), ],
    [(x, -11), (i, 0), ],
    [(x, 12), (i, 0), ],
    [(x, -12), (i, 0), ],
    [(x, 13), (i, 0), ],
    [(x, -13), (i, 0), ],
    [(x, 14), (i, 0), ],
    [(x, -14), (i, 0), ],
    [(x, 15), (i, 0), ],
    [(x, -15), (i, 0), ],
    [(x, 16), (i, 0), ],
    [(x, -16), (i, 0), ],
    [(x, 17), (i, 0), ],
    [(x, -17), (i, 0), ],
]
for test in tests:
    test.append((flag, 0))
    result = summarizer.solve(test)
    for symbol_val in result:
        print(f"{symbol_val[0]} = {symbol_val[1]}")
