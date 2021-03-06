#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

from lib.scenarios.exceptions import ConfigurationError
from lib.scenarios.fields.generators.datetime_generator import DateTimeGenerator
from lib.scenarios.fields.generators.timestamp_generator import TimeStampGenerator
from lib.scenarios.fields.generators.integer_generator import IntegerGenerator
from lib.scenarios.fields.generators.ipv4_generator import Ipv4Generator
from lib.scenarios.fields.generators.local_ipv4_generator import LocalIpv4Generator


class RandomField:
    def __init__(self, name, generate_type, config):
        self.__name = name
        if generate_type == 'datetime':
            self.__gen_type = DateTimeGenerator(config)
        elif generate_type == 'timestamp':
            self.__gen_type = TimeStampGenerator(config)
        elif generate_type == 'integer':
            self.__gen_type = IntegerGenerator(config)
        elif generate_type == 'IPv4':
            self.__gen_type = Ipv4Generator(config)
        elif generate_type == 'LocalIPv4':
            self.__gen_type = LocalIpv4Generator(config)
        else:
            raise ConfigurationError("generate type not found")

    def getName(self):
        return self.__name

    def generate(self):
        return self.__gen_type.generate()