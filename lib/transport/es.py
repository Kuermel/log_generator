#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
import json
from threading import Timer
import datetime
import requests

__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'

count = 0
old_count = 0


def send(line, host='localhost', port=9200):
    global count, manager
    doc = line[1]
    url = 'http://%s:%s/%s/%s' % (host, port, doc.get('_dst_index', datetime.datetime.now().strftime("log_%Y%m%d")), doc.get('_es_type', 'nastedlog'))
    requests.post(url, data=json.dumps(doc))
    msg = {'data': doc}
    send_socket('alarmflow', msg)
    count += 1


def send_socket(socket_name, msg):
    global manager
    try:
        manager.send(socket_name + '_instance0', socket_name, msg)
    except NameError:
        from flow import manager
        manager.send(socket_name + '_instance0', socket_name, msg)
    except:
        pass


def stat():
    global count, manager
    eps = count / 20
    count = 0
    print 'eps:%d' % eps
    t = Timer(20, stat)
    t.daemon = True
    t.start()


stat()
