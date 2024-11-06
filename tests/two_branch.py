from cfg import CFG
from int import INT
from spath_graph import SPath_Graph

"""
while (i < 100){ 
    x+=2
	if (x <= 5) 
	    i++
		x+=3
	else 
	    i+=2
		x−=4 
}
"""


def input_loop(i, x):
    path = ""

    while i < 100:
        x += 2
        if x <= 5:
            i += 1
            x += 3
            path += "A"
        else:
            i += 2
            x -= 4
            path += "B"

    return [i, x, path]


x, i = INT.define_int("x"), INT.define_int("i")

loop = CFG.define_loop([[i < 100]], [
    (
        (x, x + 2),
    ),
    [
        ([[x <= 5]], [
            (
                # lvalue, rvalue
                (x, x + 3),
                (x, x + 2),
            )
        ]),
        ([[x > 5]], [
            (
                (x, x - 4),
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
