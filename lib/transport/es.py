#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
import json
import pprint
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
    global count
    doc = line[1]
    url = 'http://%s:%s/%s/%s' % (host, port, doc.get('_dst_index', datetime.datetime.now().strftime("log_%Y%m%d")), doc.get('_es_type', 'nastedlog'))
    pprint.pprint(doc)
    resp = requests.post(url, data=json.dumps(doc))
    print resp.text
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
