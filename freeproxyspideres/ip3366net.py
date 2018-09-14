from basehelper import try_add_proxies
import config

headers = config.headers


def execute():
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import time

    if config.freeproxyspider_supportselenium:
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--window-position=10000,10000 ")
        browser = webdriver.Chrome(chrome_options=chromeOptions)
        headers['Host'] = 'www.ip3366.net'
        for page in range(10):
            url = 'http://www.ip3366.net/?stype=1&page=' + str(page + 1)
            print('spider:' + url)
            browser.get(url)
            html = browser.page_source
            soup = BeautifulSoup(html, 'html.parser')
            for tr in soup.select('#list > table > tbody > tr'):
                tds = tr.select('td')
                ip = tds[0].text.strip()
                port = tds[1].text.strip()
                protocol = tds[3].text.strip().lower()
                proxy_addr = protocol + '://' + ip + ':' + port
                try_add_proxies({'ip': ip, 'port': port, 'protocol': protocol, 'proxy_addr': proxy_addr, 'usability': 0})
            time.sleep(10)
        browser.close()
    else:
        print('selenium not supported')
