# [免费代理池](https://github.com/LuChuanBing/free-proxy-pool/blob/master/README.md) free-proxy-pool

## Description
Collect free http/https/socket proxy from internet 

## test addr:
- The data is updated daily, no tokens are 100 limit per day, and there are 1100 limit per day with tokens.
- [http://47.100.12.55:8118](http://47.100.12.55:8118)  

- [http://47.100.12.55:8118/get](http://47.100.12.55:8118/get)  
Parameter Description:
    - protocol Optional parameter http/https E.g: http://47.100.12.55:8118/get?protocol=https
    - token Optional parameter E.g: http://47.100.12.55:8118/get?protocol=http&token=o47Fa0mp9SRTf3eiKmqWm69BjG_8    
    how to get token :Pay attention to WeChat public number <b>高效工具库(gaoxiaogongjuku)</b>
    <img alt='微信公众号:gaoxiaogongjuku'  src='https://github.com/LuChuanBing/free-proxy-pool/blob/master/qrcode.jpg' />
    
#### set config.ini
    [mongodb]
    host = localhost # host or ip of mongodb
    port = 27017 # port or ip of mongodb    
    
    [webapi]
    host = 0.0.0.0 # host or ip of webapi site   
    port = 80 # port or ip of webapi site
    
    [func]
    freeproxyspider = True # start the process of crawling free http proxy from the network
    proxycheckusability = True # start the process of proxy validity check
    webapi = True # start webapi

#### Installation

1. pip install -r requirements.txt
2. install mongodb

#### run
    py main.py
    
###  MongoDB
#### backup(run in the root directory of the project)
    mongodump -h 127.0.0.1 -d proxies -o mongodb
#### restore(run in the root directory of the project)
    mongorestore -h 127.0.0.1 -d mongodb/proxies
#### mongoexport
    mongoexport -h 127.0.0.1 -d proxies -c proxies -o proxies.json
#### mongoimport
     mongoimport --db proxies --collection proxies --file proxies.json
#### freeze
pip freeze > requirements.txt



