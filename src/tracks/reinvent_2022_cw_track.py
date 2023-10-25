#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

from src.tracks.track import Track
import src.personalize.configuration.personal_track_annotations as config


class Reinvent2022ClockwiseTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "2022 re:Invent Championship (Clockwise)"
        self._ui_description = "Get ready to rev your engines on the official 2022 re:Invent Championship track! This is an intensely difficult track (35.87 m) featuring a technical chicane section that will challenge even the most skilled developers."
        self._ui_length_in_m = 35.87  # metres
        self._ui_width_in_cm = 95  # centimetres
        self._world_name = "2022_reinvent_champ_cw"
        self._track_sector_dividers = [43, 80]
        self._annotations = config.reinvent_2022_cw_annotations
        self._track_width = 0.95

        self._track_waypoints = [(0.01685067967659376, 1.1330461167634183), (0.10454194992780445, 1.037076115608218),
                                 (0.19108544565858432, 0.9400698099023651), (0.3063818905502558, 0.8108344227075577),
                                 (0.5076930373907089, 0.584124356508255), (0.7088999003171921, 0.3573188427835703),
                                 (0.9101405441761017, 0.13054199516773224), (1.1109170317649841, -0.09663845598697662),
                                 (1.3109925091266632, -0.3244275604374707), (1.510398030281067, -0.5527989640831947),
                                 (1.7115260362625122, -0.779676765203476), (1.9158819317817688, -1.0037544667720795),
                                 (2.127041459083557, -1.2212917506694794), (2.35785448551178, -1.4178684949874878),
                                 (2.6153459548950195, -1.5775030255317688), (2.9020979404449463, -1.6740959882736206),
                                 (3.192330002784729, -1.7584999799728394), (3.410485029220581, -1.9660694599151611),
                                 (3.5636454820632935, -2.2276010513305664), (3.6904104948043823, -2.5030659437179565),
                                 (3.802172064781189, -2.7848669290542603), (3.8883113861083984, -3.075444459915161),
                                 (3.9256519079208374, -3.3758625984191895), (3.857689619064331, -3.6687514781951904),
                                 (3.628520965576172, -3.8595250844955444), (3.3312785625457764, -3.9159170389175415),
                                 (3.0283209085464478, -3.9232853651046753), (2.7338016033172643, -3.858665585517884),
                                 (2.5047554969787598, -3.663868546485901), (2.3042269945144653, -3.436737537384033),
                                 (2.0655285716056824, -3.250208020210266), (1.7853264808654785, -3.1376020908355713),
                                 (1.4848524928092957, -3.1510039567947388), (1.2191407084465027, -3.29349946975708),
                                 (1.0140118598937988, -3.5154515504837036), (0.7995970845222473, -3.7257325649261475),
                                 (0.5195947587490082, -3.8406310081481934), (0.22013694792985916, -3.8849860429763794),
                                 (-0.0791160985827446, -3.842719554901123), (-0.32070594653487206, -3.665432929992676),
                                 (-0.40669136866927147, -3.3779269456863403), (-0.3660818636417389, -3.077723979949951),
                                 (-0.2731740474700928, -2.7888084650039673), (-0.1811501830816269, -2.4999635219573975),
                                 (-0.10437200963497162, -2.2066839933395386),
                                 (-0.05370424687862396, -1.9078789949417114),
                                 (-0.04975371062755585, -1.6051074862480164),
                                 (-0.12047268450260162, -1.3112254738807678),
                                 (-0.27104945853352547, -1.048856794834137),
                                 (-0.47022343426942825, -0.8207091391086578),
                                 (-0.7124057114124298, -0.6395276188850403), (-0.9999120831489563, -0.5500769801437855),
                                 (-1.2934255003929138, -0.6115724742412567), (-1.5459460020065308, -0.779325932264328),
                                 (-1.7553704977035522, -0.99831223487854), (-1.9025014638900757, -1.2629244923591614),
                                 (-1.9807295203208923, -1.5556524991989136), (-2.0042914748191833, -1.8578130006790161),
                                 (-1.9950765371322632, -2.160830020904541), (-1.9745920300483704, -2.4633378982543945),
                                 (-1.9683764576911926, -2.766396999359131), (-2.017058491706848, -3.0650094747543335),
                                 (-2.14520400762558, -3.339360475540161), (-2.316781997680664, -3.588989496231079),
                                 (-2.539884567260742, -3.7932724952697754), (-2.822121500968933, -3.8981685638427734),
                                 (-3.1190404891967773, -3.8501704931259155), (-3.3754725456237793, -3.6891149282455444),
                                 (-3.591495990753174, -3.4761509895324707), (-3.759330630302429, -3.2240179777145386),
                                 (-3.855846643447876, -2.936893939971924), (-3.894473910331726, -2.636250495910644),
                                 (-3.891848087310791, -2.3330575227737427), (-3.85984206199646, -2.0315550565719604),
                                 (-3.8061275482177734, -1.7331575155258179), (-3.735764503479004, -1.4382449984550476),
                                 (-3.6522023677825928, -1.1467989683151245), (-3.5579434633255005, -0.8586345314979553),
                                 (-3.4547725915908813, -0.5735454112291336), (-3.343720555305481, -0.29143815487623215),
                                 (-3.2113959789276123, -0.018747098743915558),
                                 (-3.058645009994507, 0.24312346291844733), (-2.9001810550689697, 0.501609206199646),
                                 (-2.758821964263916, 0.7696676254272461), (-2.6881719827651978, 1.0627945065498352),
                                 (-2.774464964866638, 1.349343478679657), (-3.0156389474868774, 1.5270600318908691),
                                 (-3.304600954055786, 1.6183845400810242), (-3.5905039310455322, 1.7184150218963623),
                                 (-3.8185924291610718, 1.9130929708480835), (-3.903972029685974, 2.20158052444458),
                                 (-3.920802593231201, 2.5043104887008667), (-3.92767596244812, 2.807428002357483),
                                 (-3.9173271656036377, 3.1104239225387573), (-3.873715877532959, 3.4103184938430786),
                                 (-3.758816957473755, 3.6895145177841187), (-3.5244959592819214, 3.875788450241089),
                                 (-3.2266565561294556, 3.927023410797119), (-2.9241185188293457, 3.908042550086975),
                                 (-2.62819242477417, 3.8442219495773315), (-2.3569549322128296, 3.71036159992218),
                                 (-2.1209999322891235, 3.520527482032776), (-1.9106189608573914, 3.3023040294647217),
                                 (-1.7090685367584229, 3.0758060216903687), (-1.5080680251121545, 2.8488199710845974),
                                 (-1.3072496354579926, 2.621672511100769), (-1.1063501834869385, 2.3945975303649902),
                                 (-0.9053516983985901, 2.167609930038452), (-0.7042564749717712, 1.9407075643539429),
                                 (-0.503077358007431, 1.7138790488243103), (-0.30175267718732357, 1.4871800541877747),
                                 (-0.09996715188026428, 1.2608924508094788), (0.01685067967659376, 1.1330461167634183)]
