import basehelper

get_soup = basehelper.get_soup
try_add_proxies = basehelper.try_add_proxies


def execute():
    soup = get_soup('https://list.proxylistplus.com/SSL-List-1',timeout=600)
    for tr in soup.select('tr.cells')[:-1]:
        tds = tr.select('td')
        ip = tds[1].text
        port = tds[2].text
        protocol = tds[3].text.lower()
        country = tds[4].text
        proxy_addr = protocol + '://' + ip + ':' + port
        try_add_proxies({'ip': ip,
                         'port': port,
                         'protocol': protocol,
                         'proxy_addr': proxy_addr,
                         'country':country
                         })
