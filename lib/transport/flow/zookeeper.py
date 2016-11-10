import json
import logbook
from logbook.compat import redirect_logging
import logging
import os
import random
import signal
import socket
import time

ztimeout = 15.0

redirect_logging()

from kazoo.client import KazooClient

zk = None
zk_write_funcs_replaced = False
log = logbook.Logger('zookeeper')
current_state = None


def connection_state(state):
    global current_state
    log.warn('zookeeper state:%s' % state)
    current_state = state


def start(servers=None, force_reconnect=False):
    global zk
    log.warn('start zookeeper current:%s' % zk)
    if zk and not force_reconnect:
        return
    server_list = []
    if not servers:
        try:
            with open('/opt/cluster/zookeeper_addresses.json') as f:
                info = json.loads(f.read())
                for s in info.get('cluster'):
                    server_list.append('%s:2181' % s.split(':')[0])
        except:
            pass
        if len(server_list) == 0:
            server_list.append('127.0.0.1:2181')

        servers = str(','.join(server_list))
    else:
        server_list = servers.split(',')

    def pick_server():
        for t in xrange(len(server_list)):
            server = server_list[random.randint(0, len(server_list) - 1)]
            try:
                host, port = server.split(':')
            except:
                host, port = server, 2181
            try:
                log.warn('checking service %s:%s' % (host, port))
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect((str(host), int(port)))
                s.close()
                log.warn('checking service %s:%s success' % (host, port))
                return server
            except:
                log.warn('checking service %s:%s failed' % (host, port))
                continue


    log.warn('Zookeeper connect to: %s connect' % (servers))
    logger = logging.getLogger('kazoo')
    logger.setLevel(logging.WARNING)
    zk = KazooClient(hosts=servers, timeout=ztimeout, logger=logger)
    zk.add_listener(connection_state)
    zk.start(timeout=ztimeout) # zk *1000 ile carpiyor, carpmamali.
    log.warn('connected')

    wait_time = 0
    while True:
        log.warn('wait %s' % current_state)
        if current_state == 'CONNECTED':
            log.warn('return')
            break
        if wait_time > 10:
            log.warn('wait too much killing myself')
            os.kill(os.getpid(), signal.SIGKILL)
            os._exit(1)
        time.sleep(1)
        wait_time += 1


def stop():
    if zk:
        zk.stop()
        zk.close()


def is_master():
    if not os.path.exists('/opt/cluster/enabled'):
        return os.path.exists('/opt/cluster/master')


def get(force_reconnect=False):
    if not zk or force_reconnect:
        start(force_reconnect=force_reconnect)
    return zk


class NotConnected(Exception):
    pass


class AlreadyExists(Exception):
    pass