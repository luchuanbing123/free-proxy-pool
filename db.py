import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
import config

_client: MongoClient = pymongo.MongoClient(host=config.mongodb_host, port=config.mongodb_port)
_db_proxies: Database = _client.get_database('proxies')

proxies: Collection = _db_proxies['proxies']
tokens: Collection = _db_proxies['proxies']
