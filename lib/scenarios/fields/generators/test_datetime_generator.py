#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

from datetime import datetime

FORMAT = "%Y/%m/%d %H:%M:%S"

__author__ = 'ozanturksever'

import unittest
from lib.scenarios.fields.generators.datetime_generator import DateTimeGenerator

class DateTimeTestCase(unittest.TestCase):
    def test_generate(self):
        config = {"format": FORMAT}
        s = DateTimeGenerator(config)
        result = s.generate()
        converted = datetime.strptime(result, FORMAT).strftime(FORMAT)
        self.assertEqual(converted, result)


if __name__ == '__main__':
    unittest.main()
