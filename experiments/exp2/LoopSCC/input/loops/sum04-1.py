import z3

from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

i, SIZE, sn, a = INT.define_int("i"), INT.define_int("SIZE"), INT.define_int("sn"), INT.define_int("a")

loop = CFG.define_loop([[i <= SIZE]], [
    [
        ([[i < 4]], [
            (
                (sn, sn + a),
            )
        ]),
        ([[i >= 4]], [
            ()
        ]),
    ],
    (
        (i, i + 1),
    ),
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()
i_pre = z3.Int('i_0')
sn_pre = z3.Int('sn_0')
sn_post = z3.Int('sn')
SIZE_post = z3.Int('SIZE')
a_post = z3.Int('a')
summarizer.check_after_loop([i_pre == 1, sn_pre == 0, z3.Int("a_0") == z3.Int("a_1")],
                            {"sn": sn_post, "SIZE": SIZE_post, "a": a_post},
                            [z3.Or(sn_post == SIZE_post * a_post, sn_post == 0)])
