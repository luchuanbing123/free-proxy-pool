# free-proxy-pool


#### Description
Collect free http/https/socket proxy from internet 

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

#### Installation

1. pip install -r requirements.txt
2. install mongodb

