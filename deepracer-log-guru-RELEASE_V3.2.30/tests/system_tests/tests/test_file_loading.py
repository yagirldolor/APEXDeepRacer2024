#
# DeepRacer Guru
#
# Version 4.0 onwards
#
# Copyright (c) 2023 dmh23
#
import filecmp
import json
import os
import unittest
from typing import Union

from src.log.log import Log
from system_tests.tests.dummy_please_wait import DummyPleaseWait
from tracks.fumiaki_loop_2020_track import FumiakiLoop2020Track
from tracks.reinvent_2018_track import Reinvent2018Track
from tracks.reinvent_2022_track import Reinvent2022Track

RESOURCE_DIR = os.path.join(os.path.dirname(__file__), "..", "resources", "file_parsing")
INPUT_FILES_DIR = os.path.join(RESOURCE_DIR, "input_log_files")
META_FILES_DIR = os.path.join(RESOURCE_DIR, "expected_output")

EXPECTED_MULTI_META = os.path.join(os.path.dirname(__file__), "..", "resources", "file_loading")

FILE_EXTENSION = ".meta.json"


class TestFileLoadingOfAllEpisodes(unittest.TestCase):
    def test_load_single_short_log_file(self):
        expected_step_counts = [139, 141, 142, 87, 156, 132, 138, 144, 143, 137, 133, 144, 147, 141, 133, 141, 140,
                                142, 131, 138]
        expected_quarters = [1] * 5 + [2] * 5 + [3] * 5 + [4] * 5
        self._test_load_episodes("training-20220721141556-OUjJCTWHR7SeYQs_-7xc4A-robomaker.log",
                                 Reinvent2018Track,
                                 expected_step_counts, expected_quarters)

    def test_load_two_worker_log_files(self):
        expected_step_counts = [25, 24, 25, 27, 15, 35, 22, 20, 22, 25,
                                44, 34, 22, 25, 23, 18, 25, 2, 22, 35,
                                60, 34, 38, 41, 20, 33, 16, 17, 26, 25,
                                12, 20, 25, 27, 19, 17, 16, 21, 26, 21,
                                20, 26, 19, 19, 19, 22, 20, 50, 27, 22,
                                27, 26, 24, 36, 21, 35, 18, 15, 27, 23,
                                54, 17, 18, 38, 21, 17, 17, 14, 18, 42,
                                39, 30, 29, 24, 26, 22, 16, 30, 23, 20,
                                37]

        expected_quarters = [1] * 20 + [2] * 20 + [3] * 21 + [4] * 20
        log = self._test_load_episodes(["deepracer-0_robomaker.1.mh77xxe01xgkyky72m378gnwp.log",
                                        "deepracer-0_robomaker.2.pleai77ybzcn6yor58nl46ic7.log"],
                                       Reinvent2022Track,
                                       expected_step_counts, expected_quarters)

        self._verify_log_meta_json(log, "test_load_two_worker_log_files.json")

    def test_load_four_worker_log_files(self):
        expected_step_counts = [165, 183, 391, 73, 366, 26, 50, 364, 195, 240,
                                95, 76, 386, 78, 362, 277, 51, 332, 272, 361,
                                360, 140, 371, 371, 112, 118, 46, 190, 200, 314,
                                368, 53, 66, 30, 376, 29, 103, 367, 238, 154,
                                75, 52, 360, 381, 39, 174, 51,
                                238, 179, 80, 71, 33, 363, 374,
                                146, 129, 79, 126, 31, 31, 89, 290, 365, 87,
                                66, 126, 141, 87, 112, 27, 120, 38, 29, 158]

        expected_quarters = [1] * 18 + [2] * 19 + [3] * 19 + [4] * 18
        log = self._test_load_episodes(["deepracer-0_robomaker.1.qwctpyyzmr74z3u19kc8pskvh.log",
                                        "deepracer-0_robomaker.2.439iylb5afjhz7nl8by8yr9p2.log",
                                        "deepracer-0_robomaker.3.kngqw8no1z62pkyozmqqnocad.log",
                                        "deepracer-0_robomaker.4.4fswvtmen73c861vyh3zwuv9c.log"],
                                       FumiakiLoop2020Track,
                                       expected_step_counts, expected_quarters)

        self._verify_log_meta_json(log, "test_load_four_worker_log_files.json")

        # Should be the 11th step of the 3rd episode in 2nd worker
        # SIM_TRACE_LOG:2,11,-7.9529,-0.2597,27.0350,-30.00,1.00,4,25.0000,False,True,1.1486,75,52.87,39.632,in_progress,0.00
        # 75 : 62 45
        # B - Bonus fast section
        sample_episode = log.get_episodes()[12]
        sample_event = sample_episode.events[10]
        self.assertEqual(12, sample_episode.id)
        self.assertEqual(12, sample_event.episode)
        self.assertEqual(11, sample_event.step)
        self.assertEqual("\n75 : 62 45\nB - Bonus fast section\n", sample_event.debug_log)
        self.assertEqual(39.632, sample_event.time)
        self.assertEqual(3, sample_event.sequence_count)
        self.assertEqual("R", sample_event.track_side)
        self.assertEqual(3.7, round(sample_event.projected_travel_distance, 1))
        self.assertTrue(sample_event.all_wheels_on_track)
        self.assertEqual(1.0, round(sample_event.track_speed, 1))

        # Last step in the last episode of the last worker
        # SIM_TRACE_LOG:19,158,-0.3655,2.3368,-40.3193,-5.00,4.00,2,0.1000,True,False,49.6239,140,52.87,557.678,off_track,0.00
        # ERROR - Going directly off track
        sample_episode = log.get_episodes()[-1]
        sample_event = sample_episode.events[-1]
        self.assertEqual(73, sample_episode.id)
        self.assertEqual(73, sample_event.episode)
        self.assertEqual(158, sample_event.step)
        self.assertEqual("\nERROR - Going directly off track\n", sample_event.debug_log)
        self.assertEqual(557.678, sample_event.time)
        self.assertEqual(5, sample_event.sequence_count)
        self.assertEqual("L", sample_event.track_side)
        self.assertEqual(0.0, round(sample_event.projected_travel_distance, 1))
        self.assertFalse(sample_event.all_wheels_on_track)
        self.assertEqual(2.4, round(sample_event.track_speed, 1))

    def _test_load_episodes(self, filenames: Union[str, list], track_type: type, expected_step_counts: list,
                            expected_quarters: list) -> Log:
        # Check valid test case & basic environment
        self.assertEqual(len(expected_quarters), len(expected_step_counts))  # Ensure valid test case
        self.assertTrue(os.path.isdir(INPUT_FILES_DIR))
        if isinstance(filenames, str):
            filenames = [filenames]
        for f in filenames:
            self.assertTrue(os.path.isfile(os.path.join(INPUT_FILES_DIR, f)))

        # Setup meta JSON files, by copying from expected output of the other tests and reinstate the
        # mtime and ctime back to the values of the file in the meta JSON rather than the test placeholder values

        meta_filenames = []
        for f in filenames:
            meta_filename = f + FILE_EXTENSION
            meta_filenames.append(meta_filename)

            log = Log(META_FILES_DIR)
            log.load_meta(meta_filename)
            meta = log.get_log_meta()
            meta.file_mtime.allow_modifications()
            meta.file_ctime.allow_modifications()
            meta_os_stats = os.stat(os.path.join(INPUT_FILES_DIR, f))
            meta.file_mtime.set(meta_os_stats.st_mtime)
            meta.file_ctime.set(meta_os_stats.st_ctime)
            log.save(INPUT_FILES_DIR)

        all_tracks = {}
        track = track_type()
        track.prepare(all_tracks)

        # Execute
        please_wait = DummyPleaseWait(self)
        log = Log(INPUT_FILES_DIR)
        if len(meta_filenames) == 1:
            log.load_all(meta_filenames[0], please_wait, track)
        else:
            log.load_all(meta_filenames, please_wait, track)

        # Tear down
        for f in filenames:
            os.remove(os.path.join(INPUT_FILES_DIR, f + FILE_EXTENSION))

        # Verify
        self.assertEqual(0, round(please_wait.start_percent))
        self.assertEqual(100, please_wait.current_percent)
        self.assertEqual(log.get_log_meta().episode_count.get(), len(log.get_episodes()))
        self.assertEqual(len(expected_step_counts), len(log.get_episodes()))
        for index, e in enumerate(log.get_episodes()):
            self.assertEqual(expected_step_counts[index], e.step_count)
            self.assertEqual(expected_quarters[index], e.quarter)
            self.assertEqual(index, e.id)

        # Return for additional specific validation
        return log

    def _verify_log_meta_json(self, log: Log, expected_json_filename: str):
        actual_json_output_file = os.path.join(INPUT_FILES_DIR, "Multi_meta.json")
        expected_json_output_file = os.path.join(EXPECTED_MULTI_META, expected_json_filename)
        log.get_log_meta().file_ctime.allow_modifications()
        log.get_log_meta().file_mtime.allow_modifications()
        log.get_log_meta().file_ctime.set(123.456)
        log.get_log_meta().file_mtime.set(1234.5678)
        with open(actual_json_output_file, "w+") as meta_file:
            log_json = log._log_meta.get_as_json()
            json.dump(log_json, meta_file, indent=2)

        self.assertTrue(filecmp.cmp(expected_json_output_file, actual_json_output_file, shallow=False),
                        "Incorrect multi JSON")
        os.remove(actual_json_output_file)

# 25, 24, 25, 27, 15, 35, 22, 20, 22, 25
# 60, 34, 38, 41, 20, 33, 16, 17, 26, 25
# 20, 26, 19, 19, 19, 22, 20, 50, 27, 22
# 54, 17, 18, 38, 21, 17, 17, 14, 18, 42
# ----
# 14 UNFINISHED *****


############################################

# 44, 34, 22, 25, 23, 18, 25, 2, 22, 35
# 12, 20, 25, 27, 19, 17, 16, 21, 26, 21
# 27, 26, 24, 36, 21, 35, 18, 15, 27, 23
# 39, 30, 29, 24, 26, 22, 16, 30, 23, 20
# 37
