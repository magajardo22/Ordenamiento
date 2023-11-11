from lista import Lista
from all_sort import ordenamientoRapido
import random
import time

tiempos = Lista()

for i in range(1, 2):
    total_tiempo_quick = 0

    for j in range(10):
        lista = Lista()

        for j in range(750):
            lista.insertar(random.randint(0, 100000))

        print("Lista generada")

        ini_quick = time.time()
        ordenamientoRapido(lista, 0, lista.get_tamanio() - 1)
        fin_quick = time.time()

        tiempo_quick = fin_quick - ini_quick
        print(tiempo_quick)
        total_tiempo_quick += tiempo_quick

    promedio_quick = total_tiempo_quick / 10

    tiempos.insertar(promedio_quick)
    print("Promedio:", promedio_quick)

tiempos.imprimir()
