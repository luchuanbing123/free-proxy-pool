import sys

hosts = {'www.sslproxies.org': '104.31.74.162',
         'free-proxy-list.net': '104.27.184.96',
         'hidemyna.me': '104.25.45.99',
         'list.proxylistplus.com': '104.28.27.84',
         'www.proxynova.com':'69.164.218.141',
         'www.gatherproxy.com':'97.74.233.74', # http://www.gatherproxy.com/proxylist/country/?c=Singapore
         }

_char_newline = '\r\n'
if sys.platform.startswith('win'):
    _hosts_path = 'C:\Windows\System32\drivers\etc\hosts'
    _char_newline = '\r\n'

if sys.platform.startswith('linux'):
    _hosts_path = '/etc/hosts'
    _char_newline = '\n'

f = open(_hosts_path, 'a')
f.write(_char_newline + '# add by https://github.com/LuChuanBing/free-proxy-pool' + _char_newline)
for host in hosts:
    f.write(('{} {}' + _char_newline).format(hosts[host], host))
