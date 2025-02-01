from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, y, t, flag = INT.define_int("x"), INT.define_int("y"), INT.define_int("t"), INT.define_int(
    "flag")

loop = CFG.define_loop([[t > 0]], [
    [
        ([[flag == 1]], [
            (
                (x, x + 1),
                (flag, -1)
            )
        ]),
        ([[flag != 1]], [
            (
                (y, y + 1),
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
    [(flag, 1), (t, 100), (x, 0), (y, 20)],
]
for test in tests:
    result = summarizer.solve(test)
    for symbol_val in result:
        print(f"{symbol_val[0]} = {symbol_val[1]}")
