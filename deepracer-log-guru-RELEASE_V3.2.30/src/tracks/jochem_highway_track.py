#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

import src.personalize.configuration.personal_track_annotations as config
from src.tracks.track import Track


class JochemHighwayTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Jochem Highway"
        self._ui_description = "Time to put your developer skills to the test on the Jochem Highway named after AWS Community member and re:Invent 2021 finalist, Jochem Lugtenburg. This incredibly difficult track features no shortage of technical sections from double 90 degree turns to unforgiving hairpin sections. The Jochem Highway will surely deliver plenty of off tracks to even the most skilled developers."
        self._ui_length_in_m = 99.99  # metres     (NOT STATED)
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "2022_august_pro"
        self._track_sector_dividers = [33, 70, 92, 127, 174]
        self._annotations = config.jochem_highway_annotations
        self._track_width = 1.067

        self._track_waypoints = [(7.216928482055664, -5.209843158721924), (7.224047899246216, -4.908241510391235),
                                 (7.221474885940552, -4.606546640396118), (7.215227365493774, -4.304901123046875),
                                 (7.211925506591797, -4.003215074539185), (7.217139959335327, -3.701570510864258),
                                 (7.2189390659332275, -3.399988532066345), (7.215593576431274, -3.098297595977783),
                                 (7.212994813919067, -2.7965980768203735), (7.211113452911377, -2.494894027709961),
                                 (7.2097556591033936, -2.1931869983673096), (7.208656549453735, -1.8914784789085388),
                                 (7.207937479019165, -1.5897694826126099), (7.207696914672852, -1.2880594730377197),
                                 (7.207672119140625, -0.986349493265152), (7.20774507522583, -0.6846393942832947),
                                 (7.208126068115234, -0.3829295039176941), (7.209033489227295, -0.08122077956795692),
                                 (7.210091829299927, 0.22048749774694443), (7.211150407791138, 0.5221957862377167),
                                 (7.212207078933716, 0.8239040374755859), (7.213265657424927, 1.125612497329712),
                                 (7.214324712753296, 1.4273210167884827), (7.215369462966919, 1.7290289998054504),
                                 (7.216236114501953, 2.0307379961013794), (7.2166619300842285, 2.3324475288391113),
                                 (7.216647148132324, 2.6341580152511597), (7.21640157699585, 2.935867428779602),
                                 (7.21640157699585, 2.935867428779602), (7.215672016143799, 3.2375770807266235),
                                 (7.2075886726379395, 3.5391775369644165), (7.209341526031494, 3.840824007987976),
                                 (7.215846538543701, 4.142462491989136), (7.216858863830566, 4.44415807723999),
                                 (7.205984592437744, 4.745635986328125), (7.17514705657959, 5.045680999755859),
                                 (7.116741895675659, 5.341560363769531), (7.0238494873046875, 5.6283814907073975),
                                 (6.892672777175903, 5.899808645248413), (6.723068952560425, 6.148624658584595),
                                 (6.501363039016724, 6.35247015953064), (6.2488579750061035, 6.517101526260376),
                                 (5.9776999950408936, 6.649060010910034), (5.694807529449463, 6.753648519515991),
                                 (5.403666973114014, 6.832471132278442), (5.106539487838745, 6.8841798305511475),
                                 (4.805575370788574, 6.89878249168396), (4.505034685134888, 6.873337984085083),
                                 (4.207479476928711, 6.8238911628723145), (3.9140759706497192, 6.753790616989136),
                                 (3.6259225606918335, 6.66448712348938), (3.344057083129883, 6.557023525238037),
                                 (3.0689074993133545, 6.433353900909424), (2.8013570308685303, 6.293983459472656),
                                 (2.5477374792099, 6.131885051727295), (2.3513124585151672, 5.904381513595581),
                                 (2.2442389726638794, 5.624154090881348), (2.243149518966675, 5.323873996734619),
                                 (2.322453022003174, 5.033336400985718), (2.4484934210777283, 4.7594153881073),
                                 (2.6011070013046265, 4.499229431152344), (2.767071008682251, 4.247284889221191),
                                 (2.9373990297317505, 3.998253107070923), (3.0884710550308228, 3.7390400171279907),
                                 (3.1384090185165405, 3.4418774843215942), (3.138700008392334, 3.140526533126831),
                                 (3.079932451248169, 2.8452435731887817), (2.9486600160598755, 2.574697494506836),
                                 (2.741844415664673, 2.3567134737968445), (2.479641556739807, 2.2093934416770935),
                                 (2.1897079944610596, 2.1277405619621277), (1.8898645043373108, 2.0966910123825073),
                                 (1.5895389914512634, 2.1152339577674866), (1.2960119843482971, 2.0541444420814514),
                                 (1.03764146566391, 1.8996695280075073), (0.8165287673473358, 1.69503253698349),
                                 (0.6255071982741356, 1.4616385102272034), (0.4507311265915632, 1.2157250046730042),
                                 (0.27537401765584946, 0.9702292680740356), (0.083969846367836, 0.7371826320886612),
                                 (-0.1353078931570053, 0.5303080156445503), (-0.35752098727971315, 0.32625829987227917),
                                 (-0.5743972584605217, 0.11651554703712463),
                                 (-0.7920087426900864, -0.09245729446411133),
                                 (-1.0211926698684692, -0.28851960599422455),
                                 (-1.2684710621833801, -0.4611809994094074), (-1.528763473033905, -0.6136277765035629),
                                 (-1.7953389286994934, -0.7548324912786484), (-2.0531709790229797, -0.9114785045385361),
                                 (-2.307997465133667, -1.0730098187923431), (-2.563710927963257, -1.2331288754940033),
                                 (-2.8229600191116333, -1.3874392807483673), (-3.0876200199127197, -1.5322544574737549),
                                 (-3.359439492225647, -1.6630609631538391), (-3.6407899856567383, -1.7716980576515198),
                                 (-3.9334338903427124, -1.843695044517517), (-4.234079360961914, -1.8501759767532349),
                                 (-4.514417409896851, -1.746175467967987), (-4.720096588134766, -1.5279124975204468),
                                 (-4.843215465545654, -1.2544030547142029), (-4.838584661483765, -0.9555122554302216),
                                 (-4.716463088989258, -0.6809590607881546), (-4.534330129623413, -0.4408188425004482),
                                 (-4.326100468635559, -0.22258714586496353), (-4.106452107429504, -0.01576155424118042),
                                 (-3.885188937187195, 0.18935079127550125), (-3.6691774129867554, 0.3999545844271779),
                                 (-3.467963457107544, 0.6246230006217957), (-3.296038508415222, 0.8721555769443512),
                                 (-3.1799360513687134, 1.149680495262146), (-3.1539034843444824, 1.4487285017967224),
                                 (-3.2697694301605225, 1.723061978816986), (-3.508713483810425, 1.9035890698432922),
                                 (-3.7912089824676514, 2.0082370042800903), (-4.084344387054443, 2.079459011554718),
                                 (-4.379456281661987, 2.1415469646453857), (-4.6794655323028564, 2.1723700165748596),
                                 (-4.9810631275177, 2.172530949115753), (-5.281261205673218, 2.1434019804000854),
                                 (-5.577366590499878, 2.086089015007019), (-5.8672144412994385, 2.002687990665436),
                                 (-6.148751974105835, 1.8944739699363708), (-6.418118000030518, 1.7596439719200134),
                                 (-6.64424204826355, 1.5611949563026428), (-6.816252946853638, 1.3140285015106201),
                                 (-6.941140174865723, 1.0396597385406494), (-7.031402349472046, 0.751893550157547),
                                 (-7.099157094955444, 0.45793895423412323), (-7.1553308963775635, 0.16150860488414764),
                                 (-7.190817356109619, -0.1373736783862114), (-7.203735113143921, -0.43880705535411835),
                                 (-7.214643478393555, -0.7403185665607452), (-7.221787452697754, -1.0419424772262573),
                                 (-7.225583076477051, -1.3436269760131836), (-7.224649429321289, -1.6453310251235962),
                                 (-7.217939853668213, -1.9469619989395142), (-7.2048234939575195, -2.2483795881271362),
                                 (-7.1830785274505615, -2.5492924451828003), (-7.150893449783325, -2.849261522293091),
                                 (-7.105281829833984, -3.1474690437316895), (-7.041054964065552, -3.442199468612671),
                                 (-6.948955535888672, -3.7293089628219604), (-6.790086507797241, -3.983747124671936),
                                 (-6.568114995956421, -4.187472581863403), (-6.318660497665405, -4.356903553009033),
                                 (-6.054937362670898, -4.503317594528198), (-5.781648874282837, -4.631046533584595),
                                 (-5.501358985900879, -4.742591857910156), (-5.215502023696899, -4.839006662368774),
                                 (-4.925075531005859, -4.920602560043335), (-4.63010048866272, -4.983712434768677),
                                 (-4.331228017807007, -5.024294376373291), (-4.029853940010071, -5.0298004150390625),
                                 (-3.7346105575561523, -4.971277952194214), (-3.4450050592422485, -4.886701583862305),
                                 (-3.15744948387146, -4.795416593551636), (-2.871519446372986, -4.699127912521362),
                                 (-2.5865880250930786, -4.599940538406372), (-2.30471408367157, -4.492385625839233),
                                 (-2.027148962020874, -4.374178409576416), (-1.7569135427474976, -4.240163087844849),
                                 (-1.5003439784049988, -4.08172333240509), (-1.2684848606586456, -3.8891544342041016),
                                 (-1.0687780380249023, -3.663286566734314), (-0.8880804628133774, -3.4216960668563843),
                                 (-0.7064920961856842, -3.1807639598846436), (-0.5147070623934269, -2.9478975534439087),
                                 (-0.31095826253294945, -2.7254185676574707),
                                 (-0.09742534160614014, -2.512298107147217), (0.1195451021194458, -2.302892029285431),
                                 (0.3593883514404297, -2.1201545000076294), (0.6209217458963394, -1.9701165556907654),
                                 (0.9005316197872162, -1.8574339747428894), (1.1929829716682434, -1.7842819690704346),
                                 (1.4922239780426025, -1.746421992778778), (1.7932530045509338, -1.7276999950408936),
                                 (2.094925045967102, -1.7307924628257751), (2.389056086540222, -1.6742819547653198),
                                 (2.651361584663391, -1.525991976261139), (2.8980984687805176, -1.3524313569068909),
                                 (3.1437149047851562, -1.1780542731285095), (3.4317939281463623, -1.095316857099533),
                                 (3.7296791076660156, -1.129713535308838), (3.9924014806747437, -1.2739175260066986),
                                 (4.178549647331238, -1.508684515953064), (4.261732459068298, -1.797216534614563),
                                 (4.281541466712952, -2.0979385375976562), (4.224656105041504, -2.3923765420913696),
                                 (4.131924510002136, -2.679321527481079), (4.080831050872803, -2.976287007331848),
                                 (4.094464421272278, -3.276844024658203), (4.190914630889893, -3.5616589784622192),
                                 (4.349841117858887, -3.8177109956741333), (4.527990102767944, -4.0611995458602905),
                                 (4.681469440460205, -4.320550918579102), (4.777903318405151, -4.605756521224976),
                                 (4.815842390060425, -4.9047160148620605), (4.813847064971924, -5.206291675567627),
                                 (4.791685104370117, -5.507171154022217), (4.767841577529907, -5.807923316955566),
                                 (4.768218040466309, -6.109391689300537), (4.829968452453613, -6.4036571979522705),
                                 (4.995036602020264, -6.6533238887786865), (5.24455714225769, -6.8209333419799805),
                                 (5.536757469177246, -6.889101505279541), (5.837904453277588, -6.881271600723267),
                                 (6.133288621902466, -6.821527004241943), (6.414339303970337, -6.712889909744263),
                                 (6.6713643074035645, -6.555800437927246), (6.888463497161865, -6.347221612930298),
                                 (7.050574064254761, -6.093677520751953), (7.1474997997283936, -5.808655500411987),
                                 (7.193763494491577, -5.510613679885864), (7.216928482055664, -5.209843158721924)]
