```python
from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x = INT.define_int("x")

# Define loop condition and body as a whole
loop = CFG.define_loop([[x < 268435455]], [
    [
        ([[True]], [
            (
                (x, x + 2),
            )
        ]),
    ]
])

# Analyze the loop
pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

# Define initial values
test = [(x, 0)]

# Solve results
result = summarizer.solve(test)
for symbol_val in result:
    if symbol_val[0] == "x":
        if int(symbol_val[1]) % 2 == 1:
            **print**("SUCCESS")
        else:
            **print**("FAILED")
```
