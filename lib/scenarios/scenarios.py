#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

import multiprocessing
import os
from lib.scenarios.scenario import Scenario
from lib.scenarios.scenario_processor_thread import ScenarioProcessorThread
from lib.scenarios.scenario_thread import ScenarioThread

QUEUE_SIZE = 100000
SCENARIO_DIRECTORY = '../../scenarios/'

class Scenarios:
    def __init__(self, scenario_directory=SCENARIO_DIRECTORY, eps=1000):
        self.__scenario_directory = scenario_directory
        self.__eps = eps
        self.__scenarios = {}
        self.__threads = []
        self.__msg_queue = multiprocessing.JoinableQueue(QUEUE_SIZE)
        self.__init_scenarios()
        pass

    def getScenarios(self):
       return self.__scenarios

    def getScenario(self, name):
        return self.__scenarios.get(name)

    def start(self, _scenario = 'all'):
        print _scenario
        for t in self.__threads:
            for scenario in _scenario.split(','):
                _parts = scenario.split(':')
                name = _parts[0]
                source_ip = None
                if len(_parts) == 2:
                    name = _parts[0]
                    source_ip = _parts[1]

                if name == 'all' or name == t.getName():
                    print "Staring scenario:", t.getName(), "source_ip", source_ip
                    t.set_source_ip(source_ip)
                    t.start()

    def setProcessor(self,callback):
        self.__processorThread = ScenarioProcessorThread(callback,self.__msg_queue, self.__eps)
        self.__processorThread.start()

    def shutdown(self):
        for t in self.__threads:
            t.shutdown()
        if self.__processorThread:
            self.__processorThread.shutdown()

    def __init_scenarios(self):
        for dirname, dirnames,filenames in os.walk(self.__scenario_directory):
            for name in dirnames:
                s = Scenario(name, '/'.join([self.__scenario_directory,name]))
                self.__scenarios[name] = s

        for name in self.__scenarios:
            t = ScenarioThread(self.__scenarios[name], self.__msg_queue, self.__eps)
            self.__threads.append(t)

