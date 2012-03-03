#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

import unittest
from lib.scenarios.exceptions import ConfigurationError
from lib.scenarios.fields.generators.integer_generator import IntegerGenerator

MIN = 1
MAX = 10

class IntegerTestCase(unittest.TestCase):
    def test_generate(self):
        config = {"min": MIN, "max": MAX}
        result = IntegerGenerator(config).generate()
        self.assertGreaterEqual(result, MIN)
        self.assertLessEqual(result, MAX)

    def test_min_gt_max(self):
        config = {"min": MAX, "max": MIN}
        self.assertRaises(ConfigurationError, IntegerGenerator, config)


if __name__ == '__main__':
    unittest.main()
