from handler.ChainedHandler import ChainedHandler


from config.Config import *

class DomainFilterHandler(ChainedHandler):
    def __init__(self):
        self.targetDomains = filteredDomains
        super(DomainFilterHandler, self).__init__()

    def doHandle(self, msg):
        if msg.request.host in filteredDomains:
            return msg
        return None