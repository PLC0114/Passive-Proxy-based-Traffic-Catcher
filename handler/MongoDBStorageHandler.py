from pymongo import MongoClient 
from config.Config import *
from handler.ChainedHandler import *


'''
    Attributes:
        client: mongoDB client
        database: target database
        collection: target collection
        
'''

class MongoDBStorageHandler(ChainedHandler):

    def __init__(self, collectionName = mongoDBDefaultCollection):
        # built in connection pool 
        # self.client = MongoClient(host = mongoDBHost, port = mongoDBPort, username = mongoDBUsername, password = mongoDBPassword)
        # for testing purpose, no authentication 
        self.client = MongoClient(host = mongoDBHost, port = mongoDBPort)
        self.database = self.client[mongoDBName]
        self.collection = self.database[collectionName]
        
        super(MongoDBStorageHandler, self).__init__()
    
    def doHandle(self, msg):
        if (type(msg) != dict and msg != {}):
            return msg
        
        self.collection.insert_one(msg)
        return msg