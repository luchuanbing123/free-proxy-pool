import basehelper
import re

get_soup = basehelper.get_soup
try_add_proxies = basehelper.try_add_proxies
_ip_reg = '^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|[1-9]).(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|[1-9]).(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|[1-9]).(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|[1-9])$'


def execute():
    soup = get_soup('https://www.proxynova.com/proxy-server-list/', timeout=30)
    for tr in soup.select('tr[data-proxy-id]'):
        tds = tr.select('td')
        ip = tds[0].text.split()[0][24:-11] + tds[0].text.split()[2].strip()[1:-3]
        port = tds[1].text.strip()
        country = tds[5].text.strip().replace('\t', '').replace('\r', '').replace('\n', '').replace(' ', '')
        protocol = 'http'
        try_add_proxies({'ip': ip,
                         'port': port,
                         'protocol': protocol,
                         'country': country
                         })
