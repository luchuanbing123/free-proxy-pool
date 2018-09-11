import WebApi
import FreeProxySpider
import threading

threading.Thread(target=WebApi.Start).start()
threading.Thread(target=FreeProxySpider.Start).start()

