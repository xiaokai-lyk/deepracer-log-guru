#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

from src.tracks.track import Track
import src.personalize.configuration.personal_track_annotations as config


class ExpeditionSuperLoopClockwiseTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Expedition Super Loop (Clockwise)"
        self._ui_description = "The pro racers will be drifting into uncharted territory on the Expedition Super Loop! This is a long track at 69.96m featuring exceptionally difficult hairpin turns and high speed straightaways. This track is sure to test even the most skillful racers."
        self._ui_length_in_m = 69.96  # metres
        self._ui_width_in_cm = 107  # centimetres   # TODO
        self._world_name = "red_star_pro_cw"
        self._track_sector_dividers = [32, 80, 120, 168]
        self._annotations = config.expedition_super_loop_cw_annotations
        self._track_width = 1.067

        self._track_waypoints = [(6.953555537007607, -2.0032757877443426), (6.940316915512085, -2.132599949836731),
                                 (6.931574989677816, -2.262305688848949), (6.920073509216309, -2.432955503463745),
                                 (6.911067962646484, -2.7339624166488647), (6.90041708946228, -3.0349154472351074),
                                 (6.8878021240234375, -3.3357924222946167), (6.872496128082275, -3.6365445852279663),
                                 (6.851777076721191, -3.936961531639099), (6.816629409790039, -4.2360169887542725),
                                 (6.763981342315674, -4.532483100891113), (6.692574977874756, -4.824960470199585),
                                 (6.596072435379028, -5.1100804805755615), (6.465707778930664, -5.381173372268677),
                                 (6.283754110336304, -5.619956970214844), (6.037519454956055, -5.791036128997803),
                                 (5.748953342437744, -5.870548963546753), (5.4507904052734375, -5.840290546417236),
                                 (5.1704020500183105, -5.731826543807983), (4.9081714153289795, -5.583988666534424),
                                 (4.65495491027832, -5.421026706695557), (4.403064966201782, -5.256078004837036),
                                 (4.160675048828125, -5.077383995056152), (3.920612096786499, -4.895570993423462),
                                 (3.68079149723053, -4.713436841964722), (3.442054510116577, -4.5298871994018555),
                                 (3.204648971557617, -4.344617009162903), (2.9678984880447388, -4.158509850502014),
                                 (2.7322030067443848, -3.9710720777511597), (2.4979355335235596, -3.7818491458892822),
                                 (2.266058564186096, -3.5897120237350464), (2.0391449332237244, -3.3917479515075684),
                                 (1.818962037563324, -3.1863194704055786), (1.6126495599746704, -2.9671905040740967),
                                 (1.444264441728592, -2.71812641620636), (1.3402898907661438, -2.4363170862197876),
                                 (1.3215706646442413, -2.137124538421631), (1.4153554141521454, -1.8530519604682922),
                                 (1.6119499802589417, -1.6270529627799988), (1.873351514339447, -1.479988008737564),
                                 (2.1681095361709595, -1.426539957523346), (2.4592409133911133, -1.4967331886291504),
                                 (2.7549275159835815, -1.5334405303001404), (3.039764404296875, -1.4402459263801575),
                                 (3.27068293094635, -1.2503913044929504), (3.3756664991378758, -0.9727489650249548),
                                 (3.3219380378723145, -0.6786083579063416), (3.1904590129852295, -0.4079502001404762),
                                 (3.030148506164551, -0.1533091440796852), (2.8368149995803833, 0.07733374834060669),
                                 (2.6209670305252075, 0.2872692421078682), (2.412004590034485, 0.5040408447384834),
                                 (2.2287579774856567, 0.7424752414226532), (2.1000455021858215, 0.9948582649230957),
                                 (2.1216520071029663, 1.310239017009735), (2.3352404832839966, 1.5409075021743774),
                                 (2.611822009086609, 1.6254899501800537), (2.9097700119018555, 1.6672430634498596),
                                 (3.207969546318054, 1.7072540521621704), (3.494476556777954, 1.797919511795044),
                                 (3.747326970100403, 1.9590574502944946), (3.9212764501571655, 2.202076017856598),
                                 (3.9816814661026, 2.4953064918518066), (3.947209596633911, 2.7934244871139526),
                                 (3.8164533376693726, 3.06273090839386), (3.5949209928512573, 3.2642884254455566),
                                 (3.322519898414612, 3.3908259868621826), (3.0295485258102417, 3.4588475227355957),
                                 (2.7297195196151733, 3.4850621223449707), (2.4295934438705444, 3.467151403427124),
                                 (2.1385874748230047, 3.391322016716005), (1.8535929918289185, 3.2940385341644287),
                                 (1.5686615109443665, 3.1965675354003906), (1.2838035225868225, 3.098883032798767),
                                 (0.9990096986293793, 3.001009464263916), (0.7142336070537567, 2.903085947036743),
                                 (0.4294431060552597, 2.8052040338516235), (0.144663299433887, 2.7072914838790894),
                                 (-0.14006922580301762, 2.609241008758545), (-0.42472819983959853, 2.510977029800413),
                                 (-0.7092883586883545, 2.4124280214309692), (-0.9937455952167511, 2.3135825395584106),
                                 (-1.2781195044517517, 2.2144969701766968), (-1.5624285340309143, 2.1152244806289673),
                                 (-1.8466814756393366, 2.015792489051821), (-2.130827009677887, 1.9160534739494324),
                                 (-2.4148058891296387, 1.8158409595489502), (-2.698536515235901, 1.7149280309677124),
                                 (-2.981945037841797, 1.6131155490875244), (-3.2649879455566406, 1.5102909803390503),
                                 (-3.547456979751587, 1.4059014022350311), (-3.8267844915390015, 1.2935166954994202),
                                 (-4.079706430435181, 1.1313326954841614), (-4.286390542984012, 0.9132440686225813),
                                 (-4.412045598030088, 0.6419639885425632), (-4.438278436660767, 0.34290455281734467),
                                 (-4.38130795955658, 0.04812920093536377), (-4.234914064407349, -0.21341319382190704),
                                 (-4.003291010856628, -0.40404554829001427), (-3.7231149673461914, -0.512868408113718),
                                 (-3.425444483757019, -0.5564972087740898), (-3.1245384216308594, -0.5511380331590772),
                                 (-2.8274190425872803, -0.5033605387434363), (-2.5477454662323, -0.39457493275403976),
                                 (-2.27681303024292, -0.2631485015153885), (-1.9986779689788818, -0.14797550439834595),
                                 (-1.7085995078086853, -0.06847275793552399),
                                 (-1.4087889790534973, -0.057888612151145935),
                                 (-1.1305416524410248, -0.16685210168361664),
                                 (-0.9079060852527618, -0.3674914427101612), (-0.7726753503084183, -0.6328622400760651),
                                 (-0.810539111495018, -0.927367091178894), (-0.979390561580658, -1.17512047290802),
                                 (-1.1957714259624481, -1.3842474818229675), (-1.3300245106220214, -1.6514675021171505),
                                 (-1.3697651326656342, -1.9488880038261414), (-1.3291771709918976, -2.2465169429779053),
                                 (-1.2233891785144806, -2.5279805660247803), (-1.0710665583610535, -2.787427067756653),
                                 (-0.9073505103588104, -3.038462996482849), (-0.847469687461853, -3.3325854539871216),
                                 (-0.8547482043504715, -3.633172392845154), (-0.9230661690235138, -3.9259119033813477),
                                 (-1.0533945262432098, -4.196689963340759), (-1.242574781179428, -4.430092096328735),
                                 (-1.4799554944038391, -4.614397287368774), (-1.749921977519989, -4.74698805809021),
                                 (-2.038186013698578, -4.833017826080322), (-2.337088465690613, -4.865729093551636),
                                 (-2.6358425617218018, -4.834390163421631), (-2.9147835969924927, -4.724140882492065),
                                 (-3.142717957496643, -4.529601335525513), (-3.2973819971084595, -4.272521018981934),
                                 (-3.3829904794692993, -3.984346032142639), (-3.4736465215682983, -3.697438597679138),
                                 (-3.6033380031585693, -3.4259119033813477), (-3.7693065404891968, -3.1749069690704346),
                                 (-3.965975046157837, -2.947080969810486), (-4.187850475311279, -2.743707537651062),
                                 (-4.429556369781494, -2.5642740726470947), (-4.686848878860474, -2.407967984676361),
                                 (-4.957162618637085, -2.2754494547843933), (-5.237262487411499, -2.1655160188674927),
                                 (-5.529191493988037, -2.091633975505829), (-5.819885492324829, -2.013022482395172),
                                 (-6.109105825424194, -1.9291595220565796), (-6.395982980728149, -1.8376214504241943),
                                 (-6.678714990615845, -1.734063982963562), (-6.948265075683594, -1.6007595658302307),
                                 (-7.135745048522949, -1.3695335388183594), (-7.2361109256744385, -1.0863554179668427),
                                 (-7.28110146522522, -0.7889012396335602), (-7.289146423339844, -0.4880272001028061),
                                 (-7.271159410476685, -0.18748565018177032), (-7.232422828674316, 0.11110895127058029),
                                 (-7.177873373031616, 0.40723659098148346), (-7.109678506851196, 0.700531542301178),
                                 (-7.027554035186768, 0.9902344942092896), (-6.931075572967529, 1.2754470109939575),
                                 (-6.814818382263184, 1.5531070232391357), (-6.669225454330444, 1.8165475130081177),
                                 (-6.49602198600769, 2.0627130270004272), (-6.2975523471832275, 2.2890209555625916),
                                 (-6.07580304145813, 2.4925570487976074), (-5.83298397064209, 2.670415997505188),
                                 (-5.572525978088377, 2.8212809562683114), (-5.296924829483032, 2.94226610660553),
                                 (-5.011700630187988, 3.0387895107269287), (-4.725564956665039, 3.1326680183410645),
                                 (-4.439396619796753, 3.2264434099197388), (-4.153187036514282, 3.320096969604492),
                                 (-3.866950511932373, 3.41366446018219), (-3.580694556236267, 3.5071738958358765),
                                 (-3.294412612915039, 3.600603461265564), (-3.0080984830856323, 3.6939345598220825),
                                 (-2.721747040748596, 3.7871508598327637), (-2.4353549480438232, 3.8802446126937866),
                                 (-2.1489239931106567, 3.973215103149414), (-1.862452507019043, 4.066061019897461),
                                 (-1.5759379863739014, 4.158777594566345), (-1.289394497871398, 4.2514015436172485),
                                 (-1.0028408467769623, 4.343993902206421), (-0.7162621021270752, 4.436509490013123),
                                 (-0.4296411871910095, 4.528894424438477), (-0.1429616529494524, 4.621097087860107),
                                 (0.14385623764246702, 4.712868690490723), (0.4308948367834091, 4.8039469718933105),
                                 (0.7180704474449158, 4.894593000411987), (1.0052867233753204, 4.985109329223633),
                                 (1.292437493801117, 5.075832843780518), (1.57959645986557, 5.166530609130859),
                                 (1.8668989539146423, 5.25677490234375), (2.154359996318817, 5.346511125564575),
                                 (2.44200599193573, 5.435651779174805), (2.7298669815063477, 5.52409815788269),
                                 (3.0180410146713257, 5.611517906188965), (3.3067615032196045, 5.697112321853638),
                                 (3.596458077430725, 5.7793333530426025), (3.8885955810546875, 5.8521623611450195),
                                 (4.188632011413574, 5.865318059921265), (4.486043691635132, 5.82005500793457),
                                 (4.7767109870910645, 5.7417309284210205), (5.060539960861206, 5.641248941421509),
                                 (5.338674068450928, 5.525859117507935), (5.611742973327637, 5.398936986923218),
                                 (5.87873911857605, 5.259990215301514), (6.094139099121094, 5.051473379135132),
                                 (6.24181056022644, 4.789742469787598), (6.332545042037964, 4.503074645996094),
                                 (6.354149580001831, 4.203406333923341), (6.434597015380859, 3.9173760414123535),
                                 (6.614871501922607, 3.676652431488037), (6.8193464279174805, 3.455775022506714),
                                 (7.011923551559448, 3.2255594730377197), (7.1444411277771, 2.9557039737701416),
                                 (7.226306438446045, 2.666182518005371), (7.27443265914917, 2.3690154552459717),
                                 (7.29197359085083, 2.0685240030288696), (7.277885437011719, 1.767823040485382),
                                 (7.252377510070801, 1.4677634835243225), (7.226216554641724, 1.167756974697113),
                                 (7.200679540634155, 0.8676995635032654), (7.175274133682251, 0.5676316618919373),
                                 (7.149756669998169, 0.2675726041197777), (7.124224424362183, -0.03248497936874628),
                                 (7.098731517791748, -0.3325451463460922), (7.07317590713501, -0.6326019465923313),
                                 (7.0475006103515625, -0.9326519668102264), (7.022186040878296, -1.232721984386444),
                                 (6.997573614120483, -1.5328315496444702), (6.971003532409668, -1.8328315019607544),
                                 (6.953555537007607, -2.0032757877443426)]
