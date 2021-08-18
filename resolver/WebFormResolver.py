from resolver.Resolver import *
from util.util import *

class WebFormResolver(Resolver):
    
    def getSupportedContentType(self):
        return "application/x-www-form-urlencoded"
    
    def resolve(self, msg):
        return formatUrlParam(str(msg,'utf-8'))
