from compare import compare
from wsummarizer import WSummarizer as ws


t, x, y, flag = ws.create_variables(4)

loop = ws.define_loop([t>0], [
    (flag == 1, [
        [1,0,0,0,-1], # t=t-1
        [0,1,0,0,1], # x=x+1
        [0,0,1,0,0], # y=y
        [0,0,0,0,-1], # flag =-1
    ]),
    (flag != 1, [
        [1,0,0,0,-1], # t=t-1
        [0,1,0,0,0], # x=x
        [0,0,1,0,1], # y=y+1
        [0,0,0,0,1], # flag =1
    ]),
])

all_initial_values = [
    [-13322, -14673, -58970, 1, ],
    [-73250, 11489, 76018, 1, ],
    [-40485, 9725, -76435, 1, ],
    [49882, -77945, -31918, 1, ],
    [-61418, 7059, -18977, 1, ],
    [-38443, 60559, 16589, 1, ],
    [-24745, 79192, 43220, 1, ],
    [66328, 31528, 18130, 1, ],
    [42005, -12332, -88315, 1, ],
    [66910, -42882, 50575, 1, ],
    [-56573, -82279, -9666, 1, ],
    [155, -59776, 30174, 1, ],
    [28605, 85843, -29416, 1, ],
    [77164, 62776, 28950, 1, ],
    [-85967, 4335, 49609, 1, ],
    [-70620, -75278, 74985, 1, ],
    [-40114, -36279, -97358, 1, ],
    [10349, -97371, 14340, 1, ],
    [-63289, 98627, -20410, 1, ],
    [-72572, -4576, -81816, 1, ],
    [-78812, 3138, -17757, 1, ],
    [-15114, 17450, -70418, 1, ],
    [-21520, -32138, 56914, 1, ],
    [-66464, 99446, -38908, 1, ],
    [33663, -17670, 56675, 1, ],
    [40762, -29688, -52428, 1, ],
    [-80208, -37572, -46058, 1, ],
    [-91451, -86445, 12986, 1, ],
    [-30237, -88402, 28522, 1, ],
    [-11259, 65445, 8213, 1, ],
    [-508, -55418, -70734, 1, ],
    [69541, -75976, -26843, 1, ],
    [97120, -44146, -65353, 1, ],
    [85649, 72194, 76494, 1, ],
    [12408, 68221, 64233, 1, ],
    [-93589, -26728, -3603, 1, ],
    [-88169, 76862, -94422, 1, ],
    [-85638, -72870, -9239, 1, ],
    [71727, -44310, -42787, 1, ],
    [67301, -70104, 19667, 1, ],
    [-59714, 4985, -45981, 1, ],
    [30250, 62183, -19721, 1, ],
    [14830, 19211, -66453, 1, ],
    [14586, 35480, 69444, 1, ],
    [-89760, 368, -92052, 1, ],
    [63900, 85500, -46420, 1, ],
    [-83748, 95087, -32450, 1, ],
    [-50569, -73696, 18363, 1, ],
    [76836, -71037, 9443, 1, ],
    [-40591, -89347, 30816, 1, ],
    [-24556, 5890, 30051, 1, ],
    [-84017, 52432, 90121, 1, ],
    [-49534, 19393, -20819, 1, ],
    [58389, -57101, -73767, 1, ],
    [-63178, 54623, 70635, 1, ],
    [5114, 10423, -87333, 1, ],
    [-51260, -76676, -92791, 1, ],
    [-21914, 62151, -98574, 1, ],
    [-44934, -40340, 13309, 1, ],
    [-68792, 77639, 57504, 1, ],
    [80448, 7633, 56225, 1, ],
    [-59632, 88321, 71021, 1, ],
    [58356, -71899, 13279, 1, ],
    [85497, -25975, 90241, 1, ],
    [82162, 8533, 15934, 1, ],
    [94249, -50635, 85720, 1, ],
    [50250, 56502, 92949, 1, ],
    [72319, -61008, -90576, 1, ],
    [31377, 22251, 80995, 1, ],
    [-47205, 81830, -5565, 1, ],
    [70647, 37021, -32954, 1, ],
    [-25819, 95750, 55587, 1, ],
    [-29, 75769, -40821, 1, ],
    [-4954, 63435, 15364, 1, ],
    [60306, -54098, -80120, 1, ],
    [-58863, 19006, -13041, 1, ],
    [-52086, 15897, -36644, 1, ],
    [-21630, -93480, 67932, 1, ],
    [10502, 52530, -46869, 1, ],
    [-78152, -49301, -48386, 1, ],
    [68493, 90280, -85255, 1, ],
    [62370, -96178, 80959, 1, ],
    [-58061, 30182, 23338, 1, ],
    [40074, -4052, 88324, 1, ],
    [-25497, -56247, 16431, 1, ],
    [32202, -63925, -3784, 1, ],
    [-65906, 49356, 45448, 1, ],
    [22403, -59817, -83714, 1, ],
    [52775, 68311, 51100, 1, ],
    [41587, 34928, -93649, 1, ],
    [25845, -26287, 17951, 1, ],
    [-46768, -16595, -95811, 1, ],
    [-59519, -44342, 18875, 1, ],
    [43897, 56227, 16876, 1, ],
    [-46596, -41505, -40825, 1, ],
    [-53268, 58837, -52624, 1, ],
    [-28825, -34247, -41362, 1, ],
    [-5394, -62535, -47097, 1, ],
    [26412, -11785, -32068, 1, ],
    [61260, 61523, 97279, 1, ],
    [33410, -55924, -54409, 1, ],
    [15370, -46141, -18244, 1, ],
    [4998, -16773, -56712, 1, ],
    [69753, 13029, 18841, 1, ],
    [-67988, -70802, 28856, 1, ],
    [4356, -79988, -84300, 1, ],
    [55768, 94785, -29942, 1, ],
    [94266, -23066, 28862, 1, ],
    [31891, -78785, -63680, 1, ],
    [-42448, 34939, -4560, 1, ],
    [33827, -2844, -30636, 1, ],
    [-90773, 58594, -12162, 1, ],
    [56596, 64046, -77925, 1, ],
    [28412, -96620, 19322, 1, ],
    [31807, -91840, 2206, 1, ],
    [64598, -55345, -67102, 1, ],
    [60412, -68209, 57858, 1, ],
    [67163, 4760, 17875, 1, ],
    [77053, -18106, -21575, 1, ],
    [-39748, 5847, -17917, 1, ],
    [41874, 97395, -74725, 1, ],
    [-46772, -28880, 62170, 1, ],
    [24506, -92907, 9442, 1, ],
    [-95088, -85557, 42157, 1, ],
    [-83222, -77062, -16666, 1, ],
    [-82169, 97163, -25468, 1, ],
    [86745, -10015, -60533, 1, ],
    [-55224, -26023, 95885, 1, ],
    [-16050, -51467, 51951, 1, ],
    [31158, 3032, -91688, 1, ],
    [-95195, 84595, 9565, 1, ],
    [-53951, 69979, -42241, 1, ],
    [46722, -93873, 97238, 1, ],
    [21980, 84450, -3301, 1, ],
    [93906, -46295, 41576, 1, ],
    [81417, -73873, -20516, 1, ],
    [-73095, 62472, -50291, 1, ],
    [33196, -46622, 28990, 1, ],
    [-22200, 32863, -91037, 1, ],
    [-8324, 75046, 20062, 1, ],
    [-88556, 41256, 80790, 1, ],
    [-71325, -57470, -93573, 1, ],
    [47803, -21809, -64598, 1, ],
    [9257, 94393, -86107, 1, ],
    [17838, -69739, 30672, 1, ],
    [80450, -96814, 14481, 1, ],
    [-92158, 69521, -82540, 1, ],
    [-22457, -73939, -2202, 1, ],
    [81146, -20328, 92864, 1, ],
    [85087, -43446, -39905, 1, ],
    [97243, -86173, 27339, 1, ],
    [-75945, 27066, -69906, 1, ],
    [-17084, 80768, 32799, 1, ],
    [1727, -51714, -12003, 1, ],
    [-73896, 99209, 30641, 1, ],
    [-90878, 10307, 6753, 1, ],
    [6315, -66488, -74104, 1, ],
    [-85482, -3315, -97842, 1, ],
    [-8224, 26887, 39522, 1, ],
    [-99294, 44526, -17289, 1, ],
    [67027, -10293, 65998, 1, ],
    [58140, -19889, 61138, 1, ],
    [-25509, -21844, -6268, 1, ],
    [97330, -19610, 15562, 1, ],
    [-84766, 15758, 46987, 1, ],
    [57264, -15405, -7106, 1, ],
    [83935, 56699, -7278, 1, ],
    [-36118, -47753, 32420, 1, ],
    [60710, 24319, -95227, 1, ],
    [-49100, -80389, -39938, 1, ],
    [5013, 94930, 30808, 1, ],
    [-22702, 87455, -52733, 1, ],
    [-45943, -80195, -46423, 1, ],
    [15146, -67893, 19370, 1, ],
    [67721, 18776, -28867, 1, ],
    [33808, 89860, 27947, 1, ],
    [41672, -80473, 81735, 1, ],
    [30420, -12722, -29792, 1, ],
    [38227, 1712, 80586, 1, ],
    [-48851, -80701, 92875, 1, ],
    [-44573, -81541, 63461, 1, ],
    [74296, 86930, 25329, 1, ],
    [-73998, 97925, -66384, 1, ],
    [79663, 97268, 41791, 1, ],
    [44131, 35285, 62492, 1, ],
    [-97589, 92001, 51267, 1, ],
    [76218, -85429, 26717, 1, ],
    [42694, -8835, -66522, 1, ],
    [-12057, 96806, 55693, 1, ],
    [-82756, 94865, -20714, 1, ],
    [27615, 76034, 3065, 1, ],
    [84551, -67454, 79054, 1, ],
    [75108, -29804, -70292, 1, ],
    [38368, 73929, 92004, 1, ],
    [-16554, -42455, 10295, 1, ],
    [-40763, 6189, 36063, 1, ],
    [-45220, 63492, -14602, 1, ],
    [40267, 70413, -68824, 1, ],
    [-84356, 83193, 22576, 1, ],
    [70177, 69444, -68499, 1, ],
    [-12306, 71905, -69808, 1, ],
    [-17174, -52315, -22466, 1, ],
    [20328, -55007, -54496, 1, ],
    [67567, 50265, -43032, 1, ],
    [97590, -54471, 3016, 1, ],
    [27245, 33033, 83527, 1, ],
    [8633, -94692, 37414, 1, ],
    [12024, 63864, -58315, 1, ],
    [-25485, 66004, -18, 1, ],
    [-21689, 18603, 15087, 1, ],
    [-29158, 44006, -84862, 1, ],
    [-12056, -5258, 57456, 1, ],
    [-63614, -95894, 56432, 1, ],
    [-74872, -90657, -43597, 1, ],
    [36834, -67993, -31383, 1, ],
    [28804, 72016, -58860, 1, ],
    [8296, 58926, -42351, 1, ],
    [-25940, -70957, -45775, 1, ],
    [77504, -73165, 3981, 1, ],
    [29722, -39903, -74683, 1, ],
    [45394, -45880, 59445, 1, ],
    [-69572, 4877, -21213, 1, ],
    [-51809, 75523, 24380, 1, ],
    [-66313, -76746, -56201, 1, ],
    [88968, -10319, -6291, 1, ],
    [-30180, 63304, 63974, 1, ],
    [-17195, 64838, -11997, 1, ],
    [61112, 18917, 95023, 1, ],
    [-95858, 75845, -22539, 1, ],
    [-77499, -53606, 67241, 1, ],
    [53730, 75142, -19042, 1, ],
    [55807, 61807, 75555, 1, ],
    [74454, 54133, -31886, 1, ],
    [-66511, 46996, 58836, 1, ],
    [39395, -59137, 63176, 1, ],
    [87295, 90243, 32931, 1, ],
    [-56918, 16796, 15103, 1, ],
    [-83052, -87101, 14549, 1, ],
    [65666, -34910, 42981, 1, ],
    [-53135, 57563, -19088, 1, ],
    [-33005, -98480, -43396, 1, ],
    [-55397, -91514, 49838, 1, ],
    [54492, -80645, 12886, 1, ],
    [-86337, 604, 26647, 1, ],
    [-78458, 35969, -66628, 1, ],
    [46633, 76479, 42643, 1, ],
    [6337, -63365, -42683, 1, ],
    [99188, -93814, -74513, 1, ],
    [77904, -17072, 9964, 1, ],
    [86857, 79146, 40713, 1, ],
    [3511, -59984, -26677, 1, ],
    [-2078, 87912, 77803, 1, ],
    [-97771, 80103, 95212, 1, ],
    [31457, -16353, -99014, 1, ],
    [91718, -79861, -43968, 1, ],
    [-80573, -47124, -6549, 1, ],
    [22745, -31004, -30611, 1, ],
    [60043, 84261, -40325, 1, ],
    [88825, -63774, 46095, 1, ],
    [71281, 40483, 94618, 1, ],
    [-97918, -42215, -2746, 1, ],
    [-59624, 89299, -14851, 1, ],
    [10242, 96301, 87818, 1, ],
    [97030, -69288, -96977, 1, ],
    [60902, -65373, 32648, 1, ],
    [3871, 61143, -55273, 1, ],
    [-30502, -94958, 48801, 1, ],
    [90578, -9140, -96236, 1, ],
    [-4120, -42851, -90412, 1, ],
    [78337, -25905, 70486, 1, ],
    [-59464, 72572, -2391, 1, ],
    [-29255, 26123, 61591, 1, ],
    [91700, -83228, -9373, 1, ],
    [-39313, 14523, -87844, 1, ],
    [-49034, 67232, -19939, 1, ],
    [-78322, -44208, -4182, 1, ],
    [36232, 16720, -59053, 1, ],
    [-97040, -22405, 47521, 1, ],
    [-17219, 4727, 31467, 1, ],
    [-21546, -21113, 48549, 1, ],
    [-4846, -41902, 17950, 1, ],
    [5997, -80790, 26401, 1, ],
    [-87384, 58343, 67985, 1, ],
    [41254, 91966, 2406, 1, ],
    [4297, -78986, 53237, 1, ],
    [-87079, -58190, -27115, 1, ],
    [44821, 83528, -42678, 1, ],
    [-78618, 94266, -62940, 1, ],
    [73684, -50439, -71424, 1, ],
    [-29528, -36537, 65554, 1, ],
    [-94661, 75665, -60109, 1, ],
    [-98620, -22158, 52976, 1, ],
    [-10627, -21597, 56102, 1, ],
    [56786, -67199, 20663, 1, ],
    [-54802, 10759, 95665, 1, ],
    [-13243, -25309, 56744, 1, ],
    [30343, 35705, -27647, 1, ],
    [74899, -4764, -49769, 1, ],
    [47052, -57472, -37487, 1, ],
    [18296, -73261, -89546, 1, ],
    [20986, -46366, -71992, 1, ],
    [-50538, -87379, 40180, 1, ],
    [-79601, -86475, -7740, 1, ],
    [17306, 2543, -14787, 1, ],
    [45800, -84624, 48020, 1, ],
    [-79029, 65700, -62189, 1, ],
    [-70366, 12354, -16001, 1, ],
    [-89995, -91867, -23407, 1, ],
    [-72849, 34427, 2490, 1, ],
    [10477, -10136, 58974, 1, ],
    [-69099, -14530, -86099, 1, ],
    [-86240, 2877, -30319, 1, ],
    [78997, -29594, 91040, 1, ],
    [-30503, -11942, -6635, 1, ],
    [-84360, -31066, -31642, 1, ],
    [24496, 5741, 64144, 1, ],
    [52946, -44294, 46435, 1, ],
    [-85935, 76405, 46795, 1, ],
    [-80807, 65741, -7422, 1, ],
    [6438, -22097, -75698, 1, ],
    [-32949, 59813, 43716, 1, ],
    [23779, -32635, 33770, 1, ],
    [-74623, 25711, -52041, 1, ],
    [93929, 49617, 69445, 1, ],
    [-89622, -99578, 77553, 1, ],
    [-59318, 37780, -45919, 1, ],
    [264, -7034, -51772, 1, ],
    [16516, -49483, -88473, 1, ],
    [46434, -52800, 21614, 1, ],
    [-10484, 7783, -81806, 1, ],
    [-91796, 56593, -11782, 1, ],
    [-34492, 45261, -35097, 1, ],
    [10690, 61850, -62170, 1, ],
    [-9280, 68113, -15556, 1, ],
    [32192, -32352, 69643, 1, ],
    [-85041, 57964, -3484, 1, ],
    [-64040, -59935, -61025, 1, ],
    [25015, 18553, 33197, 1, ],
    [-66086, 92965, 55501, 1, ],
    [84938, -94941, 95456, 1, ],
    [-48544, -43288, -82630, 1, ],
    [92590, -56955, -71296, 1, ],
    [-499, 39329, -40018, 1, ],
    [-85697, -76361, 86362, 1, ],
    [23879, -58210, 94879, 1, ],
    [-82926, 29795, 78691, 1, ],
    [85191, -46901, -37243, 1, ],
    [74395, -30941, 92435, 1, ],
    [87699, -49307, 55910, 1, ],
    [99337, -99444, 75215, 1, ],
    [-66385, -94484, -51799, 1, ],
    [-20794, -95194, -3889, 1, ],
    [-80423, 87225, 82020, 1, ],
    [40681, -56810, -44772, 1, ],
    [83325, 75618, 75285, 1, ],
    [-28658, -88814, -26684, 1, ],
    [-65475, 19669, 93532, 1, ],
    [-6604, 27581, 20384, 1, ],
    [66074, -87289, 41604, 1, ],
    [-92584, 4885, -30594, 1, ],
    [-32779, -94011, -16069, 1, ],
    [93593, 6759, -32630, 1, ],
    [98081, 94850, 53305, 1, ],
    [14216, 1278, 76105, 1, ],
    [85819, -67659, -82068, 1, ],
    [33961, 66230, -10637, 1, ],
    [-62475, 91991, 28743, 1, ],
    [65007, -57341, 33754, 1, ],
    [-91760, -28298, 37375, 1, ],
    [-78215, 48723, -62034, 1, ],
    [-58335, -10397, 44382, 1, ],
    [94611, -39224, -17245, 1, ],
    [15754, 42968, 56975, 1, ],
    [-21885, 66692, 73104, 1, ],
    [-31472, -39453, -35929, 1, ],
    [-27290, 21071, -69055, 1, ],
    [20074, -46082, 3782, 1, ],
    [-58609, 75630, -47414, 1, ],
    [-32440, 90393, 21533, 1, ],
    [36868, 64941, 47267, 1, ],
    [52008, -51903, -97477, 1, ],
    [-50459, 72665, -3055, 1, ],
    [-28721, 36990, 5123, 1, ],
    [78591, -10212, -66540, 1, ],
    [4325, 21712, 38472, 1, ],
    [30362, -31962, -82159, 1, ],
    [-74281, -23267, -25347, 1, ],
    [45765, -29945, 97342, 1, ],
    [70969, -67543, 77475, 1, ],
    [72361, 51346, -41910, 1, ],
    [-556, -31397, 45870, 1, ],
    [15672, -80237, 4519, 1, ],
    [-19071, -78113, -60945, 1, ],
    [80201, -88110, -4802, 1, ],
    [68009, 11910, 16096, 1, ],
    [-11486, -52301, -43770, 1, ],
    [-28249, -36174, 67215, 1, ],
    [85960, 72043, -55373, 1, ],
    [-7542, -75095, 69159, 1, ],
    [11866, 39662, -46403, 1, ],
    [40027, -11558, 90097, 1, ],
    [-73764, -89766, 7531, 1, ],
    [47940, 45645, -57868, 1, ],
    [-53513, 96231, 88346, 1, ],
    [-82958, 95665, 73277, 1, ],
    [-95583, 91241, -90343, 1, ],
    [784, 76854, -64153, 1, ],
    [-26183, -4077, -67962, 1, ],
    [-42170, -94509, -56341, 1, ],
    [75425, 4734, 58827, 1, ],
    [-90851, -50996, 60012, 1, ],
    [-78793, 78447, 19577, 1, ],
    [-87694, 761, 47318, 1, ],
    [-49913, -8614, -12573, 1, ],
    [91444, -98188, -51716, 1, ],
    [-13608, 91784, 15876, 1, ],
    [-27817, -51209, -14333, 1, ],
    [-85057, 54755, 95483, 1, ],
    [51076, 1761, -39244, 1, ],
    [-46531, 15493, -67861, 1, ],
    [-72889, 78463, 38152, 1, ],
    [-74684, 89612, 86056, 1, ],
    [10787, 40452, -82305, 1, ],
    [60513, -4723, 17638, 1, ],
    [94940, 47910, -24141, 1, ],
    [-41709, 2219, -85954, 1, ],
    [74494, -84963, 58495, 1, ],
    [17997, -64669, 75871, 1, ],
    [57070, -21072, -57781, 1, ],
    [38766, 83050, 10938, 1, ],
    [96018, 23813, 1677, 1, ],
    [-48786, -25997, 95388, 1, ],
    [-87900, -38294, -84377, 1, ],
    [-61639, -93363, -54554, 1, ],
    [-25063, 40160, -25791, 1, ],
    [-75414, -1967, 92618, 1, ],
    [-30646, 99757, -5871, 1, ],
    [-12617, 43179, 2972, 1, ],
    [-86212, 32448, -94593, 1, ],
    [-15188, 95345, 78460, 1, ],
    [67963, 94544, -41737, 1, ],
    [93545, -40553, -31590, 1, ],
    [-78017, -66137, 34973, 1, ],
    [96506, 23164, 17311, 1, ],
    [6514, 3618, -74193, 1, ],
    [55231, -11046, -67430, 1, ],
    [34672, -60395, -68142, 1, ],
    [14036, 79626, 80406, 1, ],
    [2438, -61921, 59111, 1, ],
    [-44968, -51555, -46441, 1, ],
    [-34713, -99412, 3719, 1, ],
    [28080, 61882, -71586, 1, ],
    [87323, -373, 61912, 1, ],
    [52777, -69453, -3955, 1, ],
    [28233, 71450, -96105, 1, ],
    [-72059, 39321, -65524, 1, ],
    [4518, -18208, 25605, 1, ],
    [64269, 50516, -78330, 1, ],
    [-16828, -78435, -5588, 1, ],
    [41305, 72562, 70642, 1, ],
    [65913, -22513, -56605, 1, ],
    [47235, -72592, 97418, 1, ],
    [27211, 44973, 78608, 1, ],
    [-39560, 71629, 43519, 1, ],
    [13860, 12161, -47727, 1, ],
    [57725, -73337, 65816, 1, ],
    [70866, -18312, 50367, 1, ],
    [-46355, 15057, -50465, 1, ],
    [16121, 35888, -72029, 1, ],
    [91511, -92029, 72903, 1, ],
    [75274, 7970, -90026, 1, ],
    [55371, 92202, 63033, 1, ],
    [13380, -93622, -80855, 1, ],
    [-37931, -69672, 90514, 1, ],
    [31375, 76544, -31102, 1, ],
    [-34297, 4408, 23078, 1, ],
    [-29559, -58914, 91441, 1, ],
    [-40311, 33825, -75806, 1, ],
    [5220, 17582, 77039, 1, ],
    [96507, 61137, -45154, 1, ],
    [-37330, 97717, 26254, 1, ],
    [3344, -44372, -63488, 1, ],
    [-1082, 17774, -81464, 1, ],
    [12110, -15763, 31157, 1, ],
    [42345, -11065, -9093, 1, ],
    [93140, 91475, -39041, 1, ],
    [-47846, -24964, -19053, 1, ],
    [47945, 55934, 93581, 1, ],
    [25838, 85734, 97804, 1, ],
    [-41113, -32303, -99007, 1, ],
    [-57734, 46598, 29669, 1, ],
    [-94299, -96702, 83489, 1, ],
    [-54355, 80431, 73872, 1, ],
    [-54399, -89348, -60630, 1, ],
    [-34495, 86049, -93844, 1, ],
    [72229, 60377, 45550, 1, ],
    [-25703, 27126, -53488, 1, ],
    [52499, -90630, -88155, 1, ],
    [79662, 99665, 11704, 1, ],
    [5302, 81303, 9712, 1, ],
    [55828, -22294, -21658, 1, ],
    [46928, 31091, -64878, 1, ],
    [-71801, 75489, 28919, 1, ],
    [-72260, 77325, 16083, 1, ],
    [-13285, -38827, -83217, 1, ],
    [-97166, 27417, 85940, 1, ],
    [-62395, 36906, 80737, 1, ],
    [-76918, 44866, 126, 1, ],
    [62636, 82183, -17567, 1, ],
    [-92319, -66880, -58359, 1, ],
    [57395, -48861, -94824, 1, ],
    [67120, -9674, -31398, 1, ],
    [82104, -10672, 56644, 1, ],
    [37259, -99442, 89733, 1, ],
    [-38199, -1448, -79997, 1, ],
    [26611, 60692, -12620, 1, ],
    [24210, -83251, -4672, 1, ],
    [-67640, -12572, -67936, 1, ],
    [-61917, 64341, -62756, 1, ],
    [3024, 99111, 47960, 1, ],
    [-2562, 39605, -29759, 1, ],
    [-43568, -42540, -72762, 1, ],
    [31295, -5783, -25622, 1, ],
    [73922, 89945, 73664, 1, ],
    [-98011, 18628, -38540, 1, ],
    [-52137, 31654, 70986, 1, ],
    [63408, 25917, -16109, 1, ],
    [86779, 15246, -30537, 1, ],
    [-16852, 23557, -60344, 1, ],
    [-91088, -4491, 96704, 1, ],
    [12073, -54283, -68008, 1, ],
    [-81864, 19378, -32915, 1, ],
    [-34579, 85955, -24298, 1, ],
    [2872, 34956, 74953, 1, ],
    [-21010, 27418, 34504, 1, ],
    [-39856, -6641, 40219, 1, ],
    [5116, 30267, 62220, 1, ],
    [25862, -85056, 43646, 1, ],
    [-63050, 2349, 2645, 1, ],
    [-84809, 47407, -576, 1, ],
    [6606, -3200, 58396, 1, ],
    [56483, -67876, -1194, 1, ],
    [-17013, -57523, -74683, 1, ],
    [-67661, -31900, 67982, 1, ],
    [71684, 3169, -52502, 1, ],
    [-29460, -72155, -90035, 1, ],
    [-29550, 5034, 29206, 1, ],
    [-6151, 99184, 23338, 1, ],
    [-13870, 77415, 94066, 1, ],
    [-28943, 54324, 16586, 1, ],
    [-39353, -12119, 31545, 1, ],
    [-7166, 58795, 50780, 1, ],
    [-74160, 53023, 22164, 1, ],
    [-91189, -4316, 81411, 1, ],
    [-49768, -24233, -91711, 1, ],
    [39629, -11985, 73440, 1, ],
    [12234, 63073, -51637, 1, ],
    [-63116, 60532, -14521, 1, ],
    [53937, -54647, -66525, 1, ],
    [-85980, 43296, -13228, 1, ],
    [52035, -97284, 3679, 1, ],
    [-74450, 78282, -59591, 1, ],
    [-22945, -82551, -44114, 1, ],
    [-70047, -33253, -22099, 1, ],
    [3555, -3395, -28043, 1, ],
    [5520, 23749, -3608, 1, ],
    [66871, 83446, 2694, 1, ],
    [-24789, 8424, -37774, 1, ],
    [20172, -23047, -10986, 1, ],
    [-63450, 35179, -17673, 1, ],
    [-4033, -26979, 20802, 1, ],
    [-4993, 37117, 63341, 1, ],
    [57509, 98523, 13203, 1, ],
    [99762, -97595, 75576, 1, ],
    [-75010, -38139, -17586, 1, ],
    [72238, -34345, -62674, 1, ],
    [-61474, 90285, -27933, 1, ],
    [30230, 25107, -89518, 1, ],
    [-5990, -26253, -47942, 1, ],
    [-73820, 93272, -89648, 1, ],
    [-47190, -7793, -50209, 1, ],
    [25270, -87635, 17656, 1, ],
    [-13887, -72989, 55132, 1, ],
    [-47565, 84991, 61696, 1, ],
    [95867, -20555, 77327, 1, ],
    [47626, -89791, -5248, 1, ],
    [-16485, 12045, 46187, 1, ],
    [-7303, -82277, 5213, 1, ],
    [44533, -82853, -74300, 1, ],
    [90042, -21599, -77835, 1, ],
    [-49642, -74416, 72746, 1, ],
    [5477, 95869, 94340, 1, ],
    [-5126, 66410, -50181, 1, ],
    [-45756, -13490, -25627, 1, ],
    [-80796, 15952, -39452, 1, ],
    [-41661, 55144, 68604, 1, ],
    [-32926, -44460, -40598, 1, ],
    [-34475, -31616, -60769, 1, ],
    [87593, 88544, -35149, 1, ],
    [65559, -80908, -57685, 1, ],
    [3406, 85880, -95804, 1, ],
    [-95028, 52735, 12836, 1, ],
    [93803, 18584, 51406, 1, ],
    [81284, 35793, 93808, 1, ],
    [-38985, 18416, -26200, 1, ],
    [83596, 32454, 44129, 1, ],
    [45635, 55603, 81760, 1, ],
    [-19551, -98015, 33820, 1, ],
    [5269, -26478, -29327, 1, ],
    [-75431, -16340, 96705, 1, ],
    [29582, -4224, 51086, 1, ],
    [19378, -57379, 71196, 1, ],
    [-30788, -20194, 64190, 1, ],
    [-7420, -45970, -62382, 1, ],
    [-17802, -61536, 93774, 1, ],
    [47902, 15043, 90686, 1, ],
    [62636, -10659, 53838, 1, ],
    [70462, 4491, -51361, 1, ],
    [-64404, 4985, 33636, 1, ],
    [-92824, -67662, -33557, 1, ],
    [60661, -19271, 27999, 1, ],
    [85303, -49435, -27081, 1, ],
    [-64945, 31521, 5884, 1, ],
    [86536, -52141, -45953, 1, ],
    [98026, -97813, -9678, 1, ],
    [-17702, -74714, -47162, 1, ],
    [-30514, -58539, -42701, 1, ],
    [-54513, 33454, -45302, 1, ],
    [72741, -53232, -76976, 1, ],
    [-84488, 3618, -72137, 1, ],
    [-60975, -91999, -19953, 1, ],
    [83837, -28258, -4539, 1, ],
    [806, 48948, 31133, 1, ],
    [-98441, 47106, -47958, 1, ],
    [-98234, 46499, 51277, 1, ],
    [-32843, 72147, 85745, 1, ],
    [35351, 64642, 50598, 1, ],
    [94997, -75078, 97629, 1, ],
    [-68846, 7974, 70263, 1, ],
    [-62767, -79993, 55848, 1, ],
    [2233, -63706, 37680, 1, ],
    [46398, -83729, -15885, 1, ],
    [-20287, -53469, 79978, 1, ],
    [-64880, 56421, -91151, 1, ],
    [58758, -74383, 87086, 1, ],
    [13605, -1553, 7525, 1, ],
    [67023, -41658, 32700, 1, ],
    [99594, 34442, -75797, 1, ],
    [26737, -39344, -92299, 1, ],
    [-66826, -39622, 3866, 1, ],
    [-53594, 64032, -46732, 1, ],
    [-83902, -30199, -20077, 1, ],
    [32303, -44428, 69377, 1, ],
    [-17706, 8473, 61458, 1, ],
    [-32256, -32369, -96809, 1, ],
    [22612, 91604, -71638, 1, ],
    [6540, -27219, 45265, 1, ],
    [65857, 19651, 9712, 1, ],
    [54627, -96856, 88458, 1, ],
    [20577, -17959, 95867, 1, ],
    [-75387, -88011, -88070, 1, ],
    [56976, 79414, -84169, 1, ],
    [46722, -91260, -29003, 1, ],
    [67734, 91392, -2504, 1, ],
    [-95434, 70810, 89713, 1, ],
    [-72757, 58423, -90919, 1, ],
    [-11512, -4704, 74079, 1, ],
    [80159, 61530, 27028, 1, ],
    [41829, 8342, -16227, 1, ],
    [-59390, -66365, -23567, 1, ],
    [-73332, -17130, 4518, 1, ],
    [25927, -25223, 91704, 1, ],
    [21884, 72480, -15775, 1, ],
    [30682, 37325, 50497, 1, ],
    [-32215, 48276, 32869, 1, ],
    [-23018, -22156, 79963, 1, ],
    [-15556, -49576, -8332, 1, ],
    [-89517, -35327, 98728, 1, ],
    [-32780, 56128, -24050, 1, ],
    [43550, 58263, 74366, 1, ],
    [28507, 37947, -9541, 1, ],
    [58690, 49918, -85125, 1, ],
    [-19717, -90892, -32355, 1, ],
    [-6772, 55458, -13583, 1, ],
    [-47641, 12305, 74659, 1, ],
    [-94800, 84054, -24976, 1, ],
    [23562, -93810, -41461, 1, ],
    [39356, -81116, -99845, 1, ],
    [65060, 80807, 86850, 1, ],
    [-37724, -42992, 91736, 1, ],
    [57500, -88272, 582, 1, ],
    [7428, -19852, 79265, 1, ],
    [74167, -31516, -44598, 1, ],
    [-60698, 31451, -10370, 1, ],
    [-47676, -17007, -69227, 1, ],
    [-52421, 61151, 19531, 1, ],
    [-28611, -50744, -20723, 1, ],
    [-72546, 77007, 50840, 1, ],
    [55356, -53362, -76093, 1, ],
    [-64382, -9805, -36797, 1, ],
    [16659, -12623, 56864, 1, ],
    [-61025, 22017, -14438, 1, ],
    [20818, -22152, 77248, 1, ],
    [-56905, -3950, -2411, 1, ],
    [-86940, -85647, -39451, 1, ],
    [99985, -23012, -2569, 1, ],
    [97328, 65650, -74150, 1, ],
    [10748, -12287, 8103, 1, ],
    [-39352, 22594, -58412, 1, ],
    [3881, 11766, -21376, 1, ],
    [-56223, -12726, -15983, 1, ],
    [74249, -38713, 68954, 1, ],
    [-97506, 17194, 43079, 1, ],
    [-69075, 53950, 9925, 1, ],
    [80208, -11933, -17681, 1, ],
    [-199, -57660, 84176, 1, ],
    [95591, 7699, 79148, 1, ],
    [-31247, 35300, -14049, 1, ],
    [86574, 41484, -84832, 1, ],
    [2260, -67526, -3957, 1, ],
    [-69246, 18512, -35567, 1, ],
    [-41209, 46056, -76680, 1, ],
    [-55030, -96443, -61234, 1, ],
    [25416, 47757, -28131, 1, ],
    [-29638, -65900, 85573, 1, ],
    [29526, 10756, -68113, 1, ],
    [51642, -86913, 67154, 1, ],
    [-15168, -4637, 85512, 1, ],
    [-55131, -60035, -97085, 1, ],
    [-91031, -71547, -9728, 1, ],
    [-76748, 82618, 71013, 1, ],
    [-80235, 84459, -13903, 1, ],
    [7478, -16975, 47287, 1, ],
    [49270, 71585, 11788, 1, ],
    [-72438, 55430, -46542, 1, ],
    [-5558, 89905, 10157, 1, ],
    [-57392, -86057, -13133, 1, ],
    [-49325, 34212, -74571, 1, ],
    [80391, -41512, 36504, 1, ],
    [5724, 88055, 59421, 1, ],
    [-53520, 21574, -24527, 1, ],
    [38933, 53873, 33901, 1, ],
    [99814, -1861, -22132, 1, ],
    [69001, 68155, -38195, 1, ],
    [8762, 70531, 46284, 1, ],
    [43406, 1248, -48966, 1, ],
    [65366, -89368, 42703, 1, ],
    [23599, -52899, -91004, 1, ],
    [65987, -98796, 44744, 1, ],
    [53273, 86989, -9436, 1, ],
    [81654, 65790, 73495, 1, ],
    [63443, 22800, 57614, 1, ],
    [71921, -38355, 26945, 1, ],
    [24852, -4738, -62984, 1, ],
    [53282, 6255, -79858, 1, ],
    [31214, -91366, -79798, 1, ],
    [-28890, 47207, 52436, 1, ],
    [-74874, 19875, 548, 1, ],
    [-4660, 21375, 84314, 1, ],
    [-19586, 7113, -97749, 1, ],
    [45265, -23321, -22598, 1, ],
    [96309, -35877, -46460, 1, ],
    [41066, -28026, -66281, 1, ],
    [-87727, -27567, -23126, 1, ],
    [28694, 85305, 71228, 1, ],
    [44444, -43303, 950, 1, ],
    [-31214, 14418, -47767, 1, ],
    [-85865, -36847, -52668, 1, ],
    [-55311, -51767, -14144, 1, ],
    [29958, -7528, 92601, 1, ],
    [86888, 74046, 61730, 1, ],
    [74542, -72912, 99953, 1, ],
    [-22690, -27046, -82207, 1, ],
    [-71005, 37416, 41329, 1, ],
    [13739, -18400, 87654, 1, ],
    [5483, -93402, -80145, 1, ],
    [18614, 5465, -85796, 1, ],
    [-82349, -76, -30688, 1, ],
    [-80358, -51729, 23910, 1, ],
    [-67866, -53348, -52124, 1, ],
    [20162, 7470, -47878, 1, ],
    [1370, -16130, -59600, 1, ],
    [-26266, -15796, 78042, 1, ],
    [84575, 19435, -78098, 1, ],
    [89557, 35198, -97555, 1, ],
    [47135, -68959, 1456, 1, ],
    [-25291, 83427, 95841, 1, ],
    [61664, 99071, 3634, 1, ],
    [-93195, 87073, 94638, 1, ],
    [-80725, 88983, 33617, 1, ],
    [-95994, -85747, -34455, 1, ],
    [-87853, -58552, -28616, 1, ],
    [-28439, -35706, 59856, 1, ],
    [24361, -77585, 90460, 1, ],
    [-64190, -52776, -78161, 1, ],
    [21591, -2557, 53522, 1, ],
    [45091, 29824, -80227, 1, ],
    [-15960, -11435, 87341, 1, ],
    [11733, -56356, -32927, 1, ],
    [61505, -2249, -14841, 1, ],
    [86196, 85375, -55142, 1, ],
    [-45272, 7205, -16191, 1, ],
    [-87829, -76710, -11282, 1, ],
    [55001, -70711, 80174, 1, ],
    [-44870, -62116, 18497, 1, ],
    [6077, 97857, -60593, 1, ],
    [-2248, 39564, 78177, 1, ],
    [-22063, 28769, -50118, 1, ],
    [58039, 13158, -47912, 1, ],
    [-11084, 37431, -48670, 1, ],
    [86986, -59062, -51368, 1, ],
    [-86406, 99306, 99349, 1, ],
    [16722, -93836, 2839, 1, ],
    [-6525, -59726, 18631, 1, ],
    [-71884, -9730, 84043, 1, ],
    [33861, 61180, -24897, 1, ],
    [58824, 86867, -81569, 1, ],
    [80360, 42999, 32392, 1, ],
    [81783, -38886, 54902, 1, ],
    [75599, 53499, 77498, 1, ],
    [-67605, 31535, -75032, 1, ],
    [95956, -81751, -48908, 1, ],
    [19317, 68613, 65367, 1, ],
    [86546, -88067, -24284, 1, ],
    [-63915, 16874, 80507, 1, ],
    [-90679, -90679, -11498, 1, ],
    [-85112, -68185, -78314, 1, ],
    [-34752, 68096, -98709, 1, ],
    [-14246, -43663, 55058, 1, ],
    [-12638, 33245, -66734, 1, ],
    [-2613, 60308, -4035, 1, ],
    [61563, -82835, 65903, 1, ],
    [-12586, 95095, -59654, 1, ],
    [-14444, -61828, -36370, 1, ],
    [35158, 60409, 23959, 1, ],
    [-63837, -21254, -34094, 1, ],
    [-92461, 5053, -33946, 1, ],
    [34647, -10070, 59253, 1, ],
    [-71877, 97696, 86463, 1, ],
    [81380, 64010, -44045, 1, ],
    [-44882, -98581, -42509, 1, ],
    [-22981, 14584, -53866, 1, ],
    [80759, 34703, -47761, 1, ],
    [74052, 18438, -2133, 1, ],
    [8615, 13025, -57202, 1, ],
    [-16539, 75689, 60402, 1, ],
    [-61619, -94704, -24402, 1, ],
    [37840, 59492, -93951, 1, ],
    [58788, 60173, -39313, 1, ],
    [-34206, 15821, -25133, 1, ],
    [6499, -31938, -13483, 1, ],
    [-5972, -89632, 14530, 1, ],
    [-22647, -19934, 60952, 1, ],
    [-6908, 27017, 50946, 1, ],
    [-72127, -76587, -35402, 1, ],
    [-47278, -70968, -48878, 1, ],
    [-13567, 5626, 2939, 1, ],
    [29540, -57831, 42454, 1, ],
    [3600, -47582, -63305, 1, ],
    [10650, 89527, -39910, 1, ],
    [-30584, -74720, 39283, 1, ],
    [76949, -80902, 14291, 1, ],
    [-65510, -94707, 85276, 1, ],
    [13945, -84817, -4375, 1, ],
    [47567, -14631, 28862, 1, ],
    [-75563, -10562, 74489, 1, ],
    [-93291, 51434, 95712, 1, ],
    [43472, -65259, -55740, 1, ],
    [7798, -5186, -73851, 1, ],
    [7580, 28076, 17972, 1, ],
    [40852, 51928, 7535, 1, ],
    [86630, 25071, -81473, 1, ],
    [37224, 53370, 67787, 1, ],
    [99199, -33793, 99467, 1, ],
    [-95598, 88535, 89200, 1, ],
    [-70915, -33147, 65077, 1, ],
    [59563, -7022, 75590, 1, ],
    [40803, 2097, -74788, 1, ],
    [84721, -94176, 23048, 1, ],
    [-21369, 68911, 73129, 1, ],
    [52830, -97856, 94222, 1, ],
    [-58775, 37268, 36143, 1, ],
    [-89944, 3943, -82930, 1, ],
    [-48442, -19745, 84716, 1, ],
    [85197, 36336, 29613, 1, ],
    [4994, 41388, 94708, 1, ],
    [-19596, 35321, -19737, 1, ],
    [-21082, -74737, -15761, 1, ],
    [87667, 61145, -27354, 1, ],
    [-11692, -14178, 42527, 1, ],
    [98683, 93296, -70652, 1, ],
    [6369, 63783, -92109, 1, ],
    [-44207, -61698, 90090, 1, ],
    [-10836, 61365, 18849, 1, ],
    [53266, -38437, 82795, 1, ],
    [88357, -21776, 97808, 1, ],
    [-9194, -52785, -55711, 1, ],
    [-13432, -50774, -55312, 1, ],
    [86383, 19018, 48688, 1, ],
    [49052, -53787, -33731, 1, ],
    [31494, 86901, 21059, 1, ],
    [-33838, -82446, 31801, 1, ],
    [62275, 32513, 42831, 1, ],
    [46979, 32437, -45182, 1, ],
    [-70299, -52978, -26783, 1, ],
    [68288, -88902, -52398, 1, ],
    [74432, 82647, -28630, 1, ],
    [31743, 43449, -38491, 1, ],
    [55945, 62522, 77894, 1, ],
    [65448, 98953, -17876, 1, ],
    [7110, -39474, -18128, 1, ],
    [-57932, 28065, 41187, 1, ],
    [-88857, 37898, -56741, 1, ],
    [-61515, -13389, -11593, 1, ],
    [-21298, -33680, -63204, 1, ],
    [-87117, 69053, 68369, 1, ],
    [-11170, -11221, -38748, 1, ],
    [-70924, -90602, 66832, 1, ],
    [-28245, 49281, 42216, 1, ],
    [-99431, -8217, 76126, 1, ],
    [69398, 92024, 92583, 1, ],
    [-74521, -49826, 1139, 1, ],
    [-49986, 10081, 83980, 1, ],
    [-39955, 39181, 57726, 1, ],
    [15402, 75558, -13422, 1, ],
    [76717, -8734, 26540, 1, ],
    [-34481, -33883, -76307, 1, ],
    [72029, -66232, 77274, 1, ],
    [-42765, 9448, -57814, 1, ],
    [-61462, -4874, -39552, 1, ],
    [60508, 71593, 87905, 1, ],
    [-89066, 21693, 95712, 1, ],
    [-78956, 76336, -29127, 1, ],
    [-56538, -55634, -70811, 1, ],
    [-68885, -41555, 47617, 1, ],
    [-55727, -95612, -69300, 1, ],
    [-76235, 68475, 40437, 1, ],
    [36971, 52696, 10819, 1, ],
    [3443, 365, 96124, 1, ],
    [-65143, -42552, 81933, 1, ],
    [19182, -15554, 8060, 1, ],
    [40097, 91876, 95164, 1, ],
    [-96863, 86756, -10257, 1, ],
    [92702, -53110, 30419, 1, ],
    [-67994, -70432, -31495, 1, ],
    [40433, 4018, -4948, 1, ],
    [-20828, 88479, 75888, 1, ],
    [73001, -14504, 30636, 1, ],
    [14171, 36769, 20844, 1, ],
    [-48183, -24448, -97597, 1, ],
    [34711, 27242, 81039, 1, ],
    [-61520, -79011, 17547, 1, ],
    [-38869, -70013, 75946, 1, ],
    [1768, 55935, -75197, 1, ],
    [-44628, -58960, -43039, 1, ],
    [-92340, 14818, 13393, 1, ],
    [-15788, -95227, 6012, 1, ],
    [-7375, -54432, 50994, 1, ],
    [17327, -57963, -31356, 1, ],
    [-40402, 28793, 72524, 1, ],
    [-30164, -33801, -57258, 1, ],
    [5837, 45227, -24154, 1, ],
    [-33564, -81049, -78276, 1, ],
    [-37708, 87803, 9040, 1, ],
    [-24402, -36218, 50455, 1, ],
    [43972, 42889, -75892, 1, ],
    [-3890, 69699, 56522, 1, ],
    [-38886, -96787, 94409, 1, ],
    [-32900, -18452, 18423, 1, ],
    [99722, -68946, -68367, 1, ],
    [29326, -6527, 24064, 1, ],
    [-61703, -99568, 82163, 1, ],
    [-89928, -98630, 11836, 1, ],
    [-99824, -98017, 56104, 1, ],
    [70464, 40531, -7970, 1, ],
    [-38551, 96108, 35803, 1, ],
    [-7677, -85953, -99060, 1, ],
    [-66634, -23112, -7423, 1, ],
    [-22010, 61364, -44317, 1, ],
    [58176, 82129, -64956, 1, ],
    [-23235, -95661, -42668, 1, ],
    [96574, 54410, 94057, 1, ],
    [-13699, 11363, 45722, 1, ],
    [2035, -51469, 52720, 1, ],
    [63159, -22617, -77850, 1, ],
    [-78303, 38346, 55277, 1, ],
    [-69239, 8259, -83337, 1, ],
    [38762, -65108, -7786, 1, ],
    [-3591, 66765, -59001, 1, ],
    [-22900, 78553, -52261, 1, ],
    [-65353, 1261, 19432, 1, ],
    [-54848, 63918, -8027, 1, ],
    [-9422, -50797, 29141, 1, ],
    [-52355, 27856, -90808, 1, ],
    [-49636, -43832, 51129, 1, ],
    [95479, -71026, 8459, 1, ],
    [-8574, 28048, -20038, 1, ],
    [87084, 14526, 47474, 1, ],
    [72983, -71477, -20938, 1, ],
    [85739, 24446, 8094, 1, ],
]

loop.summarize()

print("RESULT BELOW:")
for initial_values in all_initial_values:
    terminal_values = loop.compute_terminal_values(*initial_values)
    output_str = ''
    for each in terminal_values:
        output_str += f'{each} '
    print(output_str)