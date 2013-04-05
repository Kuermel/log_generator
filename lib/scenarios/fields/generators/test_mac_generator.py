#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#

import unittest,re
from lib.scenarios.fields.generators.mac_generator import MacGenerator

mac_regexp = re.compile(r'^([a-fA-F0-9]{2}[:|\-]?){5}[a-fA-F0-9]{2}$')

class MacGeneratorTestCase(unittest.TestCase):
    def test_generate(self):
        s = MacGenerator({})

if __name__ == '__main__':
    unittest.main()
