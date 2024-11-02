from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

"""
while (i < 100){ 
	i=100
	x+=3
}
"""

x, i = INT.define_int("x"), INT.define_int("i")

loop = CFG.define_loop([[i < 100]], [
    (
        (i, 100),
        (x, x + 3),
    )
])

print(loop.to_dot())
print(loop.get_dominators(1, len(loop.nodes) - 1))
pfg = PFG(loop)
print(len(pfg.paths))
for path in pfg.paths:
    print(path)
print(pfg.to_dot())
summarizer = Summarizer(pfg)
for scc in summarizer.pfg.scc:
    summarizer.scc_summarize(scc)
