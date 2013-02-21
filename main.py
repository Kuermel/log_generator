#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
import random

__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

import getopt
import os
import signal
import time
import sys
from lib.scenarios.scenarios import Scenarios
from lib.transport import syslog
from lib.transport import zeromq

ROOTDIR = os.path.dirname(os.path.realpath(__file__))
period = 1

def shutdown(signal, frame):
    global s
    s.shutdown()
    sys.exit(0)

def start():
    global s,server,output,bind_point,_scenario
    s = Scenarios(ROOTDIR+'/scenarios/', period=period)
    if output == "syslog":
        s.setProcessor(processor_syslog)
    elif output == "zeromq":
        zeromq.init_sockets(bind_point)
        s.setProcessor(zeromq.send)
    else:
        s.setProcessor(processor_stdout)

    s.start(_scenario)

    while 1:
        time.sleep(1)

def usage():
    print ""
    print "./start.sh -e all -o syslog -s 192.168.1.10"
    print "./start.sh -e all -o zeromq -b 'tcp://*:9000'"
    print "./start.sh -e all -o stdout"
    print ""

def getcmd_options():
    global server,output,bind_point,_scenario, period

    try:
        opts, args = getopt.getopt(sys.argv[1:], "e:o:s:b:p:", ["scenario","output", "server","bind_point","eps"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    output = "stdout"
    server = ""
    bind_point = ""
    _scenario = "all"
    for o,a in opts:
        if o in ("-o", "--output"):
            output = a
        elif o in ("-s", "--server"):
            server = a
        elif o in ("-b", "--bind_point"):
            bind_point = a
        elif o in ("-e", "--scenario"):
            _scenario = a
        elif o in ("-p", "--eps"):
            try:
                eps = float(a)
                period = 1/eps
                offset = period*0.15
                period = period-offset
            except:
                pass
        else:
            assert False, "unknown options"

    if output == "syslog" and server == "":
        print "Provide the syslog server with -s",server
        usage()
        sys.exit(2)
    if output == "zeromq" and bind_point == "":
        print "Provide the bind_point for zeromq with -b",server
        usage()
        sys.exit(2)


def processor_stdout(line):
    print line

def processor_syslog(line):
    global server
    syslog.udp_send(line, host=server)

def processor_zeromq(line):
    zeromq.send(line)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)
    getcmd_options()
    start()
