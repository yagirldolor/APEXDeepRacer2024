#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

import src.personalize.configuration.personal_track_annotations as config
from src.tracks.track import Track


class BreadCentricSpeedwayClockwiseTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "BreadCentric Speedway (Clockwise)"
        self._ui_description = "The BreadCentric Speedway is named after AWS DeepRacer Community Hero, Tomasz Ptak AKA BreadCentric. This track adds a deceivingly technical section with an unforgiving hairpin turn separating the varying dragstrips. The BreadCentric Speedway will test the skills of even the most experienced developer."
        self._ui_length_in_m = 99.99  # metres     (NOT STATED)
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "2022_june_pro_cw"
        self._track_sector_dividers = [24, 66, 125, 164]
        self._annotations = config.breadcentric_speedway_cw_annotations
        self._track_width = 1.067

        self._track_waypoints = [(3.0248320509734805, 0.8949723162547443), (3.1457895040512085, 0.942609429359436),
                                 (3.2667150795647255, 0.9903274048689316), (3.4256550073623657, 1.053046077489853),
                                 (3.7052440643310547, 1.1641815900802612), (3.9845715761184692, 1.2759704291820526),
                                 (4.263753414154053, 1.3881245255470276), (4.542538642883301, 1.501259446144104),
                                 (4.820375442504883, 1.616699993610382), (5.100101947784424, 1.7272030711174011),
                                 (5.3913185596466064, 1.8015550374984741), (5.6910719871521, 1.8190845251083374),
                                 (5.985256671905518, 1.760756492614746), (6.251391410827637, 1.6225534677505493),
                                 (6.475352048873901, 1.422531008720398), (6.65937066078186, 1.1848532259464264),
                                 (6.810885667800903, 0.9251034557819366), (6.9366774559021, 0.6518746614456177),
                                 (7.046672344207764, 0.37186095118522644), (7.1451334953308105, 0.08757979050278664),
                                 (7.234034538269043, -0.19983994401991367), (7.313437461853027, -0.4900277405977249),
                                 (7.384430408477783, -0.782382071018219), (7.445720911026001, -1.0769294500350952),
                                 (7.497364521026611, -1.3733109831809998), (7.5364861488342285, -1.6716055274009705),
                                 (7.563291072845459, -1.9712460041046143), (7.573776006698608, -2.2718909978866577),
                                 (7.570768356323242, -2.572730541229248), (7.550303220748901, -2.8727909326553345),
                                 (7.503411293029785, -3.16989803314209), (7.438760519027709, -3.463708043098452),
                                 (7.362311124801636, -3.754677414894104), (7.258517503738403, -4.036716103553772),
                                 (7.087143898010254, -4.282430529594421), (6.858612537384033, -4.477656602859497),
                                 (6.614838600158691, -4.653972625732422), (6.3658061027526855, -4.822753429412842),
                                 (6.108036041259766, -4.977814435958862), (5.838834524154663, -5.111946105957031),
                                 (5.555983781814575, -5.213768005371094), (5.260415077209473, -5.2676825523376465),
                                 (4.959831476211548, -5.279351472854614), (4.659061431884766, -5.28687858581543),
                                 (4.358222484588623, -5.285357475280762), (4.057876110076904, -5.268535614013672),
                                 (3.7602059841156006, -5.225717544555664), (3.4715360403060913, -5.142316579818726),
                                 (3.2122535705566406, -4.992220163345337), (3.042566418647766, -4.749509334564209),
                                 (2.9917019605636597, -4.453552961349487), (2.9788219928741455, -4.153033494949341),
                                 (2.980054497718811, -3.8521764278411865), (2.9829899072647095, -3.5513269901275635),
                                 (2.9772180318832397, -3.2505409717559814), (2.9463104009628296, -2.951517939567566),
                                 (2.830011010169983, -2.6782000064849854), (2.6112575531005864, -2.4727534055709843),
                                 (2.3526309728622445, -2.319987058639527), (2.0682194232940674, -2.2235634326934814),
                                 (1.7698270082473755, -2.1898324489593506), (1.4707735180854797, -2.2178465127944946),
                                 (1.182182401418686, -2.3015440702438354), (0.910503476858139, -2.430188477039337),
                                 (0.6484695971012115, -2.578034996986389), (0.3877665549516678, -2.728216052055359),
                                 (0.12817485630512238, -2.8803104162216187), (-0.130513995885849, -3.0339365005493164),
                                 (-0.3886018581688404, -3.188570022583008), (-0.6461309045553207, -3.3441319465637207),
                                 (-0.9031885862350468, -3.5004725456237797), (-1.1603251695632935, -3.6566834449768066),
                                 (-1.4176265001296997, -3.8126208782196045), (-1.6746410131454468, -3.969032645225525),
                                 (-1.9316599369049072, -4.125437021255493), (-2.1890475749969482, -4.281232953071594),
                                 (-2.446874499320984, -4.4363014698028564), (-2.7052879333496094, -4.59039044380188),
                                 (-2.9647629261016846, -4.742683410644531), (-3.225365996360779, -4.893038034439087),
                                 (-3.4913910627365112, -5.033080577850342), (-3.782420039176941, -5.103534936904907),
                                 (-4.079061031341553, -5.064505100250244), (-4.354434490203857, -4.944581031799316),
                                 (-4.613378047943115, -4.791512489318848), (-4.874413967132568, -4.642011880874634),
                                 (-5.14081597328186, -4.502198934555054), (-5.407777547836304, -4.363446950912476),
                                 (-5.672684907913208, -4.220821380615234), (-5.933971881866455, -4.071679949760437),
                                 (-6.1894330978393555, -3.912789463996887), (-6.4367804527282715, -3.7415610551834106),
                                 (-6.673677444458008, -3.556165933609009), (-6.896066904067993, -3.353655457496643),
                                 (-7.098040342330933, -3.130843997001648), (-7.273452043533325, -2.886628031730652),
                                 (-7.414400100708008, -2.621106505393982), (-7.512904405593872, -2.3371670246124268),
                                 (-7.563546895980835, -2.040920078754425), (-7.566826343536377, -1.7403530478477478),
                                 (-7.526124000549316, -1.4424810409545898), (-7.448078870773315, -1.1520753502845764),
                                 (-7.347251892089844, -0.8686129748821259), (-7.247920513153076, -0.58461993932724),
                                 (-7.155364990234375, -0.29835235327482224), (-7.071371793746948, -0.00946345180273056),
                                 (-6.998213529586792, 0.2823545038700104), (-6.927149295806885, 0.5747081488370895),
                                 (-6.854963541030884, 0.866786777973175), (-6.782042026519775, 1.1586830019950867),
                                 (-6.709033489227295, 1.4505575299263), (-6.6348936557769775, 1.7421464920043945),
                                 (-6.560009479522705, 2.0335450172424316), (-6.484011650085449, 2.3246554136276245),
                                 (-6.406662940979004, 2.615409016609192), (-6.327099084854126, 2.9055644273757935),
                                 (-6.245123624801636, 3.195046067237854), (-6.158048391342163, 3.483033061027527),
                                 (-6.057219505310059, 3.766340970993042), (-5.893666505813599, 4.017830967903137),
                                 (-5.682554006576538, 4.231792449951172), (-5.446323871612549, 4.417909383773804),
                                 (-5.194696664810181, 4.582722902297974), (-4.932321548461914, 4.729864120483398),
                                 (-4.661842346191406, 4.861543655395508), (-4.384420871734619, 4.977891206741333),
                                 (-4.101192951202393, 5.079291105270386), (-3.812636971473694, 5.164314031600952),
                                 (-3.5191630125045776, 5.230342626571655), (-3.2215219736099243, 5.273651599884033),
                                 (-2.921085000038147, 5.285857439041138), (-2.622216582298279, 5.25478196144104),
                                 (-2.339837431907654, 5.154406547546387), (-2.0984389781951904, 4.975389003753662),
                                 (-1.8655580282211304, 4.784904479980469), (-1.63662850856781, 4.5897040367126465),
                                 (-1.4123799800872803, 4.3891260623931885), (-1.192270278930664, 4.1840174198150635),
                                 (-0.9772239029407501, 3.973607659339905), (-0.7677131295204163, 3.7576910257339478),
                                 (-0.584335271269083, 3.520641565322876), (-0.47637082263827324, 3.2405319213867188),
                                 (-0.420230895280838, 2.9451504945755005), (-0.39968956261873245, 2.645137071609497),
                                 (-0.40839095413684845, 2.34450900554657), (-0.451752258464694, 2.0470380187034607),
                                 (-0.5854575783014297, 1.7810224890708923), (-0.7844322323799133, 1.556288480758667),
                                 (-1.0470322370529175, 1.414561003446579), (-1.3395770192146301, 1.3770712316036224),
                                 (-1.6022299528121948, 1.5067455172538757), (-1.767291009426117, 1.759825050830841),
                                 (-1.9448790550231934, 2.0026314854621887), (-2.136170983314514, 2.2347479462623596),
                                 (-2.3509140014648438, 2.445142984390259), (-2.597366452217102, 2.6169304847717285),
                                 (-2.875949501991272, 2.728275418281555), (-3.174241542816162, 2.759540557861328),
                                 (-3.440150499343872, 2.634487509727478), (-3.614145874977112, 2.390534520149231),
                                 (-3.7397605180740356, 2.117234528064728), (-3.8733900785446167, 1.8477035760879517),
                                 (-3.992308497428894, 1.571382999420166), (-4.0936925411224365, 1.2881674766540527),
                                 (-4.17475152015686, 0.998495489358902), (-4.233417987823486, 0.7034806907176971),
                                 (-4.26676607131958, 0.40456394851207733), (-4.273770093917847, 0.1038772463798523),
                                 (-4.251194477081299, -0.19601434469223022), (-4.19872510433197, -0.4921427518129349),
                                 (-4.114479422569275, -0.7808173596858978), (-4.001703977584839, -1.0596166253089905),
                                 (-3.8693859577178973, -1.3294924199581115), (-3.6095200777053864, -1.4670750200748428),
                                 (-3.309828042984005, -1.4858300983905788), (-3.010608434677122, -1.4560139179229732),
                                 (-2.71511447429657, -1.3997300267219543), (-2.4237968921661412, -1.324653238058091),
                                 (-2.1363894939422563, -1.235764086246489), (-1.8528739213943481, -1.1351137161254883),
                                 (-1.5732389688491821, -1.024141788482666), (-1.2981290221214294, -0.9024207592010498),
                                 (-1.0293473303318024, -0.7672747820615768), (-0.7605337500572205, -0.6321900263428688),
                                 (-0.4855956435203552, -0.5100409490987659),
                                 (-0.2083982820622623, -0.39307092130184174),
                                 (0.06957365572452545, -0.2779521942138672),
                                 (0.34823670983314514, -0.16451656818389893),
                                 (0.6273690015077591, -0.05223996937274933), (0.9067105352878571, 0.059514835476875305),
                                 (1.1863259077072144, 0.1705836057662964), (1.4660009741783142, 0.2815009653568268),
                                 (1.7458614706993103, 0.3919498883187771), (2.0258135199546814, 0.5021677380427718),
                                 (2.3058069944381714, 0.6122799515724182), (2.585842490196228, 0.722285307943821),
                                 (2.8658504486083984, 0.8323600143194199), (3.0248320509734805, 0.8949723162547443)]
