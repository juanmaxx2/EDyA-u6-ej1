from grafo import Grafo

if __name__ == "__main__":
    unGrafo = Grafo(5)
    unGrafo.Agregar(2,4)
    unGrafo.Agregar(1,4)
    unGrafo.Agregar(3,5)
    unGrafo.Agregar(3,2)
    unGrafo.Adyacente(3)