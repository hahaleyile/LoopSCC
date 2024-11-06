```python
from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x = INT.define_int("x")

loop = CFG.define_loop([[x < 268435455]], [
    [
        ([[x < 268435455]], [
            (x, "nondet")
        ])
    ]
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

x_pre = x
x_post = x
summarizer.check_after_loop([x_pre == 0], {"x": x_post}, [x_post >= 268435455])
```
