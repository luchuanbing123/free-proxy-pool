import webapi
import freeproxyspider
import proxycheckusability
import threading

threading.Thread(target=webapi.execute).start()
threading.Thread(target=freeproxyspider.execute).start()
threading.Thread(target=proxycheckusability.execute).start()

