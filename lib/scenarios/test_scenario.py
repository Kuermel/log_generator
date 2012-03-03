#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

from datetime import datetime
import os
import re
import shutil
import unittest
from lib.scenarios.scenarios import Scenario
from lib.scenarios import test_helper
from lib.scenarios.test_helper import is_valid_ipv4

class ScenarioTestCase(unittest.TestCase):
    def setUp(self):
        self.__scenarios_dir = '/tmp/scenarios'
        self.__name = test_helper.SCENARIO1
        if os.path.exists(self.__scenarios_dir):
            shutil.rmtree(self.__scenarios_dir)
        os.makedirs(self.__scenarios_dir)
        self.__scenario_data_dir = self.__scenarios_dir+'/'+self.__name
        test_helper.setupScenario(self.__name, self.__scenario_data_dir, test_helper.SENARIO_SPEC_1)

        self.__scenario = Scenario(self.__name, self.__scenario_data_dir)

    def tearDown(self):
        shutil.rmtree(self.__scenarios_dir)

    def test_check_field_count(self):
        fields = self.__scenario.getFields()
        self.assertEqual(8, len(fields))

    def test_generate_one(self):
        log = self.__scenario.generate_one()
        regexp = r'date="(?P<date>.*)" src="(?P<src>.*)" dst="(?P<dst>.*)" recv="(?P<recv>.*)" sent="(?P<sent>.*)" user_agent="(?P<user_agent>.*)" respond_code="(?P<respond_code>.*)"'
        m = re.match(regexp,log)
        self.assertTrue(m)
        date = m.group('date')
        self.assertEqual(datetime.strptime(date, "%Y/%m/%d %H:%S:%M").strftime("%Y/%m/%d %H:%S:%M"), date)
        src = m.group('src')
        self.assertTrue(is_valid_ipv4(src))
        dst = m.group('dst')
        self.assertTrue(is_valid_ipv4(dst))
        recv = int(m.group('recv'))
        self.assertLessEqual(recv, 1000000)
        sent = int(m.group('sent'))
        self.assertLessEqual(sent, 1000000)

if __name__ == '__main__':
    unittest.main()
