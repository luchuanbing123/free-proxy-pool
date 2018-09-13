import db as db
import queue

global _proxies_queues
_proxies_queues = {}


def _fetch_proxies(protocol='http', token_level=0):
    global _proxies_queues
    protocol_key = protocol + '_' + str(token_level)
    if protocol_key not in _proxies_queues:
        _proxies_queues[protocol_key] = queue.Queue()

    _queue = _proxies_queues[protocol_key]
    if _queue.empty():
        all_proxies = db.proxies.find({'protocol': protocol}).sort([('usability', -1)]).limit(
            int(token_level) * 1000 + 50)
        for proxy in all_proxies:
            _queue.put(proxy)

    return _queue


def next(protocol, token=None):
    token_level = 0
    if token:
        token_in_db = db.tokens.find_one({'token': token})
        if token_in_db:
            token_level = token_in_db['level']

    return _fetch_proxies(protocol, token_level).get_nowait()


global _proxy_count
_proxy_count = 0


def get_proxy_count():
    global _proxy_count
    return _proxy_count


def update_proxy():
    global _proxies_queues
    global _proxy_count
    _proxy_count = db.proxies.count_documents({})
    _proxies_queues = {}
