#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
from threading import Timer

__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

import socket

FACILITY = {
    'kern': 0, 'user': 1, 'mail': 2, 'daemon': 3,
    'auth': 4, 'syslog': 5, 'lpr': 6, 'news': 7,
    'uucp': 8, 'cron': 9, 'authpriv': 10, 'ftp': 11,
    'local0': 16, 'local1': 17, 'local2': 18, 'local3': 19,
    'local4': 20, 'local5': 21, 'local6': 22, 'local7': 23,
}

LEVEL = {
    'emerg': 0, 'alert': 1, 'crit': 2, 'err': 3,
    'warning': 4, 'notice': 5, 'info': 6, 'debug': 7
}

count = 0
old_count = 0
def udp_send(message, level=LEVEL['notice'], facility=FACILITY['daemon'],
             host='localhost', port=port):
    global count
    source_ip = message[0]
    if not source_ip:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = '<%d>%s' % (level + facility * 8, message[1])
        sock.sendto(data, (host, port))
        sock.close()
    else:
        from scapy.all import IP,UDP,send,conf
        conf.sniff_promisc = False
        conf.promisc = False

        data = '<%d>%s' % (level + facility * 8, message[1])
        payload = str(data)
        pkg=IP(src=source_ip, dst=host)/UDP(dport=port)/payload
        send(pkg)

    count += 1


def stat():
    global count
    eps = count / 20
    count = 0
    print 'eps:%d' % eps
    t = Timer(20, stat)
    t.daemon = True
    t.start()

stat()
