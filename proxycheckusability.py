import db
import telnetlib
import time


def execute():
    while True:
        for proxy in db.proxies.find():
            try:
                telnetlib.Telnet().open(proxy['ip'], proxy['port'], timeout=2)
            except Exception as e:
                db.proxies.update_one({'_id': proxy['_id']},
                                      {'$set': {'usability': proxy['usability'] - 1,
                                                'failed': proxy['failed'] + 1}})
            else:
                db.proxies.update_one({'_id': proxy['_id']},
                                      {'$set': {'usability': proxy['usability'] + 1,
                                                'succeed': proxy['succeed'] + 1}})
        time.sleep(60 * 30)
