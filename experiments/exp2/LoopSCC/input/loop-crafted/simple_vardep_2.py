from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

i, j, k = INT.define_int("i"), INT.define_int("j"), INT.define_int("k")

loop = CFG.define_loop([[k < 0x0fffffff]], [
    (
        (i, i + 1),
        (j, j + 2),
        (k, k + 3),
    )
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

result = summarizer.solve([(i,0),(j,0),(k,0)])
i_val, j_val, k_val = 0,0,0
print(result)
for symbol_val in result:
    
    if symbol_val[0] == "i":
        i_val = int(symbol_val[1])
    if symbol_val[0] == "j":
        j_val = int(symbol_val[1])
    if symbol_val[0] == "k":
        k_val = int(symbol_val[1])
if k_val == 3*i_val and j_val==2*i_val:
    print("SUCCESS")
else:
    print("FAILED")