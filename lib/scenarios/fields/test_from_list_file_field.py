#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

import os
from unittest import TestCase
import unittest
from lib.scenarios.fields.from_list_file_field import FromListFileField

TEST_LIST_CONTENT = "line0\nline1\n"
TMP_TEST_LIST = "/tmp/test.list"
TMP_TEST_LIST2 = "/tmp/test2.list"

class TestFromListFileField(TestCase):
    def setUp(self):
        list_file = open(TMP_TEST_LIST,"w")
        list_file.write(TEST_LIST_CONTENT)
        list_file.close()

    def tearDown(self):
        os.unlink(TMP_TEST_LIST)
        if os.path.exists(TMP_TEST_LIST2):
            os.unlink(TMP_TEST_LIST2)

    def test_get_line_sequential(self):
        s = FromListFileField("test", TMP_TEST_LIST, {"method":"sequential"})
        line = s.getOneLine()
        self.assertEqual("line0", line)
        line = s.getOneLine()
        self.assertEqual("line1", line)

    def test_can_seek_to_top(self):
        s = FromListFileField("test",TMP_TEST_LIST, {"method":"sequential"})
        line = s.getOneLine()
        self.assertEqual("line0", line)
        line = s.getOneLine()
        self.assertEqual("line1", line)
        line = s.getOneLine()
        self.assertEqual("line0", line)

    def test_get_line_random(self):
        s = FromListFileField("test",TMP_TEST_LIST, {"method":"random"})
        first_match_count = 0
        for i in range(100):
            line = s.getOneLine()
            if line == 'line0':
                first_match_count += 1

        second_match_count = 0
        for i in range(100):
            line = s.getOneLine()
            if line == 'line0':
                second_match_count += 1

        self.assertFalse(first_match_count == second_match_count)
        self.assertGreater(first_match_count,0)

    def test_get_line_ratio_20_80(self):
        list_file = open(TMP_TEST_LIST2,"w")
        for i in [0,0,1,1,1,1,1,1,1,1]:
            list_file.write(str(i)+"\n")
        list_file.close()

        s = FromListFileField("test", TMP_TEST_LIST2, {"method":"ratio", "ratio":"20,80"})
        match_count = 0
        for i in range(10):
            line = s.getOneLine()
            if line == '0':
                match_count += 1

        self.assertEqual(2, match_count)

    def test_get_line_ratio_20_60_20(self):
        list_file = open(TMP_TEST_LIST2,"w")
        for i in [0,0,1,1,1,1,1,1,2,2]:
            list_file.write(str(i)+"\n")
        list_file.close()

        s = FromListFileField("test", TMP_TEST_LIST2, {"method":"ratio", "ratio":"20,80"})
        (match_count,match_count2) = (0,0)
        for i in range(10):
            line = s.getOneLine()
            if line == '0':
                match_count += 1
            if line == '2':
                match_count2 +=1

        self.assertEqual(2, match_count)
        self.assertEqual(2, match_count)

