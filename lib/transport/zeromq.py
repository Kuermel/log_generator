#
# Copyright (c) Innotim Yazilim Telekomunikasyon ve Danismanlik Ticaret LTD. STI.
# All rights reserved.
#
import zmq

__author__ = 'Ozan Turksever (ozan.turksever@logsign.net)'
__copyright__ = 'Copyright (c) 2012 Innotim Yazilim Ltd.'
__license__ = 'GPLv2'
__version__ = '0.0.1'



publisher = None
def init_sockets(bind_point):
    global publisher
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind(bind_point)
    print publisher

def send(msg):
    global publisher
    publisher.send_unicode(msg)
