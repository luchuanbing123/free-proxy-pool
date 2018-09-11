import FreeProxySpideres
from FreeProxySpideres import *
import time


def Start():
    while True:
        for free_proxy_spider in FreeProxySpideres.__all__:
            try:
                spider = eval(free_proxy_spider)
                spider.execute()
            except Exception as msg:
                print(msg)
        time.sleep(60 * 5)


