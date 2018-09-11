import requests
from bs4 import BeautifulSoup
import db as db
from urllib.parse import urlparse

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
           }


def get_soup(url):
    print('spider:' + url)
    headers['Host'] = urlparse(url).hostname
    html = requests.get(url, headers=headers).text
    return BeautifulSoup(html, 'html.parser')


def try_add_proxies(proxy):
    proxy['usability'] = 0
    proxy['proxy_addr'] = proxy['protocol'] + '://' + proxy['ip'] + ':' + proxy['port']
    if db.proxies.find_one({'proxy_addr': proxy['proxy_addr']}) is None:
        print('add proxy:' + proxy['proxy_addr'])
        db.proxies.insert_one(proxy)
