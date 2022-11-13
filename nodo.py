class Nodo:
    __sig = None
    __item = None

    def __init__ (self):
        self.__item = None
        self.__sig = None

    def setItem(self, item):
        self.__item = item
    
    def setSig(self, sig):
        self.__sig = sig
    
    def getItem(self):
        return self.__item
    
    def getSig(self):
        return self.__sig