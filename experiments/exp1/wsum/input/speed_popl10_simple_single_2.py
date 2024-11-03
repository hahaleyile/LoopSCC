from compare import compare
from wsummarizer import WSummarizer as ws


def input_loop(x0, y0):
    path = ""
    x = x0
    y = y0

    while True:
        if x < 100:
            x = x + 1
            y = y + 1
            path += "A"
        elif y < 30:
            x = x + 1
            y = y + 1
            path += "B"
        else:
            break
    return [x, y, path]


# 创建符号变量
x, y = ws.create_variables(2)

# 定义循环条件和分支
loop = ws.define_loop([[x < 100], [y < 30]], [
    ([x < 100], [
        [1, 0, 1],  # x=x+1
        [0, 1, 1],  # y=y+1
    ]),
    ([x >= 100, y < 30], [
        [1, 0, 1],  # x=x+1
        [0, 1, 1],  # y=y+1
    ]),
])

# 包含所有初始值的列表
all_initial_values = [
    [-90235543, -1275755210, ],
    [-930811417, 1235823324, ],
    [-2071058890, 2040448598, ],
    [1211525363, 1453143795, ],
    [-846827040, -1008866486, ],
    [-1600632928, 1842011476, ],
    [945894399, 29670356, ],
    [-326681878, 1118330599, ],
    [1893424091, 500468007, ],
    [-438369960, -1493408634, ],
    [-341317242, 234735961, ],
    [-375390631, 1606760866, ],
    [592514229, 677139854, ],
    [66151671, -1389687278, ],
    [-471257342, 1846764048, ],
    [-1373652346, -447165138, ],
    [1021759666, 670906769, ],
    [-880330732, -595897610, ],
    [900871973, -1400837667, ],
    [480233449, 1885585423, ],
    [714623399, -1727442559, ],
    [700680143, -75897185, ],
    [1376092288, 1588123942, ],
    [1431440489, -1575739351, ],
    [-318793333, -1255217189, ],
    [-1207604354, 600122211, ],
    [1684988583, 302987176, ],
    [2140714476, 506782396, ],
    [-1336105942, 1820104, ],
    [2009954006, 1839007818, ],
    [344670731, -1359162086, ],
    [1156883684, -359242913, ],
    [-1948243802, -1119887985, ],
    [1483703796, 561740790, ],
    [-2038081135, -513411628, ],
    [1230267950, 2098143179, ],
    [93274394, -859655844, ],
    [2072357154, 277482706, ],
    [463305861, 309985656, ],
    [-758704847, 1581762069, ],
    [-797266774, 1448086273, ],
    [1709905355, 1258924974, ],
    [419167362, -1463035885, ],
    [-1660818339, 1947266928, ],
    [1214719436, -283863831, ],
    [-49464104, -866845670, ],
    [594639404, -1134257091, ],
    [46373654, -1519579679, ],
    [-1667573828, 1253908557, ],
    [-1181628728, -185490423, ],
    [-652657251, -1577448517, ],
    [253142452, -2747983, ],
    [338658572, -1282771379, ],
    [1714639275, -1569289995, ],
    [-296656924, -834732854, ],
    [538223579, -1489575212, ],
    [-218694094, -1122731035, ],
    [-581705223, 2046817823, ],
    [-43522971, -1512820262, ],
    [1501034631, 1039927644, ],
    [2086886898, -1596435730, ],
    [-248064695, 1386722866, ],
    [1097113552, 657663704, ],
    [-1262847377, -1826260881, ],
    [-254344778, 1210805619, ],
    [-1123914739, 1456593804, ],
    [-2066476903, 1971875901, ],
    [1085071903, 866797088, ],
    [-1263715090, 1105463455, ],
    [1372056124, 941403306, ],
    [1260151174, 2031719188, ],
    [625690084, 759317215, ],
    [-1303293689, 1409870278, ],
    [-1763694748, -862733841, ],
    [-638373585, -173212737, ],
    [1336247206, 1408017565, ],
    [40695992, -465248888, ],
    [698500923, 1716090686, ],
    [601062006, 1855530206, ],
    [-246361274, -831937762, ],
    [-662891558, 840353671, ],
    [-1463715905, -859049502, ],
    [1156633910, -1922526543, ],
    [599664241, -441232328, ],
    [1412568157, -1781326804, ],
    [1205569543, 2111895598, ],
    [1498574047, -3954948, ],
    [1782966642, 617306385, ],
    [-1597154699, 2076890698, ],
    [-942579888, -1863516937, ],
    [1003364491, -1201613210, ],
    [560313964, -1782787942, ],
    [-262080835, -1382648566, ],
    [1043262301, 425186447, ],
    [-1543181133, -573099275, ],
    [770387973, 1376549938, ],
    [457407839, 115260403, ],
    [1279515913, -1832799523, ],
    [-1498965165, 2085987764, ],
    [-860091667, -1472097130, ],
]

loop.summarize()

print("RESULT BELOW:")
for initial_values in all_initial_values:
    terminal_values = loop.compute_terminal_values(*initial_values)
    output_str = ''
    for each in terminal_values:
        output_str += f'{each} '
    print(output_str)