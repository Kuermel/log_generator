#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

from lib.scenarios.test_helper import is_valid_ipv4
import unittest
from lib.scenarios.fields.generators.ipv4_generator import Ipv4Generator

FORMAT = "%Y/%m/%d %H:%M:%S"

class Ipv4GeneratorTestCase(unittest.TestCase):
    def test_generate(self):
        s = Ipv4Generator({})
        self.assertTrue(is_valid_ipv4(s.generate()))

if __name__ == '__main__':
    unittest.main()
