import requests
from bs4 import BeautifulSoup
import db as db
from urllib.parse import urlparse
import chardet

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
           }


def get_soup(url, proxies=None, timeout=10):
    print('spider:' + url)
    headers['Host'] = urlparse(url).hostname
    req = requests.get(url, headers=headers, timeout=timeout, proxies=proxies)
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings and len(encodings) > 0:
            encoding = encodings[0]
        elif req.apparent_encoding is not None:
            encoding = req.apparent_encoding
        else:
            encoding = 'ISO-8859-1'
        html = req.content.decode(encoding, 'replace')  # replace -> replace illegal character with ?
    else:
        html = req.text
    return BeautifulSoup(html, 'html.parser')


def try_add_proxies(proxy):
    proxy['usability'] = 0
    proxy['succeed'] = 0
    proxy['failed'] = 0
    if 'country' not in proxy:
        proxy['country'] = ''
    proxy['proxy_addr'] = proxy['protocol'] + '://' + proxy['ip'] + ':' + proxy['port']
    if db.proxies.find_one({'proxy_addr': proxy['proxy_addr']}) is None:
        print('add proxy:' + proxy['proxy_addr'])
        db.proxies.insert_one(proxy)
