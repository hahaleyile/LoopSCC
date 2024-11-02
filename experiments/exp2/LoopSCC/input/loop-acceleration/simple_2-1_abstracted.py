```python
from cfg import CFG
from int import INT
from pfg import PFG
from summarizer import Summarizer

x = INT.define_int("x")

loop = CFG.define_loop([[x < 268435455]], [
    [
        ([[x < 268435455]], [
            (x, "nondet")
        ])
    ]
])

pfg = PFG(loop)
summarizer = Summarizer(pfg)
summarizer.summarize()

x_pre = x
x_post = x
summarizer.check_after_loop([x_pre == 0], {"x": x_post}, [x_post >= 268435455])
```
