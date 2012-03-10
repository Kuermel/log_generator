#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

import threading

BLOCK = True
QUEUE_BLOCK_SEC = 1

class ScenarioProcessorThread(threading.Thread):
    def __init__(self, callback, msg_queue):
        self.__callback = callback
        self.__msg_queue = msg_queue
        self.__no_shutdown = True
        threading.Thread.__init__(self)

    def run(self):
        while self.__no_shutdown:
            try:
                line = self.__msg_queue.get(BLOCK, QUEUE_BLOCK_SEC)
                if self.__callback:
                    self.__callback(line)
            except Exception, err:
                print "Exception:",err
                pass

    def shutdown(self):
        self.__no_shutdown = False


