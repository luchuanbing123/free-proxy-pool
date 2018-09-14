from basehelper import try_add_proxies
import config

headers = config.headers


def execute():
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import time
    import re

    if config.freeproxyspider_supportselenium:
        ip_reg = '^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|[1-9]).(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|[1-9]).(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|[1-9]).(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|[1-9])$'
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--window-position=10000,10000 ")
        browser = webdriver.Chrome(chrome_options=chromeOptions)
        headers['Host'] = 'spys.one'
        for page in range(3):
            url = 'http://spys.one/en/https-ssl-proxy/{}/'.format(str(page))
            print('spider:' + url)
            browser.get(url)
            html = browser.page_source
            soup = BeautifulSoup(html, 'html.parser')
            for tr in soup.select('.spy1x,.spy1xx')[1:]:
                try:
                    tds = tr.select('td')
                    ip = re.search('\d+\.\d+\.\d+\.\d+', tds[0].text).group()
                    port = re.search(':\d+', tds[0].text).group().replace(':', '')
                    protocol = 'https' if 'https' in tds[1].text.strip().lower() else 'http'
                    proxy_addr = protocol + '://' + ip + ':' + port
                    try_add_proxies({'ip': ip, 'port': port, 'protocol': protocol, 'proxy_addr': proxy_addr, 'usability': 0})
                except:
                    continue
            time.sleep(10)
        browser.close()
    else:
        print('selenium not supported')
