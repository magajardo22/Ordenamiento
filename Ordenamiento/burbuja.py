from lista import Lista
from all_sort import burbuja
import random
import time

tiempos = Lista()

for i in range(1, 6):
    total_tiempo_burbuja = 0

    for j in range(10):
        lista = Lista()

        for j in range(250 * i):
            lista.insertar(random.randint(0, 100000))

        print("Lista generada")

        inicio_burbuja = time.time()
        burbuja(lista)
        fin_burbuja = time.time()

        tiempo_burbuja = fin_burbuja - inicio_burbuja
        print(tiempo_burbuja)
        total_tiempo_burbuja += tiempo_burbuja

    promedio_burbuja = total_tiempo_burbuja / 10

    tiempos.insertar(promedio_burbuja)
    print("Promedio:", promedio_burbuja)

tiempos.imprimir()