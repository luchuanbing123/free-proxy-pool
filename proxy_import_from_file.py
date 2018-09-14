from basehelper import try_add_proxies

txt_arr = [
    'gatherproxy',
    'clarketm_proxy',
]


def clarketm_proxy():
    url = 'https://github.com/clarketm/proxy-list/blob/master/proxy-list.txt'


def gatherproxy():
    for readline in open('[gatherproxy.com]proxies_2018_09_14.txt', 'r').readlines():
        ip = readline.split(':')[0]
    port = readline.split(':')[1].strip()

    protocol = 'http'
    try_add_proxies({'ip': ip,
                     'port': port,
                     'protocol': protocol
                     })
    protocol = 'https'
    try_add_proxies({'ip': ip,
                     'port': port,
                     'protocol': protocol
                     })
