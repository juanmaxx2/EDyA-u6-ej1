import numpy as np
from colaEnlazada import ColaE
from CeldaTabla import CeldaTabla

class GrafoSecuencial:
    __tam = None

    def __init__ (self, tam):
        self.__tam = tam
        self.__matriz = np.zeros((tam,tam), dtype = int)
    
    def Agregar(self, nodo1, nodo2):
        nodo1 -= 1
        nodo2 -= 1
        if (0 <= nodo1 < self.__tam) and (0 <= nodo2 < self.__tam):
            self.__matriz [nodo1][nodo2] = 1
            self.__matriz [nodo2][nodo1] = 1
        else:
            print("\nEl nodo ingresado no es correcto")
        
    def Adyacente (self, nodo):
        nodo -= 1 
        if (0 <= nodo < self.__tam):
            for i in range(self.__tam):
                if self.__matriz [nodo][i] == 1:
                    print (i+1)
    
    def Conexo(self):
        band = True
        i = 0
        while i < self.__tam and band:
            if len(self.Adyacente(i)) == 0:
                band = False
            i+=1
        if band == False:
            print("Es disconexo")
        else:
            print("Es conexo")

    def REP_visita (self,actual,arreglo,recorrido):
        recorrido.append(actual)
        arreglo[actual] = 1
        Adyacentes = self.Adyacente(actual)
        for adyacente in adyacentes:
            if arreglo[adyacente] == 0:
               recorrido =  self.REP_visita(adyacente ,arreglo = arreglo,recorrido = recorrido)
        return recorrido
    
    def REP (self, nodo, actual, arreglo = None, recorrido = None):
        if actual >=0  and actual < self.__tam:
            arreglo = np.zeros(self.__tam,dtype = int)
            recorrido = []
            recorrido = self.REP_visita(actual = actual , arreglo = arreglo,recorrido = recorrido)
            return recorrido
        else:
            print('ERROR: vertice  origen no valido')
            return None

    def REA (self, nodo):
        arreglo = -1 * np.ones(self.__tam,dtype=int)
        cola = ColaE()
        cola.insertar(origen)
        arreglo[origen] = 0
        v = 0
        while not cola.vacia():
            cola.suprimir()
            for i in self.Adyacente(v):
                    if arreglo[i] == -1:
                        arreglo[i] = arreglo[v] + 1
                        cola.insertar(i)
    
    def getCamino (self,inicio,fin):
        d = np.zeros(self.__tam, dtype = int)
        resultado = self.REP_visita(inicio, fin, d)
        if isinstance(resultado,list):
            resultado.insert(0,inicio)
        return resultado
    
    def getV (self,Tabla):
        v = 0
        mindist = 99999999
        for i in range(len(Tabla)):
            if Tabla[i].getConocido() == False and Tabla[i].getDistancia() < mindist:
                v = i
                mindist = Tabla[i].getDistancia()
        return v

    def Dijkstra (self,origen,destino):
        Tabla = np.empty(self.__tam,dtype=CeldaTabla)
        for i in range(self.__tam):
            Tabla[i] = CeldaTabla()
        Tabla[origen].setDistancia(0)
        v = origen
        for i in range(self.__tam):
            v = self.getV(Tabla)
            Tabla[v].setConocido(True)
            for w in self.Adyacentes(v):
                    if Tabla[w].getConocido() == False:
                        if (Tabla[v].getDistancia() + self.__matriz[v,w]) < Tabla[w].getDistancia():
                            Tabla[w].setDistancia(Tabla[v].getDistancia() + self.__matriz[v,w])
                            Tabla[w].setCamino(v)
        v = destino
        camino = [v]
        while Tabla[v].getCamino() != None:
            v = Tabla[v].getCamino()
            camino.insert(0,v)
        print(camino)
    
    def Prim (self,origen):
        Tabla = np.empty(self.__tam,dtype=CeldaTabla)
        for i in range(self.__tam):
            Tabla[i] = CeldaTabla()
        Tabla[origen].setDistancia(0)
        v = origen
        for i in range(self.__tam):
            v = self.getV(Tabla)
            Tabla[v].setConocido(True)
            for w in self.Adyacentes(v):
                if self.__matriz[v,w] == 1:
                    if Tabla[w].getConocido() == False:
                        if self.__matriz[v,w] < Tabla[w].getDistancia():
                            Tabla[w].setDistancia(self.__matriz[v,w])
                            Tabla[w].setCamino(v)
        for i in range(len(Tabla)):
            print(str(i) + ": " + str(Tabla[i]))