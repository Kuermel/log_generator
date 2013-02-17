#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

import threading
import time

class ScenarioThread(threading.Thread):
    def __init__(self, scenario, q):
        self.__scenario = scenario
        self.__q = q
        self.__no_shutdown = True
        threading.Thread.__init__(self)

    def run(self):
        while self.__no_shutdown:
            line = self.__scenario.generate_one()
            self.__q.put(line)
            time.sleep(0.001)

    def getName(self):
        return self.__scenario.getName()

    def shutdown(self):
        self.__no_shutdown = False
