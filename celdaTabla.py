from numpy import integer


class CeldaTabla:
    __conocido = None
    __distancia = None
    __camino = None
    
    def __init__(self):
        self.__conocido = False
        self.__distancia = 999999999
        self.__camino = None
    
    def setConocido(self,value):
        self.__conocido = value
    
    def setDistancia(self,value):
        self.__distancia = value

    def setCamino(self,value):
        self.__camino = value

    def getConocido(self):
        return self.__conocido
    
    def getDistancia(self):
        return self.__distancia
    
    def getCamino(self):
        return self.__camino
    
    def __str__(self) -> str:
        return str(self.__conocido) + " " + str(self.__distancia) + " " + str(self.__camino)
    
