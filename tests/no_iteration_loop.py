from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
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
spg = SPath_Graph(loop)
print(len(spg.paths))
for path in spg.paths:
    print(path)
print(spg.to_dot())
summarizer = Summarizer(spg)
for scc in summarizer.spg.scc:
    summarizer.scc_summarize(scc)
