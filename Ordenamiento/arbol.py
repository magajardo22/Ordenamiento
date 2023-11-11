from nodo_arbol import nodoArbol
from lista import Lista
import time
import random

tiempos = Lista()

for i in range(1, 6):
    total_tiempo_arbol = 0

    lista = Lista()
    for j in range(10):

        for j in range(250 * i):
            lista.insertar(random.randint(0, 100000))

        print("Lista generada")

        ini_arbol = time.time()
        arbol = nodoArbol(lista.index(0))
        for j in range(1, lista.get_tamanio()):
             arbol.insertarNodo(lista.index(j))
        fin_arbol = time.time()

        tiempo_arbol = fin_arbol - ini_arbol
        print(tiempo_arbol)
        total_tiempo_arbol += tiempo_arbol

    promedio_arbol = total_tiempo_arbol / 10

    tiempos.insertar(promedio_arbol)
    print("Promedio:", promedio_arbol)

tiempos.imprimir()

