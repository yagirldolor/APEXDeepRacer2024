#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

import src.personalize.configuration.personal_track_annotations as config
from src.tracks.track import Track


class AceSuperSpeedwayClockwiseTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Ace Super Speedway (Clockwise)"
        self._ui_description = "The Ace Super Speedway was named in honor of the 2021 AWS DeepRacer 2nd place Champion, Yousuf Nizam. Featuring full throttle straightaways and unforgiving hairpin turns the Ace Super Speedway will surely require an ace in the hole to come away with a win."
        self._ui_length_in_m = 99.99  # metres     (NOT STATED)
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "2022_april_pro_cw"
        self._track_sector_dividers = [24, 62, 103, 131, 162, 190]
        self._annotations = config.ace_super_speedway_cw_annotations
        self._track_width = 1.067
        self._track_waypoints = [(0.13473508673746287, -3.3152049903099843), (0.024409905076026917, -3.246441960334778),
                                 (-0.08591620385865606, -3.177680418123087), (-0.2313736453652382, -3.0870230197906494),
                                 (-0.48715876042842865, -2.92760694026947), (-0.7429439425468445, -2.7681914567947388),
                                 (-0.9987292885780334, -2.6087764501571655), (-1.254514992237091, -2.449361026287079),
                                 (-1.510299026966095, -2.289943039417267), (-1.7660804986953735, -2.130520462989807),
                                 (-2.0218599438667297, -1.971094012260437), (-2.277640998363495, -1.811669945716858),
                                 (-2.5334354639053345, -1.6522715091705322), (-2.7892439365386963, -1.492899477481842),
                                 (-3.0450628995895386, -1.3335480690002441), (-3.300824999809265, -1.1740880608558655),
                                 (-3.5565038919448853, -1.0144716799259186), (-3.8121010065078735, -0.8546988815069199),
                                 (-4.067820906639099, -0.6951597109436989), (-4.32401704788208, -0.5365217849612236),
                                 (-4.580695152282715, -0.3787965625524521), (-4.837542057037351, -0.2213906347751636),
                                 (-5.092101812362671, -0.05965524911880493), (-5.343852519989014, 0.10739944875240326),
                                 (-5.592796325683594, 0.27976738661527634), (-5.8488733768463135, 0.43863082211464643),
                                 (-6.120704412460327, 0.5676406361162663), (-6.403992414474487, 0.669293075799942),
                                 (-6.697126388549805, 0.7393679246306419), (-6.9957435131073, 0.7801983952522278),
                                 (-7.294363975524902, 0.8210071623325348), (-7.5921430587768555, 0.8667448610067368),
                                 (-7.886673450469971, 0.9300671368837357), (-8.17282485961914, 1.0241807103157043),
                                 (-8.446634769439697, 1.1496438384056091), (-8.70540475845337, 1.3037720620632172),
                                 (-8.930992603302002, 1.5012295246124268), (-9.074108123779297, 1.7649984955787659),
                                 (-9.149331092834473, 2.0562050342559814), (-9.174318790435791, 2.3562389612197876),
                                 (-9.164329051971436, 2.656906008720398), (-9.141397953033447, 2.9574315547943115),
                                 (-9.090532779693604, 3.254440426826477), (-9.024676322937012, 3.54842746257782),
                                 (-8.945899963378906, 3.8392199277877808), (-8.855731010437012, 4.126741051673889),
                                 (-8.75358247756958, 4.4103004932403564), (-8.638096809387207, 4.688665151596069),
                                 (-8.511319160461426, 4.962002515792847), (-8.37151050567627, 5.228852987289429),
                                 (-8.215625524520874, 5.486565828323364), (-8.038267135620117, 5.729801893234253),
                                 (-7.829938650131226, 5.946592092514038), (-7.5679895877838135, 6.093074083328247),
                                 (-7.285714864730835, 6.195265054702759), (-6.993691444396973, 6.269843578338623),
                                 (-6.697747468948364, 6.325377941131592), (-6.398786544799805, 6.363123416900635),
                                 (-6.098433494567871, 6.38723611831665), (-5.79766845703125, 6.406733989715576),
                                 (-5.496569395065308, 6.415879964828491), (-5.195168972015381, 6.415632963180542),
                                 (-4.8937718868255615, 6.415518045425415), (-4.592375993728638, 6.415439605712891),
                                 (-4.290980100631714, 6.4153618812561035), (-3.989584445953369, 6.415268898010254),
                                 (-3.6881885528564453, 6.415128469467163), (-3.3867974281311035, 6.416315078735352),
                                 (-3.0854125022888184, 6.418885707855225), (-2.784027576446533, 6.421517372131348),
                                 (-2.4831470251083374, 6.407022953033447), (-2.1824555397033687, 6.386423587799072),
                                 (-1.8835519552230835, 6.351344108581543), (-1.5889864563941956, 6.288955450057983),
                                 (-1.3082090020179749, 6.181586503982544), (-1.0477622747421265, 6.033082008361816),
                                 (-0.8524883538484573, 5.807038307189941), (-0.7543443515896797, 5.525429964065552),
                                 (-0.7547328770160675, 5.224005937576294), (-0.8149292171001434, 4.9298529624938965),
                                 (-0.9670446813106537, 4.67184591293335), (-1.1900933682918549, 4.471611499786377),
                                 (-1.4561800360679626, 4.331988573074341), (-1.7397159934043884, 4.230513334274292),
                                 (-2.026790976524353, 4.138711452484131), (-2.313870906829834, 4.04692542552948),
                                 (-2.593401551246643, 3.9356926679611206), (-2.844631552696228, 3.771332025527954),
                                 (-3.030900001525879, 3.537010073661804), (-3.1252994537353516, 3.252500057220459),
                                 (-3.112987518310547, 2.954227089881897), (-2.982234001159668, 2.6839784383773804),
                                 (-2.8020670413970947, 2.4427130222320557), (-2.594843029975891, 2.2240100502967834),
                                 (-2.379225492477417, 2.0138440132141113), (-2.1505144834518433, 1.8175610303878784),
                                 (-1.9217264652252197, 1.621357023715973), (-1.6851159930229187, 1.435130536556244),
                                 (-1.4397845268249512, 1.2600349187850952), (-1.1945814192295074, 1.0847760438919067),
                                 (-0.949388861656189, 0.909504622220993), (-0.704197347164154, 0.7342314720153809),
                                 (-0.4590199515223503, 0.5589377358555794), (-0.21421541646122932, 0.3830873593688011),
                                 (0.03933415561914444, 0.22031784802675247), (0.29530154168605804, 0.06116385757923126),
                                 (0.5509458631277084, -0.09847445785999298), (0.8066202104091644, -0.2580687403678894),
                                 (1.0622842013835907, -0.417679151520133), (1.317943513393402, -0.5772971212863922),
                                 (1.5735989809036255, -0.7369210422039032), (1.8292534947395325, -0.8965460807085037),
                                 (2.084897041320801, -1.0561896860599518), (2.340622067451477, -1.2156961560249329),
                                 (2.5957515239715576, -1.3762147128582), (2.854323983192444, -1.5308705568313599),
                                 (3.1268310546875, -1.6587885022163391), (3.4180954694747925, -1.7346029877662659),
                                 (3.717794418334961, -1.7577089667320251), (4.015684962272644, -1.7181545495986938),
                                 (4.294915437698364, -1.6072510480880737), (4.5314719676971436, -1.4222469925880432),
                                 (4.701706886291504, -1.1750089228153229), (4.7979865074157715, -0.8903884887695312),
                                 (4.819482088088989, -0.5907673239707947), (4.743240594863892, -0.3006996437907219),
                                 (4.596422910690308, -0.03807620704174042), (4.408918380737305, 0.19755816459655762),
                                 (4.202115535736084, 0.41680862568318844), (3.9767510890960693, 0.6167024224996567),
                                 (3.748949408531189, 0.8140478432178497), (3.521090030670166, 1.0113285183906555),
                                 (3.2932039499282837, 1.208578109741211), (3.065426468849182, 1.4059439897537231),
                                 (2.842717528343198, 1.6088129878044155), (2.632212996482849, 1.8242070078849792),
                                 (2.4532435536384583, 2.06597101688385), (2.3578149676322937, 2.349166989326477),
                                 (2.3822180032730103, 2.648545026779175), (2.4662760496139526, 2.937654495239258),
                                 (2.5765585899353027, 3.2179394960403442), (2.70681095123291, 3.4897059202194214),
                                 (2.8565295934677124, 3.751295566558838), (3.023706078529358, 4.001846551895142),
                                 (3.195525050163269, 4.249469518661499), (3.3851640224456787, 4.483508348464966),
                                 (3.587499499320984, 4.706563472747803), (3.8027634620666455, 4.917194128036494),
                                 (4.03322696685791, 5.111451148986816), (4.282683372497559, 5.280389785766602),
                                 (4.5510194301605225, 5.417084455490112), (4.8383920192718435, 5.506140947341917),
                                 (5.137913942337036, 5.529930591583252), (5.431572914123535, 5.467356204986572),
                                 (5.694831848144531, 5.322696924209595), (5.925277471542358, 5.129071474075317),
                                 (6.1197731494903564, 4.899580955505371), (6.266309022903442, 4.636876583099365),
                                 (6.356499910354614, 4.349872589111328), (6.393784046173096, 4.051358461380005),
                                 (6.387911081314086, 3.7503755092620796), (6.347557067871094, 3.4520264863967896),
                                 (6.286013603210449, 3.157251000404358), (6.206145524978638, 2.8666324615478516),
                                 (6.126204967498779, 2.576031446456909), (6.047673463821411, 2.2850464582443237),
                                 (5.990039587020875, 1.9897390604019085), (6.013416528701782, 1.6903774738311768),
                                 (6.107812404632568, 1.4051265120506287), (6.275351524353027, 1.1557425558567047),
                                 (6.496149063110352, 0.9516026675701141), (6.749083995819092, 0.7882895171642303),
                                 (7.0143938064575195, 0.6452888399362564), (7.2875075340271, 0.5178128760308027),
                                 (7.560554504394531, 0.3902013562619686), (7.831191539764404, 0.2578248605132103),
                                 (8.095683574676514, 0.1133141964673996), (8.347577571868896, -0.05194370448589325),
                                 (8.580944061279297, -0.2425374910235405), (8.788559436798096, -0.460948146879673),
                                 (8.963764667510986, -0.7058905065059662), (9.099095821380615, -0.9744543731212616),
                                 (9.163969993591309, -1.2680144906044006), (9.179831504821777, -1.5686129927635193),
                                 (9.156758785247803, -1.8688045144081116), (9.116973876953125, -2.1675649881362915),
                                 (9.051152229309082, -2.4615265130996704), (8.976913452148438, -2.7534594535827637),
                                 (8.88338851928711, -3.0399744510650635), (8.781173706054688, -3.3232879638671875),
                                 (8.66629934310913, -3.60193407535553), (8.540563583374023, -3.8756215572357178),
                                 (8.405368328094482, -4.144995450973511), (8.257510662078857, -4.407389163970947),
                                 (8.101697206497192, -4.665383577346802), (7.930574178695679, -4.913207054138184),
                                 (7.753021240234375, -5.156750440597534), (7.555838108062744, -5.384396553039551),
                                 (7.354396820068359, -5.608561038970947), (7.130345106124878, -5.81016993522644),
                                 (6.894053936004639, -5.996865510940552), (6.63960337638855, -6.157991886138916),
                                 (6.3671336174011195, -6.286056995391847), (6.080162525177002, -6.376537561416626),
                                 (5.782690048217773, -6.4219441413879395), (5.482192516326904, -6.4074296951293945),
                                 (5.188680410385132, -6.342194557189941), (4.911575078964233, -6.225600481033325),
                                 (4.639524459838867, -6.0958781242370605), (4.36841344833374, -5.964445352554321),
                                 (4.107739448547363, -5.813957452774048), (3.856981039047241, -5.64536190032959),
                                 (3.605137586593628, -5.478749513626099), (3.35110604763031, -5.316130638122559),
                                 (3.0949374437332153, -5.15741491317749), (2.838320016860962, -4.999518394470215),
                                 (2.5820775032043457, -4.840937376022339), (2.3262104988098145, -4.681670904159546),
                                 (2.0705854296684265, -4.521962881088257), (1.8149064779281616, -4.362352967262268),
                                 (1.5591624975204468, -4.202861547470093), (1.3033600449562073, -4.043477416038513),
                                 (1.0475527048110962, -3.884101986885071), (0.7917564213275909, -3.7247064113616943),
                                 (0.5359713584184647, -3.5652899742126465), (0.2801915094605647, -3.4058644771575928),
                                 (0.13473508673746287, -3.3152049903099843)]
