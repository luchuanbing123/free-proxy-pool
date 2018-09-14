from basehelper import  try_add_proxies

for readline in open('[gatherproxy.com]proxies_2018_09_14.txt','r').readlines():
    ip=readline.split(':')[0]
    port = readline.split(':')[1].strip()

    protocol='http'
    try_add_proxies({'ip': ip,
                     'port': port,
                     'protocol': protocol
                     })
    protocol = 'https'
    try_add_proxies({'ip': ip,
                     'port': port,
                     'protocol': protocol
                     })
