#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
from Queue import Empty
import copy
import traceback

__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

import threading
import time

BLOCK = True
QUEUE_BLOCK_SEC = 1

total_count = 1
drop_percent = 0


class ScenarioProcessorThread(threading.Thread):
    def __init__(self, callback, msg_queue, eps):
        self.__callback = callback
        self.__msg_queue = msg_queue
        self.__no_shutdown = True
        self.__eps = eps
        self.old_total = 0
        self.eps = 0
        self.wait_time = float(0)

        threading.Thread.__init__(self)

    def adjust_drop_rate(self):
        global total_count, drop_percent
        # if total_count > 0:
        # drop_percent = 100 - (int(self.__eps) * 100) / total_count
        # if drop_percent < 0:
        # drop_percent = 0
        # elif drop_percent == 100:
        # drop_percent = 99
        #
        # print drop_percent, total_count
        # total_count = 1
        self.eps = total_count
        self.old_total = total_count
        total_count = 0

        if self.eps < self.__eps:
            self.wait_time = self.wait_time - 0.0001
        elif self.eps > self.__eps:
            self.wait_time = self.wait_time + 0.0001
        if self.wait_time < 0:
            self.wait_time = 0.00001

        # print 'eps:', self.eps, self.wait_time
        t = threading.Timer(1, self.adjust_drop_rate)
        t.daemon = True
        t.start()

    def run(self):
        global total_count, drop_percent
        self.adjust_drop_rate()

        if self.__eps != 0:
            self.wait_time = (1.0 / self.__eps)
        while self.__no_shutdown:

            try:
                # if drop_percent > 0 and (total_count % 100) < drop_percent:
                # time.sleep(0.00001)
                # continue

                if self.__eps != 0:
                    time.sleep(self.wait_time)

                line = self.__msg_queue.get(BLOCK)
                # print total_count, line
                if self.__callback:
                    self.__callback(line)
                    total_count += 1
            except Empty:
                pass
            except Exception, err:
                print "Exception:", err
                print traceback.format_exc()


    def shutdown(self):
        self.__no_shutdown = False


