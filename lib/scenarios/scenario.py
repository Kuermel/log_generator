#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

import json

import os
from string import Template
from lib.scenarios.exceptions import ConfigurationError
from lib.scenarios.fields.from_list_file_field import FromListFileField
from lib.scenarios.fields.random_field import RandomField
import random
import pprint

class Scenario:
    def __init__(self, name, data_dir):
        self.__name = name
        self.__data_dir = data_dir
        self.__spec_file = '/'.join([self.__data_dir, name + '.spec'])
        if not os.path.exists(self.__spec_file):
            raise ConfigurationError("spec file not found")
        self.__fields = []
        self.__gen_data = {}
        self.__loadSpec()
        self.__initFields()
        self.templateCount = 0

    def getName(self):
        return self.__name

    def getFields(self):
        return self.__fields

    def generate_one(self):
        for field in self.__fields:
            self.__gen_data[field.getName()] = field.generate()
        for field_spec in self.__spec['fields']:
            for field_name in field_spec:
                if field_name == 'templateCount':
                    self.templateCount = int(field_spec[field_name]['count']) - 1
        randomCount = random.randint(0, self.templateCount)
        tpl = Template(self.__spec['template'][randomCount])
        return tpl.substitute(self.__gen_data)

    def __loadSpec(self):
        spec_txt = open(self.__spec_file, "r").read()
        self.__spec = json.loads(spec_txt)

    def __initFields(self):
        for field_spec in self.__spec['fields']:
            for field_name in field_spec:
                field_config = field_spec[field_name]
                if field_name == 'templateCount':
                    continue
                elif field_config['type'] == 'random':
                    self.__fields.append(RandomField(field_name, field_config['generate_type'], field_config))
                elif field_config['type'] == 'from_list_file':
                    self.__fields.append(FromListFileField(field_name, self.__data_dir + '/' + field_config['file'], field_config))

    def __str__(self):
        return "<scenario name=${self.__name}>"
