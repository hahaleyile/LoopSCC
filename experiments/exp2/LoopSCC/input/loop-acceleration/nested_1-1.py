from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

outer_loop = CFG.define_loop([[x < 0x0fffffff]], [
    (
        (y, 0),
    ),
    [
        ([[y<10]], [
            (
                (y,10),
            )
        ]),
        ([[y>=10]], [
            (
                
            )
        ]),
    ],
    (
        (x, x + 1),
    ),
])

spg = SPath_Graph(outer_loop)
summarizer = Summarizer(spg)
summarizer.summarize()

x_pre = INT.define_int('x')
y_pre = INT.define_int('y')
x_post = INT.define_int('x')
y_post = INT.define_int('y')
result = summarizer.solve([(x, 0), (y, 0)])
for symbol_val in result:
    if symbol_val[0] == "x":
        if int(symbol_val[1]) % 2 != 0:
            print("SUCCESS")
        else:
            print("FAILED")
