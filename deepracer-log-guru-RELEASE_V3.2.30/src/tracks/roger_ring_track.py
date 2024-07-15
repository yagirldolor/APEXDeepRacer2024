#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

import src.personalize.configuration.personal_track_annotations as config
from src.tracks.track import Track


class RogerRingTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Roger Ring"
        self._ui_description = "Get ready rip on the Roger Ring! This track at 45.3m honoring community member, Roger Logan, features a lightning fast drag strip straight into back-to-back 90 degree turns will undoubtedly send developers careening into the green. Do you have the skills to keep all four wheels on track? Submit your model today and find out!"
        self._ui_length_in_m = 45.30  # metres
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "2022_september_open"
        self._track_sector_dividers = [49, 99]
        self._annotations = config.roger_ring_annotations
        self._track_width = 1.067

        self._track_waypoints = [(6.1176934242248535, 1.6017529964447021), (5.826994180679321, 1.6844214797019958),
                                 (5.53624701499939, 1.76692396402359), (5.2456374168396, 1.8499065041542053),
                                 (4.955142974853516, 1.9332934617996216), (4.664625883102417, 2.016602039337158),
                                 (4.374183416366577, 2.100167989730835), (4.083874464035035, 2.184198975563049),
                                 (3.793715476989746, 2.2687445282936096), (3.503848910331726, 2.3542869687080383),
                                 (3.214389443397521, 2.4411974549293523), (2.925180554389955, 2.5289388895034786),
                                 (2.6363024711608896, 2.6177620887756343), (2.347991466522216, 2.7084079980850224),
                                 (2.060753583908081, 2.802393078804016), (1.7753009796142578, 2.9016555547714233),
                                 (1.4936890006065369, 3.0112431049346924), (1.2169225215911865, 3.1326210498809814),
                                 (0.9413017332553864, 3.2566055059432983), (0.6672488451004028, 3.3840194940567017),
                                 (0.3946755900979042, 3.5145689249038696), (0.1235755942761898, 3.648151397705078),
                                 (-0.1463654674589634, 3.7840625047683716), (-0.415218710899353, 3.9221115112304688),
                                 (-0.6831388473510742, 4.061965107917786), (-0.9506725668907166, 4.202555537223816),
                                 (-1.2176772952079773, 4.344149589538574), (-1.4843894839286804, 4.4862940311431885),
                                 (-1.7510585188865662, 4.628519058227539), (-2.0179539918899536, 4.770318508148193),
                                 (-2.28485107421875, 4.91211462020874), (-2.5521894693374634, 5.053076982498169),
                                 (-2.8203275203704816, 5.192512035369872), (-3.0881814956665026, 5.332491397857665),
                                 (-3.355399489402771, 5.4736809730529785), (-3.6222130060195923, 5.615631580352783),
                                 (-3.888953447341919, 5.757719993591309), (-4.155704379081726, 5.899791955947876),
                                 (-4.423083066940309, 6.040673971176148), (-4.691425085067747, 6.179715633392333),
                                 (-4.960876941680908, 6.316583871841431), (-5.231634855270386, 6.450769424438477),
                                 (-5.5168914794921875, 6.548874616622925), (-5.815761566162109, 6.541188955307007),
                                 (-6.068263053894043, 6.3810999393463135), (-6.249250650405884, 6.139617443084717),
                                 (-6.413990497589111, 5.886249542236328), (-6.573343515396118, 5.62945294380188),
                                 (-6.730562925338745, 5.371339559555054), (-6.88414740562439, 5.111117124557495),
                                 (-7.037384986877441, 4.850625038146973), (-7.1907124519348145, 4.5901854038238525),
                                 (-7.336475849151611, 4.325462102890015), (-7.464720964431763, 4.0518845319747925),
                                 (-7.564963340759277, 3.76695454120636), (-7.623372316360474, 3.470766067504883),
                                 (-7.626456022262573, 3.1690934896469116), (-7.562005281448364, 2.874750018119812),
                                 (-7.427715539932251, 2.6046454906463623), (-7.243634462356567, 2.365394115447998),
                                 (-7.0248143672943115, 2.1572749614715576), (-6.784235000610352, 1.974494993686676),
                                 (-6.530263185501096, 1.8107579946517927), (-6.268717527389526, 1.6593539714813232),
                                 (-6.003293991088867, 1.5148224830627441), (-5.737553119659424, 1.3708758354187012),
                                 (-5.473800897598267, 1.223331332206726), (-5.207903623580933, 1.0796711146831512),
                                 (-4.9424450397491455, 0.9352074712514877), (-4.704691171646121, 0.7866308391094226),
                                 (-4.523929953575134, 0.5308073908090591), (-4.573440074920653, 0.2270696051418818),
                                 (-4.722730875015258, -0.03277765214442985), (-4.864018440246582, -0.29994249902665615),
                                 (-5.0049331188201895, -0.5673051923513395), (-5.14219856262207, -0.8365587890148163),
                                 (-5.279217958450317, -1.105937510728836), (-5.416518449783325, -1.3751740455627441),
                                 (-5.555163860321045, -1.643716037273407), (-5.694401979446411, -1.9119524955749512),
                                 (-5.834875822067261, -2.1795474886894226), (-5.978220462799074, -2.4456034898757966),
                                 (-6.097316026687622, -2.722458004951477), (-6.0933234691619855, -3.021409034729007),
                                 (-5.95368695259094, -3.2869644165039085), (-5.73467493057251, -3.4942145347595215),
                                 (-5.481660842895504, -3.659173011779787), (-5.215909957885742, -3.803052544593811),
                                 (-4.948010683059692, -3.9429309368133545), (-4.685173988342285, -4.09201455116272),
                                 (-4.420256614685059, -4.2374759912490845), (-4.155316948890686, -4.3828970193862915),
                                 (-3.8903539180755615, -4.528275966644287), (-3.625418543815613, -4.673704385757446),
                                 (-3.360502600669861, -4.819168329238892), (-3.095589518547058, -4.964637517929077),
                                 (-2.830662488937378, -5.11008095741272), (-2.5657039880752563, -5.2554686069488525),
                                 (-2.300939917564392, -5.4012041091918945), (-2.0365095138549805, -5.547548532485962),
                                 (-1.7723710536956787, -5.6944193840026855), (-1.508049488067627, -5.84096097946167),
                                 (-1.2444284856319427, -5.988757371902466), (-0.980852335691452, -6.136584520339966),
                                 (-0.7190878540277481, -6.2876341342926025), (-0.4501989036798477, -6.425368070602417),
                                 (-0.1660713143646717, -6.527409553527832), (0.13278110325336456, -6.566696405410767),
                                 (0.4304436892271042, -6.520448446273804), (0.7084534913301468, -6.403428077697754),
                                 (0.9675221741199493, -6.24785041809082), (1.2268309593200684, -6.092614650726318),
                                 (1.486472487449646, -5.937933921813965), (1.7460734844207764, -5.783183336257935),
                                 (2.0057239532470703, -5.628516435623169), (2.2658130526542664, -5.474587917327881),
                                 (2.525781512260437, -5.3204569816589355), (2.785777449607849, -5.166370868682861),
                                 (3.045876979827881, -5.012459993362427), (3.3060195446014404, -4.8586225509643555),
                                 (3.5657620429992676, -4.704110860824585), (3.8252564668655396, -4.549181938171387),
                                 (4.0846474170684814, -4.394079566001892), (4.343545913696289, -4.238158583641052),
                                 (4.602388858795166, -4.082143425941467), (4.860654592514038, -3.9251744747161865),
                                 (5.118396997451782, -3.767355442047119), (5.377038478851318, -3.6110085248947144),
                                 (5.632726669311523, -3.4499200582504272), (5.877057313919067, -3.2721970081329346),
                                 (6.102092981338501, -3.070756435394287), (6.304429531097412, -2.8464900255203247),
                                 (6.481137990951538, -2.6015130281448364), (6.63477349281311, -2.3412625789642334),
                                 (6.7866246700286865, -2.079955041408539), (6.938342571258545, -1.8185715675354004),
                                 (7.089535474777222, -1.5568880438804626), (7.239607334136963, -1.2945560216903687),
                                 (7.239607334136963, -1.2945560216903687), (7.339818000793457, -1.0094459056854248),
                                 (7.4290478229522705, -0.7207111120223999), (7.507282733917236, -0.4288051426410675),
                                 (7.571354627609253, -0.1334923580288887), (7.61388373374939, 0.16563044860959053),
                                 (7.626677513122559, 0.4674154967069626), (7.5943121910095215, 0.7674819529056549),
                                 (7.489768028259277, 1.0496461689472198), (7.276292324066162, 1.2573940753936768),
                                 (6.988321542739868, 1.3486551344394684), (6.6985039710998535, 1.4343655109405518),
                                 (6.408241033554077, 1.5185534358024597), (6.1176934242248535, 1.6017529964447021)]
