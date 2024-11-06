from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer
import z3

# Define symbolic variables
a, b = INT.define_int("a"), INT.define_int("b")
c, d = INT.define_int("c"), INT.define_int("d")
e, f = INT.define_int("e"), INT.define_int("f")
# Loop definition
loop = CFG.define_loop([[a < 6]], [
    (
        (b,0),
    ),
    [
        ([[b<6]],[
            (
                (c,0),
            ),
            [
                ([[c<6]],[
                    (
                        (d,0),
                    ),
                    [
                        ([[d<6]],[
                            (
                                (e,0),
                            ),
                            [
                                ([[e<6]],[
                                    (
                                        (f,6),
                                    ),
                                    [
                                        ([[f<6]], [
                                            (
                                                (f,6),
                                            )
                                        ]),
                                        ([[f>=6]], [
                                            (
                                                
                                            )
                                        ]),
                                    ],
                                    (
                                        (e,6),
                                    )
                                ]),
                                ([[e>=6]],[
                                    (
                                        
                                    )
                                ]),  
                            ],
                            (
                                (d,6),
                            )
                        ]),
                        ([[d>=6]],[
                            (
                                
                            )
                        ]),
                    ],
                    (
                        (c, 6),
                    )
                ]),
                ([[c>=6]],[
                    (
                        
                    )
                ])
            ],
            (
                (b,6),
            )
        ]),
        ([[b>=6]],[
            (
                
            )
        ])
    ],
    (
        (a, a+1),
    )
])


# Loop analysis
spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

result = summarizer.solve([(a, 0), (b, 6),(c, 6),(d,6),(e,6),(f,6)])
a_val, b_val, c_val,d_val = 0,0,0,0
e_val, f_val = 0,0
for symbol_val in result:
    if symbol_val[0] == "a":
        a_val = int(symbol_val[1])
    elif symbol_val[0] == "b":
        b_val = int(symbol_val[1])
    elif symbol_val[0] == "c":
        c_val = int(symbol_val[1])
    elif symbol_val[0] == "d":
        d_val = int(symbol_val[1])
    elif symbol_val[0] == "e":
        e_val = int(symbol_val[1])
    elif symbol_val[0] == "f":
        f_val = int(symbol_val[1])

if a_val==6 and b_val==6 and c_val==6 and d_val==6 and e_val==6 and f_val==6:
    print("SUCCESS")
else:
    print("FAILED")
