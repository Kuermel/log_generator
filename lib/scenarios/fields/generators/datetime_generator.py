#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

import datetime

class DateTimeGenerator:
    def __init__(self, config):
        if config.has_key("format"):
            self.__format = config['format']
        else:
            self.__format = "%Y/%m/%d %H:%M:%S"

    def generate(self):
        return datetime.datetime.now().strftime(self.__format)