from lista import Lista
from all_sort import burbujaMejorada
import random
import time

tiempos = Lista()

for i in range(1, 6):
    total_tiempo_burbujam = 0

    for j in range(10):
        lista = Lista()

        for j in range(250 * i):
            lista.insertar(random.randint(0, 100000))

        print("Lista generada")

        inicio_burbujam = time.time()
        burbujaMejorada(lista)
        fin_burbujam = time.time()

        tiempo_burbujam = fin_burbujam - inicio_burbujam
        print(tiempo_burbujam)
        total_tiempo_burbujam += tiempo_burbujam

    promedio_burbujam = total_tiempo_burbujam / 10

    tiempos.insertar(promedio_burbujam)
    print("Promedio:", promedio_burbujam)

tiempos.imprimir()

