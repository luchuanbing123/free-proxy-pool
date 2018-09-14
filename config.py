import configparser

_conf = configparser.ConfigParser()
_conf.read('config.ini')

mongodb_host = _conf.get('mongodb', 'host')
mongodb_port = _conf.getint('mongodb', 'port')

webapi_host = _conf.get('webapi', 'host')
webapi_port = _conf.getint('webapi', 'port')

func_webapi = _conf.getboolean('func', 'webapi')
func_freeproxyspider = _conf.getboolean('func', 'freeproxyspider')
func_proxycheckusability = _conf.getboolean('func', 'proxycheckusability')

freeproxyspider_supportselenium = _conf.getboolean('freeproxyspider', 'supportselenium')

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
           }
