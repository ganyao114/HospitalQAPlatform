from pymongo import MongoClient

client = MongoClient('192.168.149.129', 12345)
dbname = 'test'
db = client[dbname]
for u in db.test.find({"name":2}):
    print u