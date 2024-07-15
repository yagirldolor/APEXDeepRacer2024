#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

import src.personalize.configuration.personal_track_annotations as config
from src.tracks.track import Track


class CumuloTurnpikeTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Cumulo Turnpike"
        self._ui_description = "The Cumulo Turnpike shifts from high-speed straightaways to challenging corners. It requires a perfect storm of exceptional navigation skill and speed control."
        self._ui_length_in_m = 60  # metres
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "Belille"
        self._track_sector_dividers = [61, 178, 250, 335]
        self._annotations = config.cumulo_turnpike_annotations
        self._track_width = 1.066

        self._track_waypoints = [
            (-2.2433555126190186, -5.3092265129089355), (-2.3801075220108032, -5.3720526695251465),
            (-2.5168585777282715, -5.434880495071411), (-2.6536084413528442, -5.497710466384888),
            (-2.7903579473495483, -5.560542583465576), (-2.927107095718384, -5.62337589263916),
            (-3.0638540983200073, -5.686211824417114), (-3.200601100921631, -5.749051094055176),
            (-3.3373450040817256, -5.811892986297607), (-3.474087953567505, -5.874738931655884),
            (-3.610828995704651, -5.937588453292847), (-3.7475684881210327, -6.0004425048828125),
            (-3.884305953979492, -6.063300132751465), (-4.021041393280029, -6.126162528991699),
            (-4.1577736139297485, -6.189031600952148), (-4.29450249671936, -6.251907587051392),
            (-4.431227922439575, -6.314790487289429), (-4.567950963973999, -6.377681016921997),
            (-4.704670429229736, -6.440577983856201), (-4.841385126113892, -6.503485441207886),
            (-4.978094100952148, -6.566405534744263), (-5.11479640007019, -6.629338502883911),
            (-5.251493453979492, -6.692283630371094), (-5.388185024261475, -6.755242586135864),
            (-5.524868488311768, -6.818216323852539), (-5.6615424156188965, -6.881212472915649),
            (-5.798206567764282, -6.944230556488037), (-5.934859991073608, -7.007270097732544),
            (-6.071503400802612, -7.0703325271606445), (-6.208120584487915, -7.133450508117676),
            (-6.3447043895721436, -7.196640491485596), (-6.481255531311035, -7.259903430938721),
            (-6.617772340774536, -7.3232386112213135), (-6.754256010055542, -7.386646032333374),
            (-6.895652532577515, -7.437852621078491), (-6.895652532577515, -7.437852621078491),
            (-7.044490575790405, -7.459097623825073), (-7.193974018096924, -7.444172620773315),
            (-7.335344076156616, -7.393069505691528), (-7.4621570110321045, -7.312326431274414),
            (-7.572683572769165, -7.2102508544921875), (-7.668017387390137, -7.09384560585022),
            (-7.75023341178894, -6.967808485031128), (-7.821142911911011, -6.835077524185181),
            (-7.8872129917144775, -6.699860572814941), (-7.952604532241821, -6.5643181800842285),
            (-8.018579959869385, -6.429056882858276), (-8.084591388702393, -6.293812990188599),
            (-8.15066409111023, -6.158599615097046), (-8.216837167739868, -6.023435354232788),
            (-8.28309178352356, -5.888311386108398), (-8.349424839019775, -5.753226041793823),
            (-8.415831327438354, -5.618176460266113), (-8.482304096221924, -5.483159065246582),
            (-8.548837184906006, -5.34817099571228), (-8.615426540374756, -5.213212013244629),
            (-8.682065963745117, -5.078277111053467), (-8.74875783920288, -4.943368434906006),
            (-8.815499305725098, -4.808484077453613), (-8.882203578948975, -4.673581123352051),
            (-8.94908332824707, -4.5387654304504395), (-9.01633071899414, -4.404132843017578),
            (-9.081042289733887, -4.268253564834595), (-9.135771751403809, -4.12810754776001),
            (-9.175667762756348, -3.983043909072876), (-9.196319580078125, -3.834062933921814),
            (-9.19265604019165, -3.6837589740753174), (-9.160329818725586, -3.536964535713196),
            (-9.098246097564697, -3.4000675678253174), (-9.011915683746338, -3.2768609523773193),
            (-8.918860912322998, -3.1585785150527954), (-8.82591962814331, -3.0402140617370605),
            (-8.73243236541748, -2.922279953956604), (-8.638368129730225, -2.8048059940338135),
            (-8.543859004974365, -2.687690019607544), (-8.448991298675537, -2.5708630084991455),
            (-8.353895664215088, -2.4542230367660522), (-8.258726358413696, -2.337641477584839),
            (-8.163627862930298, -2.221003532409668), (-8.068738460540771, -2.10419499874115),
            (-7.97413444519043, -1.987155020236969), (-7.880150556564331, -1.8696194887161255),
            (-7.785728693008423, -1.7524240612983704), (-7.6937456130981445, -1.6333025097846985),
            (-7.6129748821258545, -1.5057514905929565), (-7.553110837936401, -1.3680450320243835),
            (-7.516254901885986, -1.2216024994850159), (-7.499631881713867, -1.0718979835510254),
            (-7.500295639038086, -0.9213157296180725), (-7.515851974487305, -0.7714698016643524),
            (-7.542841911315918, -0.623399555683136), (-7.579787969589233, -0.47740304470062256),
            (-7.62422513961792, -0.3336169943213463), (-7.6752989292144775, -0.19199201464653015),
            (-7.731427431106567, -0.05235494673252106), (-7.792064666748047, 0.08541585505008698),
            (-7.856169939041138, 0.22157439636066556), (-7.923354387283325, 0.3562564067542553),
            (-7.992866277694702, 0.48973448574543), (-8.064391136169434, 0.622152641415596),
            (-8.137332201004028, 0.753787949681282), (-8.211293458938599, 0.884854257106781),
            (-8.285639524459839, 1.0156990587711334), (-8.360096216201782, 1.1464861631393433),
            (-8.434146881103516, 1.2775099873542786), (-8.503588676452637, 1.411071002483368),
            (-8.566099643707275, 1.5481584668159485), (-8.616635799407959, 1.6898580193519592),
            (-8.653736591339111, 1.8359314799308777), (-8.675332069396973, 1.984975516796112),
            (-8.679991722106934, 2.135432004928589), (-8.666483879089355, 2.2854939699172974),
            (-8.634544372558594, 2.432634472846985), (-8.5849928855896, 2.574732542037964),
            (-8.519152641296387, 2.7101329565048218), (-8.43893814086914, 2.8375344276428223),
            (-8.346338510513306, 2.9562039375305176), (-8.243124961853027, 3.0657429695129395),
            (-8.13066840171814, 3.165739417076111), (-8.009968280792236, 3.255635976791382),
            (-7.881226539611816, 3.3335455656051636), (-7.752162933349609, 3.411041021347046),
            (-7.6240553855896, 3.4901355504989624), (-7.496673107147217, 3.570428490638733),
            (-7.368025541305542, 3.6484909057617188), (-7.237656116485596, 3.7235344648361206),
            (-7.105564594268799, 3.795559883117676), (-6.97175145149231, 3.8645673990249634),
            (-6.836216449737549, 3.930468440055847), (-6.698961496353149, 3.992436408996582),
            (-6.559986591339111, 4.050267934799194), (-6.419292688369751, 4.103961944580078),
            (-6.276879549026489, 4.153459548950195), (-6.132765531539917, 4.197142481803894),
            (-5.9869585037231445, 4.234286069869995), (-5.83945894241333, 4.264890670776367),
            (-5.690495491027832, 4.2886329889297485), (-5.540827512741089, 4.304440379142761),
            (-5.390514612197876, 4.312228441238403), (-5.2396931648254395, 4.312081456184387),
            (-5.089314699172974, 4.304585933685303), (-4.939561367034912, 4.289853453636169),
            (-4.790463209152222, 4.2680981159210205), (-4.642301559448242, 4.241247892379761),
            (-4.495143175125122, 4.209763526916504), (-4.348968982696533, 4.173761010169983),
            (-4.203459978103638, 4.135177135467529), (-4.058502554893494, 4.094702482223511),
            (-3.9140959978103638, 4.052338600158691), (-3.7699644565582275, 4.009029507637024),
            (-3.625798463821411, 3.9658321142196655), (-3.4815980195999146, 3.9227445125579834),
            (-3.337344527244568, 3.879835844039917), (-3.1927939653396606, 3.8379725217819214),
            (-3.047871947288513, 3.7974201440811157), (-2.902577519416809, 3.758177876472473),
            (-2.7569104433059692, 3.7202640771865845), (-2.610836982727051, 3.683997869491577),
            (-2.4643439054489136, 3.649502158164978), (-2.317432403564453, 3.616776466369629),
            (-2.1701014041900635, 3.585821032524109), (-2.022367537021637, 3.55674946308136),
            (-1.8742765188217163, 3.529923915863037), (-1.725832998752594, 3.505371928215027),
            (-1.57703697681427, 3.4830929040908813), (-1.427887499332428, 3.4630870819091797),
            (-1.2784189581871033, 3.4451464414596558), (-1.12892347574234, 3.427451491355896),
            (-0.979468584060669, 3.4095760583877563), (-0.8300549983978271, 3.3915189504623413),
            (-0.6806949973106384, 3.3731045722961426), (-0.5314159393310547, 3.354022979736328),
            (-0.38226155936717987, 3.3339951038360596), (-0.23328470438718796, 3.3126864433288574),
            (-0.08441589749418199, 3.2906334400177), (0.06460554199293256, 3.2696419954299927),
            (0.21384215354919434, 3.250235438346863), (0.3632168620824814, 3.2319204807281494),
            (0.5126787573099136, 3.214334011077881), (0.6621837615966797, 3.197110414505005),
            (0.8115487992763519, 3.1787179708480835), (0.9601696729660034, 3.1550785303115845),
            (1.1069781482219696, 3.1220650672912598), (1.2502599954605103, 3.076130986213684),
            (1.387781023979187, 3.0150485038757324), (1.5173375010490417, 2.938517928123474),
            (1.63754802942276, 2.8480039834976196), (1.7480729222297668, 2.7458709478378296),
            (1.8494539856910706, 2.63463294506073), (1.9421690106391907, 2.516116499900818),
            (2.0297159552574158, 2.393684983253479), (2.1140004992485046, 2.26898592710495),
            (2.195928931236267, 2.1427114605903625), (2.2762394547462463, 2.0154260396957397),
            (2.354925036430359, 1.8871264457702637), (2.431849479675293, 1.7577794790267944),
            (2.506954550743103, 1.627368986606598), (2.580485463142395, 1.4960525035858154),
            (2.6529375314712524, 1.364147961139679), (2.7246769666671753, 1.231853872537613),
            (2.796860456466675, 1.0997960567474365), (2.870419502258301, 0.9685046374797821),
            (2.947264552116394, 0.8390718102455139), (3.0296369791030884, 0.7131262123584747),
            (3.1195740699768066, 0.5923783034086227), (3.219469428062439, 0.47972026094794273),
            (3.3298414945602417, 0.3774394430220127), (3.4503334760665894, 0.28701790422201157),
            (3.5788694620132446, 0.20868974924087524), (3.7134904861450195, 0.14123915135860443),
            (3.852482557296753, 0.08338779211044312), (3.994196057319641, 0.03257836401462555),
            (4.137877941131592, -0.012348845601081848), (4.283376932144165, -0.051017746329307556),
            (4.430595636367798, -0.08318580687046051), (4.579591989517212, -0.10432656109333038),
            (4.730315923690796, -0.10960753262042999), (4.879870176315308, -0.09259010851383209),
            (5.023515462875366, -0.04747360944747925), (5.151707649230957, 0.03164850175380707),
            (5.253910064697266, 0.1422177478671074), (5.326608657836914, 0.27402351424098015),
            (5.373631000518798, 0.41700080037116666), (5.400956392288208, 0.5649996101856232),
            (5.4137959480285645, 0.7149454653263092), (5.4161529541015625, 0.8654195964336395),
            (5.411362171173096, 1.0158352553844452), (5.403127431869507, 1.166106998920444),
            (5.398573637008667, 1.3165479898452779), (5.401602506637573, 1.4670075178146362),
            (5.4133689403533936, 1.6170559525489807), (5.43486738204956, 1.7660344839096034),
            (5.467522144317627, 1.9129775166511536), (5.513009071350098, 2.0564634799957275),
            (5.573216915130615, 2.1943995356559753), (5.649998426437378, 2.3238298892974854),
            (5.744685411453247, 2.440798044204712), (5.857232570648193, 2.540704607963562),
            (5.98550009727478, 2.619455933570862), (6.125471115112305, 2.674915909767151),
            (6.272496938705444, 2.7074824571609497), (6.422598123550415, 2.719393014907837),
            (6.57290244102478, 2.7153120040893555), (6.722724676132202, 2.6995290517807007),
            (6.872570514678955, 2.6845895051956177), (7.022485971450806, 2.6716148853302),
            (7.1723785400390625, 2.658342957496643), (7.322237014770508, 2.64449405670166),
            (7.472078084945679, 2.630481004714966), (7.621904611587524, 2.616336464881897),
            (7.771716117858887, 2.6020299196243286), (7.921517610549927, 2.5876134634017944),
            (8.071313381195068, 2.5731334686279297), (8.221107959747314, 2.558650016784668),
            (8.370905876159668, 2.544204592704773), (8.520713329315186, 2.5298575162887573),
            (8.670535564422607, 2.5156530141830444), (8.820373058319092, 2.501621961593628),
            (8.970231056213379, 2.4878114461898804), (9.120108604431152, 2.4742095470428467),
            (9.269999504089355, 2.4607419967651367), (9.41991662979126, 2.4475714564323425),
            (9.56989049911499, 2.4351800680160522), (9.719870567321777, 2.4228214621543884),
            (9.869534492492676, 2.4068950414657593), (10.015608310699463, 2.371210515499115),
            (10.152763843536377, 2.3096755146980286), (10.27585506439209, 2.2233670353889465),
            (10.381980419158936, 2.116804540157318), (10.471235275268555, 1.9957199692726135),
            (10.545615196228027, 1.8649355173110962), (10.60825490951538, 1.72810298204422),
            (10.667805194854736, 1.5898955464363098), (10.72820520401001, 1.4520530104637146),
            (10.788965225219727, 1.3143699765205383), (10.850074768066406, 1.1768428683280945),
            (10.911449909210205, 1.0394341945648193), (10.973020076751709, 0.9021105766296387),
            (11.034704685211182, 0.7648414969444275), (11.096434593200684, 0.6275901049375534),
            (11.158114910125732, 0.49031925201416016), (11.21983003616333, 0.35306115448474884),
            (11.280125141143799, 0.21516924817115068), (11.329169750213623, 0.07295960932970047),
            (11.359954833984375, -0.07426137453876436), (11.367300033569336, -0.2244369015097618),
            (11.34650993347168, -0.37329520285129547), (11.296084880828857, -0.5148769617080688),
            (11.21923017501831, -0.64410200715065), (11.13294506072998, -0.7674107849597931),
            (11.044525146484375, -0.8891947567462921), (10.956705093383789, -1.0114072263240814),
            (10.869455337524414, -1.1340309381484985), (10.782229900360107, -1.2566669285297394),
            (10.694904804229736, -1.3792340159416199), (10.607550144195557, -1.5017805099487305),
            (10.520225048065186, -1.6243454813957214), (10.4329195022583, -1.7469249963760376),
            (10.34561538696289, -1.8695074915885925), (10.25831651687622, -1.9920910000801086),
            (10.17101526260376, -2.114675998687744), (10.08371877670288, -2.237263023853302),
            (9.996421337127686, -2.35985004901886), (9.909124851226807, -2.482437014579773),
            (9.82183027267456, -2.6050225496292114), (9.734525203704834, -2.727604031562805),
            (9.647212505340576, -2.850181460380554), (9.55989694595337, -2.9727535247802734),
            (9.472569942474365, -3.0953184366226196), (9.385233402252197, -3.2178770303726196),
            (9.297898292541504, -3.34043550491333), (9.21055793762207, -3.462991952896118),
            (9.123159408569336, -3.585506558418274), (9.035682678222656, -3.707964539527893),
            (8.948288440704346, -3.83048152923584), (8.86124324798584, -3.9532485008239746),
            (8.774272441864014, -4.076067566871643), (8.685470581054688, -4.197580099105835),
            (8.590948104858398, -4.314641952514648), (8.486961841583252, -4.423393964767456),
            (8.374224662780762, -4.523056507110596), (8.25344443321228, -4.612786531448364),
            (8.125500440597534, -4.691985130310059), (7.991434097290039, -4.760290861129761),
            (7.852306604385376, -4.817622423171997), (7.709304094314575, -4.864459037780762),
            (7.564477920532227, -4.905381441116333), (7.419328451156616, -4.945178508758545),
            (7.274196624755859, -4.984982013702393), (7.128847360610964, -5.023985147476195),
            (6.983260154724123, -5.062102079391479), (6.837462902069092, -5.099407911300659),
            (6.691451787948608, -5.135865926742554), (6.545218467712404, -5.171421051025391),
            (6.398759603500364, -5.206034421920776), (6.2520740032196045, -5.239680051803589),
            (6.10516095161438, -5.2723095417022705), (5.958019018173218, -5.303899526596069),
            (5.810649156570435, -5.334401607513428), (5.6630518436431885, -5.363789319992065),
            (5.515228033065796, -5.39201283454895), (5.367182970046997, -5.419054985046387),
            (5.218924522399902, -5.4448933601379395), (5.070435047149658, -5.469389915466309),
            (4.921712160110474, -5.492479085922241), (4.772916078567505, -5.514821529388428),
            (4.623981475830078, -5.536067485809326), (4.473963975906372, -5.551774501800537),
            (4.322773218154907, -5.560617923736572), (4.172840595245361, -5.552545547485352),
            (4.025197386741638, -5.5232908725738525), (3.881927490234375, -5.473924160003662),
            (3.7473496198654175, -5.406658411026001), (3.621706485748291, -5.322608947753906),
            (3.5055429935455322, -5.226886510848999), (3.3987849950790405, -5.120456218719482),
            (3.299368977546692, -5.007312059402466), (3.206622004508972, -4.8887550830841064),
            (3.1188145875930786, -4.7664361000061035), (3.0343445539474487, -4.6418845653533936),
            (2.9524779319763184, -4.515594005584717), (2.8708975315093994, -4.389116287231445),
            (2.7892138957977295, -4.262710928916931), (2.7047860622406006, -4.138124585151672),
            (2.6168099641799927, -4.015897035598755), (2.5223804712295532, -3.8986915349960327),
            (2.4196245670318604, -3.7882291078567505), (2.3056334257125854, -3.689913511276245),
            (2.1780235171318054, -3.608363628387451), (2.038639008998871, -3.5521680116653442),
            (1.8890864849090576, -3.526404023170471), (1.738826036453247, -3.5300599336624146),
            (1.5914654731750488, -3.5624356269836426), (1.4479820132255554, -3.6108254194259644),
            (1.308882474899292, -3.668620467185974), (1.1735565662384033, -3.734509587287903),
            (1.038214921951294, -3.800363063812256), (0.9022049009799957, -3.8647836446762085),
            (0.7655268907546997, -3.9277695417404175), (0.6284805089235306, -3.9899659156799316),
            (0.49152445793151855, -4.052355170249939), (0.3546635955572116, -4.114948868751527),
            (0.21789796696975752, -4.177747011184692), (0.08122085779905319, -4.2407344579696655),
            (-0.05545080453157425, -4.303733468055725), (-0.19214190635830164, -4.3666908740997314),
            (-0.3288523964583874, -4.4296064376831055), (-0.46558229625225067, -4.492480516433716),
            (-0.6023316532373428, -4.555312633514404), (-0.7390885353088379, -4.618128538131714),
            (-0.8758440613746643, -4.6809468269348145), (-1.0125977098941803, -4.743769407272339),
            (-1.1493500769138336, -4.806594371795654), (-1.2861005067825317, -4.8694236278533936),
            (-1.422850489616394, -4.932255506515503), (-1.55959951877594, -4.995086908340454),
            (-1.6963495016098022, -5.057917833328247), (-1.8330999612808228, -5.120747089385986),
            (-1.9698514938354492, -5.183574676513672), (-2.106602966785431, -5.24640154838562),
            (-2.2433555126190186, -5.3092265129089355)
        ]
