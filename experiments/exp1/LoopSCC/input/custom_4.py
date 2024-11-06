from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, i = INT.define_int("x"), INT.define_int("i")

loop = CFG.define_loop([[i < 100]], [
    [
        ([[x > 5]], [
            (
                (x, x - 2),
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

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()
tests = [
    [(i, -6422128), (x, -2616176), ],
    [(i, -9514962), (x, 5566229), ],
]
for test in tests:
    result = summarizer.solve(test)
    for symbol_val in result:
        print(f"{symbol_val[0]} = {symbol_val[1]}")
