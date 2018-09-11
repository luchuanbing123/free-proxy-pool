import db
import requests
import time


def execute():
    while True:
        time.sleep(2)
        for proxy in db.proxies.find():
            try:
                if 'succeed' not in proxy:
                    proxy['succeed'] = 0
                if 'failed' not in proxy:
                    proxy['failed'] = 0

                requests.get(proxy['protocol'] + "://www.baidu.com",
                             proxies={proxy['protocol']: proxy['proxy_addr']},
                             timeout=5)
            except Exception as msg:
                db.proxies.update_one({'_id': proxy['_id']},
                                      {'$set': {'usability': proxy['usability'] - 1,
                                                'succeed': proxy['failed'] + 1}})
            else:
                db.proxies.update_one({'_id': proxy['_id']},
                                      {'$set': {'usability': proxy['usability'] + 1,
                                                'succeed': proxy['succeed'] + 1}})


execute()
