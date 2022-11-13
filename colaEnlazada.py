class Celda:
    __sig = None
    __item = None

    def __init__(self, item = None):
        self.__sig = None
        self.__item = item

    def setItem(self, item):
        self.__item = item
    
    def setSig(self, celda):
        self.__sig = celda

    def getItem(self):
        return self.__item
    
    def getSig(self):
        return self.__sig

class ColaE:
    __cant = None
    __ul = None
    __pr = None

    def __init__(self, cant=0):
        self.__cant = cant
        self.__pr = NULL
        self.__ul = NULL
    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, x):
        ps1 = Celda()
        ps1.setItem(x)
        ps1.setSig(NULL)
        if(self.__ul == NULL):
            self.__pr = ps1
        else:
            self.__ul.setSig(ps1)
        self.__ul = ps1
        self.__cant += 1
        return self.__ul.getItem()

    def suprimir(self):
        if (self.vacio()):
            print("\nLa cola esta vacia")
            return 0
        else:
            aux = self.__pr
            x = self.__pr.getItem()
            self.__pr = self.__pr.getSig()
            self.__cant -= 1
            if self.__pr == NULL:
                self.__ul = NULL
            del aux
            return x

    def recuperar(self):
        return self.__pr
    
    def mostrar(self):
        aux = self.__pr
        while (aux!=NULL):
            print(aux.getItem())
            aux = aux.getSig()