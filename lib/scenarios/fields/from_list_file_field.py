#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

from random import randint
from lib.scenarios.exceptions import ConfigurationError

class FromListFileField:

    def __init__(self, name, file, method_config):
        self.__name = name
        self.__file = file
        self.__method = method_config['method']
        self.__method_config = method_config
        self.__cursorPos = 0
        self.__data = []
        self.__load()
        self.__ratioCounter = 0
        if self.__method == 'ratio':
            self.__setupRatios(method_config)



    def getName(self):
        return self.__name

    def generate(self):
        return self.getOneLine()

    def getOneLine(self):
        if self.__method == 'sequential':
            return self.__getOneLineSquential()
        elif self.__method == 'random':
            return self.__getOneLineRandom()
        elif self.__method == 'ratio':
            return self.__getOneLineRatio()

    def __getOneLineSquential(self):
        line = self.__data[self.__cursorPos]
        self.__incrCursor()
        return line

    def __getOneLineRandom(self):
        rPos = randint(0, self.__data_len-1)
        return self.__data[rPos]

    def __getOneLineRatio(self):
        segment = self.__ratioCounter % 100
        for (low,high) in self.__bounds:
            if segment >= low and segment < high:
                break
        self.__ratioCounter+=1
        rPos = randint(low, high-1)
        return self.__data[rPos]

    def __load(self):
        fd = open(self.__file,"r")
        for line in fd:
            self.__data.append(line.strip())
        fd.close()
        self.__data_len = len(self.__data)

    def __incrCursor(self):
        if self.__data_len == self.__cursorPos:
            self.__cursorPos = 0
        else:
            self.__cursorPos += 1

        if self.__data_len == self.__cursorPos:
            self.__cursorPos = 0

    def __setupRatios(self, method_config):
        ratios = method_config['ratio'].split(',')
        total = 0
        self.__bounds = []
        high_bound = 0
        low_bound = 0
        for v in ratios:
            percent = int(v)
            if high_bound>0:
                low_bound = high_bound+1;
            high_bound += (percent*self.__data_len)/100
            self.__bounds.append((low_bound,high_bound))
            total += percent
        if total > 100:
            raise ConfigurationError("total can't be greater than 100")
        if total < 100:
            raise ConfigurationError("total can't be lower than 100")
