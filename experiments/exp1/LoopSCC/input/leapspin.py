from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

d, t =  INT.define_int("d"), INT.define_int("t")

loop = CFG.define_loop([[t > 0]], [
    [
        ([[d == 1]], [
            (
                (d, d - 2),
            )
        ]),
        ([[d == -1]], [
            (
                (d, d + 2),
            )
        ]),
    ],
    (
        (t, t - 1),
    ),
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

tests = [
    [(d, 1), (t, 100)],
]
for test in tests:
    result = summarizer.solve(test)
    for symbol_val in result:
        print(f"{symbol_val[0]} = {symbol_val[1]}")
