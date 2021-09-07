from handler.DoaminFilterHandler import *
from handler.MongoDBFormatHandler import *
from handler.MongoDBStorageHandler import *

'''
    Attributes:
        handler: root handler of the target handler chain

'''
class Processor:
    def __init__(self, handler):
        self.handler = handler

    def response(self,flow):
        self.handler.handle(flow)

requestHandler = ChainedHandler.HandlerBuilder().addHandler(DomainFilterHandler()).addHandler(MongoDBFormatHandler()).addHandler(MongoDBStorageHandler("request")).build()

addons = [
    Processor(requestHandler)
]