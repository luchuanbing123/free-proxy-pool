import threading
import config

if config.func_freeproxyspider:
    import freeproxyspider

    threading.Thread(target=freeproxyspider.execute).start()

if config.func_proxycheckusability:
    import proxycheckusability

    threading.Thread(target=proxycheckusability.execute).start()

if config.func_webapi:
    import webapi

    threading.Thread(target=webapi.execute).start()
