from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

"""
while (i < 100){ 
	if (x <= 5) 
	    i++
		x+=3
	else if (x > 5 && x <= 10)
	    i+=3
	    x+=2
	else
	    i+=2
		x−=5
}
"""

x, i = INT.define_int("x"), INT.define_int("i")

loop = CFG.define_loop([[i < 100]], [
    [
        ([[x <= 5]], [
            (
                # lvalue, rvalue
                (x, x + 3),
                (i, i + 1),
            )
        ]),
        ([[x > 5, x <= 10]], [
            (
                (x, x + 2),
                (i, i + 3),
            )
        ]),
        ([[x > 10]], [
            (
                (x, x - 5),
                (i, i + 2),
            )
        ]),
    ]
])

print(loop.to_dot())
print(loop.get_dominators(1, len(loop.nodes) - 1))
spg = SPath_Graph(loop)
print(len(spg.paths))
for path in spg.paths:
    print(path)
print(spg.to_dot())
summarizer = Summarizer(spg)
summarizer.summarize()
tests = [
    [(x, 100), (i, 90)],
    [(x, 93), (i, 89)],
    [(x, 93), (i, 69)],
    [(x, 16), (i, 89)],
    [(x, 16), (i, 69)],
    [(x, 12), (i, 89)],
]
for test in tests:
    result = summarizer.solve(test)
    for symbol_val in result:
        print(f"{symbol_val[0]} = {symbol_val[1]}")
print("")
for test in tests:
    x = test[0][1]
    i = test[1][1]
    while i < 100:
        if x <= 5:
            x += 3
            i += 1
        elif x > 5 and x <= 10:
            x += 2
            i += 3
        else:
            x -= 5
            i += 2
    print(f"x = {x}")
    print(f"i = {i}")

