#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

import src.personalize.configuration.personal_track_annotations as config
from src.tracks.track import Track


class RogueRacewayCounterClockwiseTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Rogue Raceway (Counter Clockwise)"
        self._ui_description = "Named in honor of the 2021 DeepRacer Championship Cup winner, Sairam Naragoni, the Rogue Raceway boasts a variety of sweeping turns and drag strips for a worthy training challenge."
        self._ui_length_in_m = 60.17  # metres
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "2022_march_pro_ccw"
        self._track_sector_dividers = [50, 88, 120, 180, 218]
        self._annotations = config.rogue_raceway_ccw_annotations
        self._track_width = 1.067

        self._track_waypoints = [(0.5094514336143264, -0.37646722563545215), (0.6388646066188812, -0.38880540430545807),
                                 (0.7685477434840338, -0.39787645787238846), (0.939370185136795, -0.4098251163959503),
                                 (1.2397050261497498, -0.4331660754978657), (1.5399169921875, -0.45803461596369743),
                                 (1.8400480151176453, -0.4838643576949835), (2.140112042427063, -0.5104598253965378),
                                 (2.440059542655945, -0.5383403713349253), (2.7398414611816406, -0.5679420176893473),
                                 (3.039472460746765, -0.5990395024418831), (3.338955044746399, -0.6315341331064701),
                                 (3.63827896118164, -0.6654576510190963), (3.9373960494995117, -0.701159194111824),
                                 (4.237025499343872, -0.7321882545948029), (4.5374529361724845, -0.7541587948799133),
                                 (4.838437557220459, -0.7662969753146172), (5.139660358428955, -0.7685357481241226),
                                 (5.440721035003662, -0.759147897362709), (5.739865541458129, -0.7250317782163621),
                                 (6.0298779010772705, -0.645101748406887), (6.301907062530518, -0.5163639765232801),
                                 (6.551624536514282, -0.34830325469374657), (6.78018593788147, -0.1522151529788971),
                                 (6.98775577545166, 0.0659029483795166), (7.170406579971313, 0.30528201442211805),
                                 (7.326836109161377, 0.5625898092985153), (7.464430809020996, 0.8304701149463654),
                                 (7.566650629043579, 1.1135124564170837), (7.617375612258911, 1.4100500345230103),
                                 (7.611611366271973, 1.710820496082306), (7.553797483444214, 2.0061980485916138),
                                 (7.465277433395386, 2.2940934896469116), (7.364265203475952, 2.5778504610061646),
                                 (7.2418365478515625, 2.8530339002609253), (7.144474029541016, 3.1370769739151),
                                 (7.134068489074707, 3.4371209144592303), (7.1986048221588135, 3.7312084436416644),
                                 (7.217203617095947, 4.031513452529907), (7.191014051437378, 4.331406116485596),
                                 (7.1256256103515625, 4.625280380249023), (7.0271923542022705, 4.909863710403442),
                                 (6.910496473312378, 5.187555313110352), (6.766817569732666, 5.451999187469482),
                                 (6.577205657958984, 5.685469150543213), (6.345340967178345, 5.877109050750732),
                                 (6.082003355026245, 6.0226709842681885), (5.80027437210083, 6.1289379596710205),
                                 (5.507811784744263, 6.199140787124634), (5.211284875869751, 6.252216577529907),
                                 (4.915272951126099, 6.308093547821045), (4.619694471359251, 6.366219520568848),
                                 (4.32384991645813, 6.422827482223511), (4.0240254402160645, 6.449751615524292),
                                 (3.7228760719299316, 6.457159042358398), (3.4217389822006226, 6.465039968490601),
                                 (3.1206165552139282, 6.473478078842163), (2.819440484046936, 6.479360580444336),
                                 (2.521697521209717, 6.444552421569824), (2.2505215406417847, 6.315103054046631),
                                 (2.0212079882621765, 6.121047019958496), (1.852728545665741, 5.872389078140259),
                                 (1.7582160234451294, 5.587206602096558), (1.736835539340973, 5.287338018417358),
                                 (1.7729464769363403, 4.9885170459747314), (1.8629929423332214, 4.701694965362549),
                                 (2.0232225656509377, 4.447748422622684), (2.2587024569511414, 4.262937426567078),
                                 (2.5337159633636435, 4.14036285877228), (2.815037488937378, 4.032650947570801),
                                 (3.099050521850586, 3.9323134422302246), (3.3780174255371094, 3.820264458656311),
                                 (3.6195445060730003, 3.6409929990768406), (3.808397054672241, 3.407703399658203),
                                 (3.917473554611206, 3.1281124353408813), (3.9428484439849854, 2.82893705368042),
                                 (3.8824585676193246, 2.5348269939422647), (3.7431100606918335, 2.2686314582824707),
                                 (3.5504419803619385, 2.0374335050582886), (3.319893479347226, 1.8442360162734968),
                                 (3.05969500541687, 1.6930134296417236), (2.7792694568634033, 1.5837244391441345),
                                 (2.4843839406967163, 1.5238428711891174), (2.1837209463119507, 1.5076048970222473),
                                 (1.882618010044098, 1.5156788527965546), (1.581928014755249, 1.5338389873504639),
                                 (1.281470000743866, 1.5555115342140198), (0.9817195236682892, 1.5853095054626465),
                                 (0.683076411485672, 1.624693512916565), (0.3860968053340912, 1.6749049425125122),
                                 (0.09349253773688926, 1.7464650273323068), (-0.19796527177095413, 1.822609007358551),
                                 (-0.4891469329595566, 1.8998035192489624), (-0.780255913734436, 1.9772729873657227),
                                 (-1.070313423871994, 2.058526933193207), (-1.3481689691543604, 2.1730970144271877),
                                 (-1.5472105145454407, 2.393452525138855), (-1.6254194378852846, 2.682790040969852),
                                 (-1.6395410299301147, 2.983531951904297), (-1.6023245453834534, 3.2819604873657227),
                                 (-1.5022394657135025, 3.5654580593109086), (-1.327273279428482, 3.808461904525757),
                                 (-1.1164193451404572, 4.023421406745911), (-0.9280807375907898, 4.2584744691848755),
                                 (-0.7540236711502075, 4.504176616668701), (-0.6370297484099865, 4.780325174331665),
                                 (-0.6246625371277332, 5.07986855506897), (-0.706679068505764, 5.368777275085449),
                                 (-0.8480114042758942, 5.634553909301758), (-1.0267476737499237, 5.876359701156616),
                                 (-1.2522545456886292, 6.075271129608154), (-1.516186535358429, 6.219141006469727),
                                 (-1.805783987045288, 6.300004959106445), (-2.105974555015564, 6.319036960601807),
                                 (-2.4047540426254272, 6.284224987030029), (-2.6910295486450195, 6.191761493682861),
                                 (-2.9593000411987305, 6.055123567581177), (-3.213705539703369, 5.8940935134887695),
                                 (-3.4465030431747437, 5.7030675411224365), (-3.669092535972595, 5.500098943710327),
                                 (-3.88948392868042, 5.294736862182617), (-4.108337044715881, 5.08774209022522),
                                 (-4.3201210498809814, 4.873558521270752), (-4.517955541610718, 4.646458387374878),
                                 (-4.697176933288574, 4.4045209884643555), (-4.8629865646362305, 4.153037071228027),
                                 (-5.038577079772949, 3.908280611038208), (-5.2226715087890625, 3.6698479652404785),
                                 (-5.410367488861084, 3.4342299699783325), (-5.598997592926025, 3.1993589401245117),
                                 (-5.788055419921875, 2.9648324251174927), (-5.977741479873657, 2.7308130264282227),
                                 (-6.1667540073394775, 2.4962520599365234), (-6.3526434898376465, 2.259205996990204),
                                 (-6.537305116653442, 2.0212034583091736), (-6.71709418296814, 1.7795164585113525),
                                 (-6.87860250473022, 1.525430500507362), (-7.012948036193848, 1.2559075355529785),
                                 (-7.124495506286624, 0.9761428833007745), (-7.22263765335083, 0.6913456916809082),
                                 (-7.315647840499878, 0.4048345610499382), (-7.397722482681274, 0.11500955745577812),
                                 (-7.4679834842681885, -0.17790353670716286), (-7.5262451171875, -0.47343701124191284),
                                 (-7.571751117706299, -0.7711922526359558), (-7.602418661117554, -1.0708380341529846),
                                 (-7.618122577667236, -1.3716399669647217), (-7.6239683628082275, -1.6728194952011108),
                                 (-7.616261959075928, -1.9739055633544922), (-7.578953504562378, -2.2726550102233887),
                                 (-7.501424551010132, -2.5635149478912354), (-7.385219097137451, -2.841231942176819),
                                 (-7.235222578048706, -3.102279543876648), (-7.0575315952301025, -3.345397472381592),
                                 (-6.856735467910767, -3.569633960723877), (-6.638310432434082, -3.7770434617996216),
                                 (-6.437363386154175, -4.001362442970276), (-6.255087375640869, -4.2411381006240845),
                                 (-6.080541849136356, -4.486655473709101), (-5.907378435134888, -4.733150482177734),
                                 (-5.736269474029541, -4.9810755252838135), (-5.569004535675049, -5.231603622436523),
                                 (-5.339703559875488, -5.423738956451416), (-5.0658860206604, -5.548659563064575),
                                 (-4.7797160148620605, -5.6425769329071045), (-4.488308429718018, -5.718865156173706),
                                 (-4.194092988967905, -5.7835114002227765), (-3.897715926170349, -5.83727240562439),
                                 (-3.5989885330200293, -5.875969648361205), (-3.2998565435409546, -5.911537408828735),
                                 (-3.001273512840264, -5.951447486877442), (-2.7032470703125, -5.995330333709717),
                                 (-2.405748963356018, -6.042629957199097), (-2.1088104248046875, -6.093357563018799),
                                 (-1.8116030097007751, -6.142487049102783), (-1.5142149925231996, -6.190505504608153),
                                 (-1.216781973838799, -6.238250494003297), (-0.9191830158233643, -6.284947872161865),
                                 (-0.621282309293747, -6.329672574996948), (-0.32266004383563995, -6.369237661361694),
                                 (-0.023278294131159782, -6.402615547180176), (0.27665259689092636, -6.43063759803772),
                                 (0.5770289003848957, -6.453399181365966), (0.8777581751346588, -6.4708945751190186),
                                 (1.1788259744644165, -6.48050594329834), (1.4796035289764404, -6.467550992965698),
                                 (1.776325523853302, -6.416043043136597), (2.064602494239807, -6.329864978790283),
                                 (2.329877495765686, -6.188287019729614), (2.5507410764694214, -5.985239028930664),
                                 (2.73746395111084, -5.749192476272583), (2.9747759103775024, -5.564805030822754),
                                 (3.254401445388794, -5.455129623413086), (3.5360203981399536, -5.348636150360107),
                                 (3.807894468307495, -5.218942165374756), (4.072826027870178, -5.075791120529175),
                                 (4.301792502403259, -4.882169008255005), (4.440697908401489, -4.616816520690918),
                                 (4.484709024429321, -4.319714546203613), (4.479778051376342, -4.018581509590142),
                                 (4.433456659317017, -3.7214224338531494), (4.315580606460567, -3.4452819824218697),
                                 (4.1173335313797, -3.220089554786682), (3.8597604036331177, -3.0654945373535156),
                                 (3.573360562324524, -2.973312020301819), (3.2768800258636475, -2.9204180240631104),
                                 (2.9764950275421143, -2.9068644046783447), (2.6769886016845805, -2.938666582107543),
                                 (2.3781845569610596, -2.976902961730957), (2.07907497882843, -3.012661933898926),
                                 (1.7794714570045573, -3.0439980030059806), (1.4795385003089905, -3.0720280408859253),
                                 (1.1794825196266174, -3.098710536956787), (0.8793976902961731, -3.12507700920105),
                                 (0.5792884528636932, -3.151158928871155), (0.2790991961956024, -3.1762999296188354),
                                 (-0.021305351052433252, -3.1986989974975586),
                                 (-0.32214389741420746, -3.213968515396118), (-0.6233064830303192, -3.2119604349136353),
                                 (-0.9234188795089722, -3.1869759559631348), (-1.221503496170044, -3.143507480621338),
                                 (-1.5206434726715088, -3.108119487762451), (-1.8207005262374878, -3.0814844369888306),
                                 (-2.121214509010315, -3.060662031173706), (-2.422155022621155, -3.0473430156707764),
                                 (-2.7229195833206177, -3.0307945013046265), (-3.0227625370025635, -3.001910448074341),
                                 (-3.3221285343170166, -2.9683754444122314), (-3.6201870441436768, -2.924942970275879),
                                 (-3.912691593170166, -2.8538180589675903), (-4.18956446647644, -2.7359999418258667),
                                 (-4.4507269859313965, -2.5862494707107544), (-4.681084632873535, -2.3929959535598755),
                                 (-4.859083652496338, -2.150849938392639), (-4.973223924636841, -1.8727390766143799),
                                 (-5.020001411437988, -1.575716495513916), (-5.003413438796997, -1.2753934860229492),
                                 (-4.927248001098633, -0.984493613243103), (-4.790140867233276, -0.7168816477060318),
                                 (-4.602973461151123, -0.4812915101647377), (-4.388985872268677, -0.26953279227018356),
                                 (-4.140840649604797, -0.09977760910987854),
                                 (-3.8583654165267944, 0.001665949821472168),
                                 (-3.558079481124878, 0.002537280321121216),
                                 (-3.258860468864441, -0.032289743423461914),
                                 (-2.9591989517211914, -0.0630282461643219), (-2.6585274934768677, -0.0807376503944397),
                                 (-2.357342481613159, -0.08637823164463043),
                                 (-2.0564719438552856, -0.10107433795928955),
                                 (-1.7560319900512695, -0.12299923598766327),
                                 (-1.4559414982795715, -0.14927491545677185),
                                 (-1.1561729907989502, -0.1789996474981308), (-0.856713205575943, -0.21170204877853394),
                                 (-0.5574503391981125, -0.24615706503391266),
                                 (-0.25851764529943466, -0.2833654433488846), (0.0401512635871768, -0.322641983628273),
                                 (0.33903689682483673, -0.3602200001478195), (0.5094514336143264, -0.37646722563545215)]
