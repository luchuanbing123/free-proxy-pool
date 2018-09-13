# 免费代理池 [free-proxy-pool](https://github.com/LuChuanBing/free-proxy-pool/blob/master/README.en.md)

##  说明
    从互联网上收集免费的http / https / socket代理
    测试地址:
    
#### 配置选项 config.ini
    [mongodb]
    host = localhost #mongodb 的host或者ip
    port = 27017 #mongodb的端口    
    
    [webapi]
    host = 0.0.0.0 # 网站的host或者ip    
    port = 80 # 网站的端口
    
    [func]
    freeproxyspider = True # 开启从网络上爬取免费http代理的进程
    proxycheckusability = True # 开启代理有效性检查的进程
    webapi = True # 启动webapi
    
#### 安装    
    1. pip install -r requirements.txt
    2.安装mongodb
    
#### 运行
    py main.py
### MongoDB
#### backup（在项目的根目录中运行）  
    mongodump -h 127.0.0.1 -d proxies -o mongodb
#### restore（在项目的根目录中运行）
    mongorestore -h 127.0.0.1 -d mongodb / proxies
#### mongoexport
    mongoexport -h 127.0.0.1 -d proxies -c proxies -o proxies.json
#### mongoimport
    mongoimport --db proxies --collection proxies --file proxies.json
#### freeze
    pip freeze> requirements.txt
