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
