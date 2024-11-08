from cfg import CFG
from int import INT
from spath_graph import SPath_Graph
from summarizer import Summarizer

x, y = INT.define_int("x"), INT.define_int("y")

loop = CFG.define_loop([[x < 100]], [
    [
        ([[y < 30]], [
            (
                (y, y + 1),
            )
        ]),
        ([[y >= 30]], [
            (
                (x, x + 1),
            )
        ]),
    ]
])

spg = SPath_Graph(loop)
summarizer = Summarizer(spg)
summarizer.summarize()
tests = [
    [(x, 8589517), (y, 6240715), ],
    [(x, 8321094), (y, 388181), ],
    [(x, -7632014), (y, -5770692), ],
    [(x, -8543193), (y, -7753988), ],
    [(x, 8548546), (y, -4238938), ],
    [(x, 6125316), (y, 3584156), ],
    [(x, 5484478), (y, -3921945), ],
    [(x, 7264303), (y, 739999), ],
    [(x, -8552869), (y, 2323771), ],
    [(x, -2448153), (y, -3378009), ],
    [(x, 4015789), (y, 6397145), ],
    [(x, -3331104), (y, -7057563), ],
    [(x, -8404005), (y, 8395511), ],
    [(x, -905590), (y, -196115), ],
    [(x, 9875940), (y, -7538256), ],
    [(x, -6859585), (y, 5755196), ],
    [(x, 8322169), (y, -4700794), ],
    [(x, 8766446), (y, 6663100), ],
    [(x, 8233733), (y, 6530964), ],
    [(x, -2417683), (y, 96500), ],
    [(x, 5004620), (y, 3074384), ],
    [(x, 1110171), (y, 8475289), ],
    [(x, 5853519), (y, 8856057), ],
    [(x, 8353795), (y, 7880208), ],
    [(x, 8862779), (y, 3514407), ],
    [(x, 7324036), (y, 9520288), ],
    [(x, 9923748), (y, -5282568), ],
    [(x, -9121473), (y, 6374785), ],
    [(x, -6239829), (y, 231682), ],
    [(x, -9482968), (y, 6672454), ],
    [(x, -7088169), (y, -4072633), ],
    [(x, -4210477), (y, -1842846), ],
    [(x, 7916486), (y, -4295184), ],
    [(x, 3194181), (y, 2669026), ],
    [(x, -8637909), (y, 1594005), ],
    [(x, 2057547), (y, 2861469), ],
    [(x, 3361716), (y, 3980286), ],
    [(x, -9093005), (y, -8910045), ],
    [(x, 4686155), (y, 3546328), ],
    [(x, 6458278), (y, 9765808), ],
    [(x, 4676843), (y, -8220673), ],
    [(x, 8679607), (y, 5113988), ],
    [(x, -9218261), (y, 5409101), ],
    [(x, -392285), (y, 5590782), ],
    [(x, 311425), (y, -6831242), ],
    [(x, -7340884), (y, 8139876), ],
    [(x, -4857571), (y, 7315093), ],
    [(x, 9586290), (y, 4978153), ],
    [(x, -9117149), (y, -8291409), ],
    [(x, -129379), (y, 1875793), ],
    [(x, -4224499), (y, 1576594), ],
    [(x, 5556148), (y, -5586670), ],
    [(x, -9403584), (y, -8412832), ],
    [(x, 2530073), (y, 6131167), ],
    [(x, 2043991), (y, 5384372), ],
    [(x, -2949506), (y, 6427776), ],
    [(x, -2674806), (y, -4539114), ],
    [(x, -6461878), (y, -517941), ],
    [(x, 1399716), (y, -9757496), ],
    [(x, 2071121), (y, 6620364), ],
    [(x, 5672144), (y, -8331166), ],
    [(x, 3443390), (y, -8936930), ],
    [(x, 6142894), (y, 6321964), ],
    [(x, -4617161), (y, -1297299), ],
    [(x, -5697317), (y, -9865275), ],
    [(x, -476458), (y, -1286063), ],
    [(x, -1897614), (y, -159992), ],
    [(x, 4391216), (y, 6881352), ],
    [(x, 1849853), (y, -1755706), ],
    [(x, 3289877), (y, 1014900), ],
    [(x, 9805537), (y, -8658933), ],
    [(x, 7877922), (y, -217866), ],
    [(x, -1357001), (y, -5102835), ],
    [(x, -3413523), (y, -9655678), ],
    [(x, 9968369), (y, -3131134), ],
    [(x, -358644), (y, 6376720), ],
    [(x, -4071410), (y, -802334), ],
    [(x, 8696734), (y, 9192303), ],
    [(x, 362952), (y, -9973039), ],
    [(x, 7682402), (y, 9692739), ],
    [(x, 5153615), (y, -7594354), ],
    [(x, 7795065), (y, -565763), ],
    [(x, -2058628), (y, 5086388), ],
    [(x, 4394749), (y, 7635797), ],
    [(x, -2210429), (y, 7202189), ],
    [(x, 1527574), (y, 2054843), ],
    [(x, 1900369), (y, -7431692), ],
    [(x, 3120357), (y, -790390), ],
    [(x, -45842), (y, 2829701), ],
    [(x, -5466202), (y, 6654534), ],
    [(x, -575103), (y, 3912214), ],
    [(x, 2039879), (y, 3785408), ],
    [(x, 8765610), (y, 293330), ],
    [(x, -1560947), (y, -4026106), ],
    [(x, -2638356), (y, 7655811), ],
    [(x, -4260438), (y, 8028523), ],
    [(x, 3201125), (y, 9900080), ],
    [(x, -9111751), (y, 6233374), ],
    [(x, -485204), (y, 3862323), ],
    [(x, -5367272), (y, -7397124), ],
]
for test in tests:
    result = summarizer.solve(test)
    for symbol_val in result:
        print(f"{symbol_val[0]} = {symbol_val[1]}")
