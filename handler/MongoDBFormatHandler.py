from pymongo import MongoClient 
from config.Config import *
from handler.ChainedHandler import *
from util.util import *
from resolver.JsonResolver import *
from resolver.WebFormResolver import *
'''
    Attributes:
        requestContentResolvers: resolver chain for request body resolving based on content type
        responseContentResolvers: resolver chain for response body resolving based on content type
'''

class MongoDBFormatHandler(ChainedHandler):
    
    def __init__(self):
        self.configure()
        super(MongoDBFormatHandler, self).__init__()

    def configure(self):
        # outer responsibility chain is used, because the content types are fixed
        # request resolvers
        self.requestContentResolvers=[]
        self.requestContentResolvers.append(JsonResolver())
        self.requestContentResolvers.append(WebFormResolver())

        # response resolvers
        self.responseContentResolvers=[]
        self.responseContentResolvers.append(JsonResolver())

    def doHandle(self, msg):
        if (msg.request == None or msg.response == None):
            return {}

        res={}
        self.formatFromRequest(msg.request, res)

        # handle response
        self.formatFromResponse(msg.response, res)

        return res

    
    def formatFromRequest(self, request, res):
        res['timestamp_start'] = request.timestamp_start

        res['host'] = request.host
        res['port'] = request.port
        res['method'] = request.method

        requestPath = request.path.split('?')

        res['path'] = requestPath[0]

        if len(requestPath) > 1:
            res['urlParam'] =  formatUrlParam(requestPath[1])

        if len(request.content) > 0:
        # tbd: content
            res['content-type'] = request.headers["Content-Type"]
            res['content'] = self.resolve(self.requestContentResolvers, request.content, res['content-type'])


    def formatFromResponse(self, response, res):
        res['response'] = {}
        res['response']['timestamp_start'] = response.timestamp_start

        res['response']['status_code'] = response.status_code

        res['response']

        if (len(response.content) > 0):
            res['response']['content-type'] = response.headers["Content-Type"]
            res['response']['content'] = self.resolve(self.responseContentResolvers, response.content, res['response']['content-type'])

    def resolve(self, resolvers, rawcontent, contenttype):
        for resolver in resolvers:
            if (resolver.supports(contenttype)):
                return resolver.resolve(rawcontent)

        return rawcontent

    