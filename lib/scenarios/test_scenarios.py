#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#

__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

import os
import shutil
from lib.scenarios.scenarios import Scenarios, Scenario
from lib.scenarios import test_helper

import unittest

class ScenariosTestCase(unittest.TestCase):
    def setUp(self):
        self.__scenarios_dir = '/tmp/scenarios'
        if os.path.exists(self.__scenarios_dir):
            shutil.rmtree(self.__scenarios_dir)
        os.makedirs(self.__scenarios_dir)
        test_helper.setupScenario(test_helper.SCENARIO1, self.__scenarios_dir+'/'+test_helper.SCENARIO1, test_helper.SENARIO_SPEC_1)
        test_helper.setupScenario(test_helper.SCENARIO2, self.__scenarios_dir+'/'+test_helper.SCENARIO2, test_helper.SENARIO_SPEC_1)
        self.scenarios = Scenarios(scenario_directory=self.__scenarios_dir)

    def tearDown(self):
        shutil.rmtree(self.__scenarios_dir)

    def test_can_get_scenario_list(self):
        list = self.scenarios.getScenarios()
        self.assertEqual([test_helper.SCENARIO1, test_helper.SCENARIO2],sorted(list))

    def test_can_get_scenario(self):
        scenario = self.scenarios.getScenario(test_helper.SCENARIO1)
        self.assertEqual(test_helper.SCENARIO1, scenario.getName())

if __name__ == '__main__':
    unittest.main()
