from cfg import CFG
from int import INT
from pfg import PFG
from recurrence import PiecewiseSubDomain

"""
while (i < 100){ 
	if (x <= 5) 
		x++; 
	else 
	    if (x < 7)
	        x--;
	    else
	        x -= 3;
	    x += 2;
	    if (x > 9)
		    x −= 4; 
		else
		    x += 1;
	if (y < 8) 
		y++; 
	else 
		y −= 3;
	i++; 
}
"""


def input_loop(i, x, y):
    path = ""

    while i < 100:
        if x <= 5:
            x += 1
            path += "A"
        else:
            if x < 7:
                x -= 1
                path += "B"
            else:
                x -= 3
                path += "C"
            x += 2
            path += "D"
            if x > 9:
                x -= 4
                path += "E"
            else:
                x += 1
                path += "F"

        if y < 8:
            y += 1
            path += "G"
        else:
            y -= 3
            path += "H"

        i += 1

    return [i, x, y, path]


x, y, i = INT.define_int("x"), INT.define_int("y"), INT.define_int("i")

loop = CFG.define_loop([[i < 100]], [
    [
        ([[x <= 5]], [
            (
                (x, x + 1),
            )
        ]),
        ([[x > 5]], [
            [
                ([[x < 7]], [
                    (
                        (x, x - 1),
                    )
                ]),
                ([[x >= 7]], [
                    (
                        (x, x - 3),
                    )
                ])
            ],
            (
                (x, x + 2),
            ),
            (
                (x, x + 1),
            ),
            [
                ([[x > 9]], [
                    (
                        (x, x - 4),
                    )
                ]),
                ([[x <= 9]], [
                    (
                        (x, x + 1),
                    )
                ])
            ]
        ])
    ],
    [
        ([[y < 8]], [
            (
                (y, y + 1),
            )
        ]),
        ([[y >= 8]], [
            (
                (y, y - 3),
            )
        ]),
    ],
    (
        (i, i + 1),
    )
])

print(loop.to_dot())
print(loop.get_dominators(1, len(loop.nodes) - 1))
print(loop.get_dominators(3, 11))
pfg = PFG(loop)
print(len(pfg.paths))
for path in pfg.paths:
    print(path)
# for path_arc in pfg.path_arcs:
#     print(path_arc)
t = PiecewiseSubDomain(pfg.paths[2])
pass
