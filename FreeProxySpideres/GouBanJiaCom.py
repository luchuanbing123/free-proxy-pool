from FreeProxySpideres import FreeProxySpiderHelper

get_soup = FreeProxySpiderHelper.get_soup
try_add_proxies = FreeProxySpiderHelper.try_add_proxies


def execute():
    soup = get_soup('http://www.goubanjia.com/')
    for tr in soup.select('#services > div > div.row > div > div > div > table > tbody > tr'):
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
