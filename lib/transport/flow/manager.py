from container import get_container
import app_context
import msgpack
import zmq
import json
import logbook

context = zmq.Context(2)

container = get_container(app_context)
zookeeper = container.get_object('zookeeper')
data = zookeeper.get('/comm_config')
log = logbook.Logger('log_generator_socket_manager')
send_socket_cache = {}
send_msg_count = {}


def clear_socket_config_cache(data, stat, event=None):
    global comm_conf, send_socket_cache
    log.debug('clear socket cache')
    try:
        data = zookeeper.get('/comm_config')
        comm_conf = json.loads(data[0])
        for cache_key in send_socket_cache:
            socket_name, uri = cache_key.split('@')
            if uri not in comm_conf.get(socket_name, []):
                try:
                    s = send_socket_cache[cache_key][1]
                    s.close(5)
                except TypeError:
                    pass
                except Exception, e:
                    log.exception(e)
                send_socket_cache[cache_key] = None
    except:
        pass


zookeeper.DataWatch('/comm_config', clear_socket_config_cache)


def send(instance, socket_name, msg):
    fail_count = 0
    msg = msgpack.packb(msg)

    def do_send(msg):
        socket_info = ''
        try:
            dealer, socket_info = get_distributed_socket(instance, socket_name, extra_info=True)
            if not dealer:
                return False, socket_info, 'no dealer'
            dealer.send(msg, zmq.NOBLOCK)
            return True, socket_info, ''
        except Exception, e:
            return False, socket_info, str(e)

    dropped = True
    while fail_count < 3:
        resp = do_send(msg)
        if resp[2] == 'no dealer':
            dropped = True
            break
        if resp[0]:
            dropped = False
            break
        else:
            fail_count += 1
            log.warn('%s.unavail' % socket_name)
    if dropped:
        log.warn('%s.drop' % socket_name)


def get_distributed_socket_uris(socket_name):
    return comm_conf.get(socket_name, [])


def get_distributed_socket(instance, socket_name, extra_info=False):
    global send_msg_count

    if not send_msg_count.get(socket_name):
        send_msg_count[socket_name] = 0
    send_msg_count[socket_name] += 1

    uris = get_distributed_socket_uris(socket_name)
    if not uris:
        return
    uri = uris[send_msg_count.get(socket_name, 0) % len(uris)]
    cache_key = '%s@%s' % (socket_name, uri)
    if send_socket_cache.get(cache_key):
        if not extra_info:
            return send_socket_cache.get(cache_key)[1]
        else:
            return send_socket_cache.get(cache_key)[1], uri
            # context = zmq.Context()
    send_socket_cache[cache_key] = context, context.socket(zmq.PUSH)
    send_socket_cache[cache_key][1].connect(str(uri))
    log.warn('connect to %s@%s' % (socket_name, uri))
    if not extra_info:
        return send_socket_cache.get(cache_key)[1]
    else:
        return send_socket_cache.get(cache_key)[1], uri
