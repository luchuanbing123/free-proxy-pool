import freeproxyspideres
from freeproxyspideres import *
import time


def execute():
    while True:
        for free_proxy_spider in freeproxyspideres.__all__:
            try:
                spider = eval(free_proxy_spider)
                spider.execute()
            except Exception as msg:
                print(msg)
        time.sleep(60)


