import json
from resolver.Resolver import *

class JsonResolver(Resolver):

    def getSupportedContentType(self):
        return "application/json"

    def resolve(self, msg):
        return json.loads(str(msg,'utf-8'))