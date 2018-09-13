import basehelper

get_soup = basehelper.get_soup
try_add_proxies = basehelper.try_add_proxies


def execute():
    for page in range(1, 7):
        soup = get_soup('https://list.proxylistplus.com/SSL-List-' + str(page), timeout=60)
        for tr in soup.select('tr.cells')[1:-1]:
            tds = tr.select('td')
            ip = tds[1].text
            port = tds[2].text
            protocol = 'https' if tds[6].text == 'yes' else 'http'
            country = tds[4].text
            proxy_addr = protocol + '://' + ip + ':' + port
            try_add_proxies({'ip': ip,
                             'port': port,
                             'protocol': protocol,
                             'proxy_addr': proxy_addr,
                             'country': country
                             })
