import basehelper

get_soup = basehelper.get_soup
try_add_proxies = basehelper.try_add_proxies


def execute():
    soup = get_soup('https://www.sslproxies.org/', timeout=30)
    for tr in soup.select('#proxylisttable tr')[1:-1]:
        tds = tr.select('td')
        ip = tds[0].text
        port = tds[1].text
        country = tds[3].text
        protocol = 'https' if tds[6].text == 'yes' else 'http'
        try_add_proxies({'ip': ip,
                         'port': port,
                         'protocol': protocol,
                         'country': country
                         })
