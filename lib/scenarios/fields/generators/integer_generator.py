#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

from lib.scenarios.exceptions import ConfigurationError
import random

class IntegerGenerator:
    def __init__(self, config):
        self.__min = config['min']
        self.__max = config['max']
        if self.__min > self.__max:
            raise ConfigurationError("min value greater than max value")
        pass

    def generate(self):
        return random.randint(self.__min, self.__max)

