#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

import src.personalize.configuration.personal_track_annotations as config
from src.tracks.track import Track


class KueiRacewayTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Kuei Raceway"
        self._ui_description = "Kuei Raceway is a fast short track (46.15m) with a friendly high speed arch and two straightaways interspersed between 2 hairpins, a chicane, and a technical cutback hairpin. It is named after 3rd place DeepRacer League finalists Kuei of NCTU CGI Taiwan."
        self._ui_length_in_m = 46.15  # metres
        self._ui_width_in_cm = 107  # centimetres   # TODO
        self._world_name = "hamption_open"
        self._track_sector_dividers = [20, 36, 50]
        self._annotations = config.kuei_raceway_annotations
        self._track_width = 1.066

        self._track_waypoints = [(6.03279709815979, -1.8021149635314941), (5.714150428771973, -1.2862839698791504),
                                 (5.43648386001587, -0.7462107092142117), (5.1395111083984375, -0.216559037566185),
                                 (4.814438104629518, 0.29628457222133664), (4.455544471740723, 0.7859974503517151),
                                 (4.057212948799133, 1.2441150844097137), (3.631266951560974, 1.6769095659255981),
                                 (3.1829644441604614, 2.086407959461212), (2.705763578414917, 2.4617600440979004),
                                 (2.2013275027275085, 2.799659490585327), (1.6760309934616089, 3.104224443435669),
                                 (1.1368111073970795, 3.3834869861602783), (0.5887244492769241, 3.6449666023254395),
                                 (0.035548001527786255, 3.895533561706543), (-0.5196972638368607, 4.141484975814819),
                                 (-1.0772297382354736, 4.382203578948975), (-1.6382399797439575, 4.614681005477905),
                                 (-2.20794141292572, 4.822925567626953), (-2.801669955253601, 4.950915575027466),
                                 (-3.3955925703048706, 5.07689094543457), (-3.992967128753662, 5.166588068008423),
                                 (-4.598506927490234, 5.121818542480469), (-5.201858282089233, 5.052990436553955),
                                 (-5.803656101226807, 4.971605062484741), (-6.4028966426849365, 4.874637126922607),
                                 (-6.930181980133058, 4.585408926010129), (-7.2630465030670175, 4.084510922431942),
                                 (-7.368319511413574, 3.48846697807312), (-7.138064861297607, 2.9441345930099487),
                                 (-6.619609117507935, 2.6371489763259888), (-6.026624917984009, 2.5179010033607483),
                                 (-5.421321630477905, 2.4689239263534546), (-4.816093921661377, 2.419008493423462),
                                 (-4.210949897766113, 2.368097484111786), (-3.6059085130691493, 2.3159834742546077),
                                 (-3.0010104179382324, 2.2622230052948), (-2.396325469017029, 2.206129491329193),
                                 (-1.7920175194740295, 2.146120548248291), (-1.1888505220413208, 2.075769066810608),
                                 (-0.6659398972988129, 1.8077430129051208), (-0.4352745898067951, 1.252098023891449),
                                 (-0.5128816515207291, 0.6738810986280441), (-1.1053279638290405, 0.6027795858681202),
                                 (-1.7060315012931824, 0.6901264190673828), (-2.312256097793579, 0.6939805597066879),
                                 (-2.831323027610779, 0.43881770968437195), (-2.8748650550842285, -0.15723134577274323),
                                 (-2.6617225408554077, -0.722334623336792), (-2.233074963092804, -1.1469694077968597),
                                 (-1.8114210367202759, -1.5823174715042114), (-1.5404115319252014, -2.1215705275535583),
                                 (-1.5179549157619476, -2.7235995531082153), (-1.7210304737091064, -3.2933980226516724),
                                 (-1.9128600358963013, -3.8599605560302734), (-1.8256959915161133, -4.4549479484558105),
                                 (-1.4326944947242737, -4.905786991119385), (-0.8669790029525757, -5.117151498794556),
                                 (-0.26290419697761536, -5.170000076293945), (0.3444003015756607, -5.174861669540405),
                                 (0.3444003015756607, -5.174861669540405), (0.951689600944519, -5.178654432296753),
                                 (1.5589675307273865, -5.181377649307251), (2.166237950325012, -5.183030128479004),
                                 (2.7735044956207275, -5.183609962463379), (3.380771517753601, -5.183118104934692),
                                 (3.988041520118714, -5.181550979614258), (4.595319509506226, -5.178909063339233),
                                 (5.202609539031982, -5.175189971923828), (5.809914588928223, -5.170393943786621),
                                 (6.414836883544922, -5.126328945159912), (6.982332944869995, -4.921492099761963),
                                 (7.335270166397095, -4.444735527038574), (7.323241949081421, -3.8437174558639526),
                                 (7.084682464599609, -3.289611577987671), (6.733030080795288, -2.7945034503936768),
                                 (6.382162809371948, -2.298838496208191), (6.03279709815979, -1.8021149635314941)]