
'''
    Attributes:
        next: pointer to the next handler

'''
class ChainedHandler:

    def __init__(self):
        self.next = None

    def handle(self, msg):
        
        msg = self.doHandle(msg)

        if (self.next != None):
            self.next.handle(msg)

    def doHandle(self,msg):
        return None

    def getNext(self):
        return self.next

    def setNext(self, handler):
        if (not isinstance(handler, ChainedHandler)):
            return 
        self.next = handler

    '''
        Chained builder pattern
    '''
    class HandlerBuilder:

        def __init__(self):
            self.rootHandler = None
            self.tailHandler = None

        def addHandler(self, handler):
            if (not isinstance(handler, ChainedHandler)):
                return self
            
            if (self.rootHandler == None):
                self.rootHandler = handler
                self.tailHandler = handler
                return self
            
            self.tailHandler.setNext(handler)
            self.tailHandler = handler
            return self

        def build(self):
            return self.rootHandler