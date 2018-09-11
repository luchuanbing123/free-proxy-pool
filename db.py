import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

_client: MongoClient = pymongo.MongoClient(host='localhost', port=27017)
_db_proxies: Database = _client.get_database('proxies')

proxies: Collection = _db_proxies['proxies']
tokens: Collection = _db_proxies['proxies']
