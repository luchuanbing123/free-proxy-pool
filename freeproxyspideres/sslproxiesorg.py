import basehelper

get_soup = basehelper.get_soup
try_add_proxies = basehelper.try_add_proxies


def execute():
    soup = get_soup('https://www.sslproxies.org/')
    for tr in soup.select('#proxylisttable tr'):
        tds = tr.select('td')
        ip = ''
        port = ''
        for t in tds[0].select('*'):
            if 'style' in t.attrs and 'none;' in t.attrs['style']:
                continue
            if 'class' in t.attrs and 'port' in t.attrs['class']:
                port = t.text.strip()
            else:
                ip += t.text.strip()
        protocol = tds[2].text.strip()
        try_add_proxies({'ip': ip, 'port': port, 'protocol': protocol})
