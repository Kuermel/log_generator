#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
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

ROOTDIR = os.path.dirname(os.path.realpath(__file__))

def shutdown(signal, frame):
    global s
    s.shutdown()
    sys.exit(0)

def start():
    global s,server,output
    s = Scenarios(ROOTDIR+'/scenarios/')
    if output == "syslog":
        s.setProcessor(processor_syslog)
    else:
        s.setProcessor(processor_stdout)

    s.start()

    while 1:
        time.sleep(1)

def usage():
    print ""
    print "./start.sh -o syslog -s 192.168.1.10"
    print "./start.sh -o stdout"
    print ""

def getcmd_options():
    global server,output

    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:s:", ["output", "server"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    output = "stdout"
    server = ""
    for o,a in opts:
        if o in ("-o", "--output"):
            output = a
        elif o in ("-s", "--server"):
            server = a
        else:
            assert False, "unknown options"

    if output == "syslog" and server == "":
        print "Provide the syslog server with -s",server
        usage()
        sys.exit(2)


def processor_stdout(line):
    print line

def processor_syslog(line):
    global server
    syslog.udp_send(line, host=server)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)
    getcmd_options()
    start()
