from freeproxyspideres import freeproxyspiderhelper

get_soup = freeproxyspiderhelper.get_soup
try_add_proxies = freeproxyspiderhelper.try_add_proxies


def execute():
    soup = get_soup('https://free-proxy-list.net/')
    for tr in soup.select('#proxylisttable tr')[1:]:
        ip = tr.select('td')[0].text
        port = tr.select('td')[1].text
        protocol = 'http' if tr.select('td')[6].text.strip() == 'no' else 'https'
        proxy_addr = protocol + '://' + ip + ':' + port
        try_add_proxies(
            {'ip': ip, 'port': port, 'protocol': protocol, 'proxy_addr': proxy_addr, 'usability': 0})
