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
from lib.transport import zeromq
from lib.transport import es

ROOTDIR = os.path.dirname(os.path.realpath(__file__))
output = "stdout"
server = ""
bind_point = ""
_scenario = "all"
_eps = 100
_eps_wave = True
port = 514


def shutdown(signal, frame):
    global s
    os._exit(0)
    # s.shutdown()
    # sys.exit(0)


def start():
    global s, server, output, bind_point, _scenario, _eps, _eps_wave, port
    s = Scenarios(ROOTDIR + '/scenarios/', eps=_eps, eps_wave=_eps_wave, output=output, port=port)
    if output == "syslog":
        s.setProcessor(processor_syslog)
    elif output == "zeromq":
        zeromq.init_sockets(bind_point)
        s.setProcessor(zeromq.send)
    elif output == "es":
        s.setProcessor(processor_es)
    else:
        s.setProcessor(processor_stdout)

    s.start(_scenario)

    while 1:
        time.sleep(1)


def usage():
    print ""
    print "./start.sh -e all -o syslog -s 192.168.1.10 -P 514"
    print "./start.sh -e all -o zeromq -b 'tcp://*:9000'"
    print "./start.sh -e all -o stdout"
    print ""
    print "-p eps"
    print "-e scenario"


def getcmd_options():
    global server, output, bind_point, _scenario, _eps, _eps_wave, port

    try:
        opts, args = getopt.getopt(sys.argv[1:], "e:o:s:b:p:P:", ["scenario", "output", "server", "bind_point", "eps", "port"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    output = "stdout"
    server = ""
    bind_point = ""
    _scenario = "all"
    for o, a in opts:
        if o in ("-o", "--output"):
            output = a
        elif o in ("-s", "--server"):
            server = a
        elif o in ("-P", "--port"):
            port = a
        elif o in ("-b", "--bind_point"):
            bind_point = a
        elif o in ("-e", "--scenario"):
            _scenario = a
        elif o in ("-p", "--eps"):
            _eps = float(a)
        elif o in ("-w", "--eps_wave"):
            if a == 'no':
                _eps_wave = True
        else:
            assert False, "unknown options"

    if output == "syslog" and server == "":
        print "Provide the syslog server with -s", server
        usage()
        sys.exit(2)
    if output == "es" and server == "":
        print "Provide the es server with -s", server
        usage()
        sys.exit(2)
    if output == "zeromq" and bind_point == "":
        print "Provide the bind_point for zeromq with -b", server
        usage()
        sys.exit(2)


def processor_stdout(line):
    print line


def processor_syslog(line):
    global server
    syslog.udp_send(line, host=server, port=port)


def processor_es(line):
    global server
    parts = server.split(':')
    _port = 9200
    if len(parts) == 1:
        _host = server
    elif len(parts) == 2:
        _host = parts[0]
        _port = int(parts[1])

    es.send(line, host=_host, port=_port)


def processor_zeromq(line):
    zeromq.send(line)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)
    getcmd_options()
    start()
