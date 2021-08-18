import abc

class Resolver(metaclass = abc.ABCMeta):
    
    def supports(self, contenttype):
        return contenttype == self.getSupportedContentType()
    
    @abc.abstractmethod
    def getSupportedContentType(self):
        return

    @abc.abstractmethod
    def resolve(self, msg):
        pass
