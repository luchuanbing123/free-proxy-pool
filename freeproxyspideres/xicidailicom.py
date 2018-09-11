from freeproxyspideres import freeproxyspiderhelper

get_soup = freeproxyspiderhelper.get_soup
try_add_proxies = freeproxyspiderhelper.try_add_proxies


def execute():
    soup = get_soup('http://www.xicidaili.com/')
    for tr in soup.select('#ip_list  tr'):
        tds = tr.select('td');
        if len(tds) == 8 and (tds[5].text == 'HTTP' or tds[5].text == 'HTTPS'):
            ip = tds[1].text
            port = tds[2].text
            protocol = tds[5].text.strip().lower()
            proxy_addr = protocol + '://' + ip + ':' + port
            try_add_proxies({'ip': ip, 'port': port, 'protocol': protocol, 'proxy_addr': proxy_addr, 'usability': 0})
