from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer
import z3

x, y = INT.define_int("x"), INT.define_int("y")
i = INT.define_int("i")
loop = CFG.define_loop([[i<x]], [
        [
            ([[x == 0]], [
                [
                    ([[y > 0]], [
                        (
                            (x, x + 1),
                        ),
                    ]),
                    ([[y <= 0]], [
                        (
                            (x, x - 1),
                        ),
                    ]),
                ],
            ]),
            ([[x>0]], [()]),
            ([[x<0]], [()]),
        ],
        [
            ([[x > 0]], [
                (
                    (y, y + 1),
                ),
            ]),
            ([[x <= 0]], [
                (
                    (x, x - 1),
                ),
            ]),
        ]
    ]
)

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

x_pre = z3.Int('x_0')
x_post = z3.Int('x')
y_pre = z3.Int('y_0')
y_post = z3.Int('y')

summarizer.check_after_loop([x_pre * y_pre >= 0], {"x": x_post, "y": y_post}, [x_post * y_post >= 0])
