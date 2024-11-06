Here is the converted Python code based on the given C code:

```python
from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer
import z3

x, y = INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop(
    [[x < 100], [y < 100]],
    [
        [
            ([[x < 100], [y < 100]]),
            (
                (x, x + 1),
                (y, y + 1),
            )
        ]
    ]
)

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

# Define input and output variables
x_pre = z3.Int('x_0')
x_post = z3.Int('x')
y_pre = z3.Int('y_0')
y_post = z3.Int('y')

# Verify condition after loop
summarizer.check_after_loop([x_pre < 100, y_pre < 100], {"x": x_post, "y": y_post}, [z3.Or(x_post == 100, y_post == 100)])
```
