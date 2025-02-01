from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

b, c, t, flag = INT.define_int("b"), INT.define_int("c"), INT.define_int("t"), INT.define_int(
    "flag")

loop = CFG.define_loop([[t > 0]], [
    [
        ([[flag == 1]], [
            (
                (b, b + 1),
                (c, c - 1),
                (flag, -1)
            )
        ]),
        ([[flag != 1]], [
            (
                (b, b + 1),
                (c, c + 1),
                (flag, 1)
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
    [(flag, 1), (t, 100), (b, 0), (c, 20)],
]
for test in tests:
    result = summarizer.solve(test)
    for symbol_val in result:
        print(f"{symbol_val[0]} = {symbol_val[1]}")
