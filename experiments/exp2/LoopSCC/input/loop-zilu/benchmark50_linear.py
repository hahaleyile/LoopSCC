from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

xa, ya = INT.define_int("xa"), INT.define_int("ya")

loop = CFG.define_loop([[xa > 0]], [
    (
        (xa, xa - 1),
        (ya, ya + 1),
    )
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()

# Result verification
import z3
xa_pre = z3.Int('xa_0')
xa_post = z3.Int('xa')
ya_pre = z3.Int('ya_0')
ya_post = z3.Int('ya')
summarizer.check_after_loop([xa_pre + ya_pre > 0], {"xa": xa_post, "ya": ya_post}, [ya_post >= 0])
