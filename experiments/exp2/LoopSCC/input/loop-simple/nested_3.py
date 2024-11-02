from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer
import z3

# Define symbolic variables
a, b = INT.define_int("a"), INT.define_int("b")
c = INT.define_int("c")

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
pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

result = summarizer.solve([(a, 0), (b, 6),(c, 6)])
a_val, b_val, c_val = 0,0,0
for symbol_val in result:
    if symbol_val[0] == "a":
        a_val = int(symbol_val[1])
    elif symbol_val[0] == "b":
        b_val = int(symbol_val[1])
    elif symbol_val[0] == "c":
        c_val = int(symbol_val[1])

if a_val==6 and b_val==6 and c_val==6:
    print("SUCCESS")
else:
    print("FAILED")
