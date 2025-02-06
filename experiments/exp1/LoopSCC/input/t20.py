from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

var_map = {"x": x, "y": y}

loop1 = CFG.define_loop([[x < y]], [
    [
        ([[x == x]], [
            (
                (x, x + 1),
            )
        ]),
    ]
])

loop2 = CFG.define_loop([[y < x]], [
    [
        ([[y == y]], [
            (
                (y, y + 1),
            )
        ]),
    ]
])

spg = SPath_Graph(loop1)
summarizer = Summarizer(spg)
summarizer.summarize()

spg2 = SPath_Graph(loop2)
summarizer2 = Summarizer(spg2)
summarizer2.summarize()
tests = [
    [(x, 8034911), (y, -2115461), ],
    [(x, -590904), (y, -3785669), ],
    [(x, -7260342), (y, 3328147), ],
    [(x, 3412672), (y, 2428087), ],
    [(x, -2415475), (y, -6211944), ],
    [(x, -8100323), (y, -6213284), ],
    [(x, 2910629), (y, -2963133), ],
    [(x, -5426185), (y, 9372763), ],
    [(x, -4019892), (y, -85137), ],
    [(x, -646038), (y, -8500835), ],
    [(x, 7342193), (y, 2199279), ],
    [(x, -3034703), (y, 8675516), ],
    [(x, -7971011), (y, -3619011), ],
    [(x, -9155485), (y, 8359793), ],
    [(x, 3860330), (y, 3228797), ],
    [(x, 4950547), (y, 5884331), ],
    [(x, -7141346), (y, 2538409), ],
    [(x, -1113095), (y, -2014793), ],
    [(x, 2918755), (y, -8718130), ],
    [(x, 2593064), (y, -2251570), ],
    [(x, -3777536), (y, 4058245), ],
    [(x, -8190315), (y, 9402083), ],
    [(x, -9595404), (y, 5137615), ],
    [(x, 1615662), (y, -3177598), ],
    [(x, -8349771), (y, 1553808), ],
    [(x, -3149871), (y, 8281496), ],
    [(x, -2712581), (y, -7817215), ],
    [(x, -1055928), (y, -184387), ],
    [(x, -570420), (y, -7144860), ],
    [(x, -2155541), (y, -5310569), ],
    [(x, -34894), (y, 5346254), ],
    [(x, -8595985), (y, 1682601), ],
    [(x, 1848156), (y, -6553254), ],
    [(x, -3937237), (y, 3989312), ],
    [(x, 243540), (y, -928890), ],
    [(x, -649158), (y, -6196727), ],
    [(x, 2582392), (y, 4177536), ],
    [(x, -3993146), (y, -4030543), ],
    [(x, -277152), (y, -2049251), ],
    [(x, -871458), (y, -7644114), ],
    [(x, -2839534), (y, 5947392), ],
    [(x, -73392), (y, 4327458), ],
    [(x, -2507479), (y, 8745186), ],
    [(x, 931139), (y, -4875042), ],
    [(x, 9869992), (y, 177986), ],
    [(x, 1700833), (y, -6874404), ],
    [(x, -289944), (y, 6006610), ],
    [(x, -9750661), (y, -8163964), ],
    [(x, 7288789), (y, -7910258), ],
    [(x, -37336), (y, -8388749), ],
    [(x, 6348102), (y, 6393631), ],
    [(x, 7635969), (y, 7129095), ],
    [(x, 7122171), (y, -586052), ],
    [(x, 9751285), (y, 827724), ],
    [(x, 5074488), (y, 6057766), ],
    [(x, -4416889), (y, -3899297), ],
    [(x, 6552006), (y, -1966356), ],
    [(x, -9534178), (y, 73693), ],
    [(x, -3959802), (y, -5533071), ],
    [(x, -7707732), (y, 6070524), ],
    [(x, 9606359), (y, 9711938), ],
    [(x, 9689009), (y, 9943016), ],
    [(x, -5781384), (y, 2051678), ],
    [(x, -4659967), (y, -4935164), ],
    [(x, 4824145), (y, 773390), ],
    [(x, 6852072), (y, 6025709), ],
    [(x, -1457350), (y, -9450232), ],
    [(x, -9925432), (y, 6566777), ],
    [(x, -5457388), (y, 4424738), ],
    [(x, 4091836), (y, 5298843), ],
    [(x, -9667063), (y, 744024), ],
    [(x, 208107), (y, -7247264), ],
    [(x, 9860817), (y, -4969256), ],
    [(x, 8902585), (y, 9689040), ],
    [(x, 9487802), (y, -4743435), ],
    [(x, 4851158), (y, 9024423), ],
    [(x, -6277542), (y, 3438736), ],
    [(x, 1227828), (y, -3250067), ],
    [(x, -5808678), (y, 9423467), ],
    [(x, -2468859), (y, -8133558), ],
    [(x, -1342826), (y, 4435375), ],
    [(x, -7653477), (y, -7621315), ],
    [(x, 176801), (y, 383775), ],
    [(x, -6441457), (y, 7408087), ],
    [(x, 8667383), (y, -2635015), ],
    [(x, 5741473), (y, 6274732), ],
    [(x, -4738268), (y, 2275105), ],
    [(x, 9654241), (y, -3340466), ],
    [(x, -5387101), (y, 7690406), ],
    [(x, 4555269), (y, -6992794), ],
    [(x, 5191208), (y, 9022515), ],
    [(x, 1970890), (y, 9856548), ],
    [(x, -6252238), (y, 2774241), ],
    [(x, 9565251), (y, 740259), ],
    [(x, 2044445), (y, 4787223), ],
    [(x, 7456834), (y, 2196315), ],
    [(x, 3909513), (y, 165191), ],
    [(x, -6123317), (y, 8701490), ],
    [(x, 6562460), (y, 1135136), ],
    [(x, -1239987), (y, -4960638), ],
]
for test in tests:
    # res1 = List[tuple('symbol_name', 'symbol_var')]
    res1 = summarizer.solve(test)

    input2 = []
    for each in res1:
        input2.append((var_map[each[0]], each[1]))

    result = summarizer2.solve(input2)
    for symbol_val in result:
        print(f"{symbol_val[0]} = {symbol_val[1]}")
