from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

## Define Symbolic Variables
a = INT.define_int("a")

## Define Loop
loop = CFG.define_loop([[a < 0]], [
    (
        (a, a + 1),
    )
])

## Define Initial Value
test = [(a, 6)]

## Loop Analysis
pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

## Result Verification
result = summarizer.solve(test)
for symbol_val in result:
    if symbol_val[0] == "a":
        if int(symbol_val[1]) != 6:
            print("SUCCESS")
        else:
            print("FAILED")