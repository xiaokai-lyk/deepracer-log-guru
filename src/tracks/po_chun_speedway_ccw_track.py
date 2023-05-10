#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

from src.tracks.track import Track
import src.personalize.configuration.personal_track_annotations as config


class PoChunSpeedwayCounterClockwiseTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Po-Chun Speedway (Counter Clockwise)"
        self._ui_description = "Po-Chun Speedway is a short track (68.68m) featuring a simple oval track paired with a dragstrip, and single hairpin. It is named in honor of the 2020 AWS DeepRacer League Champion from NCTU CGI Taiwan."
        self._ui_length_in_m = 68.68  # metres
        self._ui_width_in_cm = 107  # centimetres   # TODO
        self._world_name = "penbay_open_ccw"
        self._track_sector_dividers = [62, 91, 121, 154, 184]
        self._annotations = config.po_chun_speedway_ccw_annotations
        self._track_width = 1.066

        self._track_waypoints = [(-0.6727288113748293, -4.261760196357879), (-0.5427288115024567, -4.261765956878662),
                                 (-0.41272881150245666, -4.261765956878662), (-0.24142305552959442, -4.261765956878662),
                                 (0.05988187529146671, -4.261759877204895), (0.3611871004104614, -4.26175594329834),
                                 (0.662492573261261, -4.261754035949707), (0.9637983441352844, -4.261754035949707),
                                 (1.2651039958000254, -4.261754989624023), (1.5664100050926208, -4.261757969856262),
                                 (1.8677160143852234, -4.261762619018555), (2.169021487236023, -4.261765003204346),
                                 (2.4703269004821777, -4.261756539344788), (2.7716320753097534, -4.261736035346985),
                                 (3.072937488555908, -4.261713981628418), (3.374243974685669, -4.261752128601074),
                                 (3.675552487373352, -4.261863827705383), (3.9768584966659546, -4.2619019746780396),
                                 (4.278155565261841, -4.261481404304504), (4.579463005065918, -4.261572003364563),
                                 (4.8806915283203125, -4.2578253746032715), (5.181959867477417, -4.254327416419983),
                                 (5.483231067657471, -4.258774518966675), (5.784441947937012, -4.266305446624756),
                                 (6.085649490356445, -4.2740079164505005), (6.386899471282959, -4.2797510623931885),
                                 (6.6881959438323975, -4.2817264795303345), (6.9894773960113525, -4.278228998184204),
                                 (7.290585517883301, -4.267500996589661), (7.591221570968628, -4.247570037841797),
                                 (7.890862464904785, -4.2160950899124146), (8.188625812530518, -4.170198082923889),
                                 (8.483022212982178, -4.106245994567871), (8.77152156829834, -4.019588470458984),
                                 (9.049848556518555, -3.9045119285583496), (9.310968399047852, -3.7546104192733765),
                                 (9.544243812561035, -3.5644270181655884), (9.736420154571533, -3.332915425300598),
                                 (9.876531600952148, -3.06666898727417), (9.961713790893555, -2.77800452709198),
                                 (9.997364044189453, -2.4790204763412476), (9.992513656616211, -2.1778650283813477),
                                 (9.956003665924072, -1.8788430094718933), (9.894077777862549, -1.5841249823570251),
                                 (9.812457084655762, -1.29424250125885), (9.66081428527832, -1.0337065160274506),
                                 (9.488127708435059, -0.78695909678936), (9.288923263549805, -0.561100609600544),
                                 (9.060757637023926, -0.36464982852339745), (8.804934024810791, -0.20598824322223663),
                                 (8.527814388275146, -0.08826449513435364), (8.238211631774902, -0.005510240793228149),
                                 (7.943350076675415, 0.05637580156326294), (7.647890567779541, 0.11541084945201874),
                                 (7.356168508529663, 0.19046875834465027), (7.075143098831177, 0.29854194819927216),
                                 (6.814655065536499, 0.4493507123552263), (6.582998037338257, 0.6415981501340866),
                                 (6.382713317871094, 0.8664526641368866), (6.211200475692749, 1.1140539646148682),
                                 (6.063836574554443, 1.3767935037612915), (5.936128616333008, 1.6496694684028625),
                                 (5.824274063110352, 1.929423987865448), (5.725372076034546, 2.214029550552368),
                                 (5.637132406234741, 2.502124071121216), (5.557794570922852, 2.792796015739441),
                                 (5.4859678745269775, 3.0854159593582153), (5.420738458633423, 3.3795734643936157),
                                 (5.3604021072387695, 3.674780488014221), (5.307320833206177, 3.971400022506714),
                                 (5.255425453186035, 4.268174409866333), (5.171319961547852, 4.557399034500122),
                                 (5.056972503662109, 4.836001634597778), (4.907825469970703, 5.097540855407715),
                                 (4.719061613082886, 5.331911563873291), (4.487469673156738, 5.523720026016235),
                                 (4.215168476104736, 5.650381088256836), (3.9173269271850586, 5.685263395309448),
                                 (3.625952959060669, 5.614634990692139), (3.373075485229492, 5.452829122543335),
                                 (3.171789050102234, 5.229472398757935), (3.019010543823242, 4.970172882080078),
                                 (2.907155990600586, 4.690608978271484), (2.828793525695801, 4.3997814655303955),
                                 (2.765389084815979, 4.105362057685852), (2.6939600706100464, 3.8126490116119385),
                                 (2.6243560314178467, 3.519492983818054), (2.5559974908828735, 3.2260444164276123),
                                 (2.487694561481476, 2.9325824975967407), (2.4175084233283997, 2.6395665407180786),
                                 (2.343197524547577, 2.3475719690322876), (2.2633349895477295, 2.057048499584198),
                                 (2.1776190400123596, 1.7681970000267029), (2.086601972579956, 1.4809705018997192),
                                 (1.9911779761314392, 1.1951764822006226), (1.8922170400619507, 0.9105875492095947),
                                 (1.7906580567359924, 0.6269115954637527), (1.6768489480018616, 0.34800703823566437),
                                 (1.5417359471321106, 0.07877694815397263), (1.375271588563919, -0.17161869257688522),
                                 (1.15410515666008, -0.37502243742346764), (0.8856999278068542, -0.5099009610712528),
                                 (0.5925252735614777, -0.5772204324603081), (0.2920594960451126, -0.5973111353814602),
                                 (-0.009182423586025834, -0.5928616132587194),
                                 (-0.31029094755649567, -0.5819892752915621),
                                 (-0.6115384697914124, -0.5761552453041077), (-0.9127890169620514, -0.5704887192696333),
                                 (-1.2135834693908691, -0.5551804481074214), (-1.5122205018997192, -0.5153579474426806),
                                 (-1.8065675497055054, -0.45146988332271576), (-2.0903285145759583, -0.350995734333992),
                                 (-2.347411513328551, -0.19532895088195884),
                                 (-2.5437334775924683, 0.031190089881420135), (-2.6491819620132446, 0.3120837062597275),
                                 (-2.6779699325561523, 0.6115317344665527), (-2.661715030670166, 0.9122658967971775),
                                 (-2.622437000274658, 1.2109695076942444), (-2.573083519935608, 1.508201539516449),
                                 (-2.5218159556388855, 1.8051134943962097), (-2.4741424918174744, 2.102620005607605),
                                 (-2.434129536151886, 2.401245951652527), (-2.4043270349502563, 2.701111078262329),
                                 (-2.406980514526367, 3.0022435188293457), (-2.4207990169525146, 3.30322802066803),
                                 (-2.441581964492798, 3.6038070917129517), (-2.4723209142684937, 3.903531551361084),
                                 (-2.5107465386390686, 4.202370643615723), (-2.5568959712982178, 4.500107049942017),
                                 (-2.612674593925476, 4.796196460723877), (-2.6756625175476074, 5.090838432312012),
                                 (-2.747232437133789, 5.38350248336792), (-2.827921509742737, 5.673794984817505),
                                 (-2.9156274795532227, 5.9620466232299805), (-3.0483914613723755, 6.232008695602417),
                                 (-3.2063599824905396, 6.4884703159332275), (-3.3874534368515015, 6.72915244102478),
                                 (-3.593221426010132, 6.949068784713745), (-3.824547052383423, 7.141828536987305),
                                 (-4.080575466156006, 7.300200939178467), (-4.358578443527222, 7.415583610534668),
                                 (-4.652133941650391, 7.481949329376221), (-4.952775955200195, 7.495491981506348),
                                 (-5.251155376434326, 7.456039667129517), (-5.538953065872192, 7.367794990539551),
                                 (-5.810091495513916, 7.236910104751587), (-6.060878276824951, 7.070228576660156),
                                 (-6.289544582366943, 6.874241590499878), (-6.495656490325928, 6.654613971710205),
                                 (-6.67950701713562, 6.41601300239563), (-6.841804504394531, 6.162233352661133),
                                 (-6.983479976654053, 5.896380424499512), (-7.105449438095093, 5.621113061904907),
                                 (-7.207826852798462, 5.3384034633636475), (-7.290602445602417, 5.0483644008636475),
                                 (-7.365024089813232, 4.755202531814575), (-7.442820072174072, 4.463300466537476),
                                 (-7.523991584777832, 4.17266058921814), (-7.6085381507873535, 3.883281946182251),
                                 (-7.696443796157837, 3.5951579809188843), (-7.78537917137146, 3.3074194192886353),
                                 (-7.8737101554870605, 3.0194555521011353), (-7.9614362716674805, 2.7312660217285156),
                                 (-8.048557996749878, 2.4428519010543823), (-8.135090589523317, 2.1542180776596034),
                                 (-8.22156810760498, 1.8655635118484497), (-8.308249711990356, 1.5769850015640259),
                                 (-8.395094633102417, 1.2884650230407715), (-8.481954574584961, 0.9999508559703827),
                                 (-8.568812847137451, 0.7114363014698029), (-8.655672550201416, 0.42292189598083496),
                                 (-8.742536067962646, 0.13440883718430996), (-8.830108165740967, -0.15388999806600623),
                                 (-8.91724157333374, -0.44232161343097687), (-9.00410795211792, -0.7308340072631836),
                                 (-9.090854167938232, -1.0193826854228973), (-9.177350521087646, -1.3080059885978699),
                                 (-9.26429796218872, -1.5964934825897217), (-9.352263450622559, -1.8846725225448608),
                                 (-9.440130233764648, -2.1728785037994385), (-9.52503490447998, -2.461964964866638),
                                 (-9.613758563995361, -2.7499120235443115), (-9.701560974121094, -3.0381405353546143),
                                 (-9.784660339355469, -3.3277535438537598), (-9.859379291534424, -3.61963152885437),
                                 (-9.92163372039795, -3.914404511451721), (-9.962469577789307, -4.21284556388855),
                                 (-9.987803936004639, -4.513065338134766), (-9.99890422821045, -4.81411600112915),
                                 (-9.990517139434814, -5.115253448486328), (-9.959575176239014, -5.414888143539429),
                                 (-9.90441083908081, -5.711017608642578), (-9.82174825668335, -6.000604152679443),
                                 (-9.706324100494385, -6.278738498687744), (-9.554830551147461, -6.5388500690460205),
                                 (-9.363844871520996, -6.771458387374878), (-9.132537364959717, -6.963716983795166),
                                 (-8.879008769989014, -7.126331090927124), (-8.610604286193848, -7.2629759311676025),
                                 (-8.32959508895874, -7.371350049972534), (-8.038633823394775, -7.449054002761841),
                                 (-7.7405478954315186, -7.491698980331421), (-7.439494609832764, -7.493931531906128),
                                 (-7.141908168792725, -7.448947906494141), (-6.8572678565979, -7.351420879364014),
                                 (-6.59694766998291, -7.200623989105225), (-6.371587038040161, -7.001312017440796),
                                 (-6.187023401260376, -6.763595104217529), (-6.043107986450195, -6.499178647994995),
                                 (-5.910693407058716, -6.228633403778076), (-5.772217035293579, -5.961036443710327),
                                 (-5.6286585330963135, -5.6961350440979), (-5.4757280349731445, -5.436559438705444),
                                 (-5.309916019439697, -5.185019493103027), (-5.1293785572052, -4.943895578384399),
                                 (-4.925506830215454, -4.7222301959991455), (-4.697670936584473, -4.525363922119141),
                                 (-4.440497636795044, -4.3691980838775635), (-4.157896041870117, -4.2658209800720215),
                                 (-3.8566675186157227, -4.265198588371277), (-3.5556814670562744, -4.262607932090759),
                                 (-3.2546329498291016, -4.260531544685364), (-2.9532374143600464, -4.261255502700806),
                                 (-2.6518514156341553, -4.261902451515198), (-2.3505290746688843, -4.262041091918945),
                                 (-2.0492465496063232, -4.261852860450745), (-1.7479559779167175, -4.261733055114746),
                                 (-1.4466549754142761, -4.261695027351379), (-1.1453449726104736, -4.261724948883057),
                                 (-0.8440361618995595, -4.261752605438232), (-0.6727288113748293, -4.261760196357879)]
