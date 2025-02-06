from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

# k=x-y
x, y, t, k = INT.define_int("x"), INT.define_int("y"), INT.define_int("t"), INT.define_int("k")

loop = CFG.define_loop([[t > 0]], [
    [
        ([[k == 1]], [
            (
                (k, k - 2),
                (y, y + 2),
            )
        ]),
        ([[k != 1]], [
            (
                (k, k + 2),
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
    [(t, 56600), (x, 12262), (y, -41371)],
]
for test in tests:
    x_val = 0
    y_val = 0
    t_val = 0
    for symbol_val in test:
        if symbol_val[0].symbols[0].name == "x":
            x_val = symbol_val[1]
        if symbol_val[0].symbols[0].name == "y":
            y_val = symbol_val[1]
        if symbol_val[0].symbols[0].name == "t":
            t_val = symbol_val[1]
    temp = [(t, t_val), (k, x_val - y_val), (y, y_val)]
    result = summarizer.solve(temp)
    k_val = 0
    for symbol_val in result:
        if symbol_val[0] == "x":
            y_val = symbol_val[1]
            print(f"y = {y_val}")
        elif symbol_val[0] == "k":
            k_val = symbol_val[1]
        else:
            print(f"{symbol_val[0]} = {symbol_val[1]}")
    x_val = int(y_val) + int(k_val)
    print(f"x = {x_val}")
