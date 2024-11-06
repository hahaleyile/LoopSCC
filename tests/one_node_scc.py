from cfg import CFG
from int import INT

from spath_graph import SPath_Graph
from summarizer import Summarizer

x, i = INT.define_int("x"), INT.define_int("i")

loop = CFG.define_loop([[i < 100000000]], [
    [
        ([[x <= 5]], [
            (
                # lvalue, rvalue
                (x, x + 2),
                (i, i + 3),
            )
        ]),
        ([[x > 5]], [
            (
                (x, x + 3),
                (i, i + 2),
            )
        ]),
    ]
])

print(loop.to_dot())
print(loop.get_dominators(1, len(loop.nodes) - 1))
spg = SPath_Graph(loop)
print(len(spg.paths))
print(spg.to_dot())
summarizer = Summarizer(spg)
summarizer.summarize()
tests = [
    [(x, 1), (i, 0)],
    [(x, 7), (i, 3)],
    [(x, -100000), (i, 0)],
    [(x, -7), (i, 3)],
]
for test in tests:
    result = summarizer.solve(test)
    for symbol_val in result:
        print(f"{symbol_val[0]} = {symbol_val[1]}")
print("")
for test in tests:
    x = test[0][1]
    i = test[1][1]
    while i < 100000000:
        if x <= 5:
            x += 2
            i += 3
        else:
            x += 3
            i += 2
    print(f"x = {x}")
    print(f"i = {i}")
