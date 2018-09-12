# from freeproxyspideres import  sslproxiesorg
#
# sslproxiesorg.execute()
import requests

print(requests.get('http://www.baidu.com', proxies={'http': "http://202.100.83.139:80"}).text)
