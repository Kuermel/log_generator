#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#

import random

class MacGenerator:
    def __init__(self, config):
        pass

    def generate(self):
        mac = [ 0x00, random.randint(0x00, 0x24), random.randint(0x00, 0x81),random.randint(0x00, 0x7f),random.randint(0x00, 0xff),random.randint(0x00, 0xff) ]
        return ':'.join(map(lambda x: "%02x" % x, mac))
