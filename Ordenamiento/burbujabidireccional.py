from lista import Lista
from all_sort import burbujaBidireccional
import random
import time

tiempos = Lista()

for i in range(1, 6):
    total_tiempo_burbujabi = 0

    for j in range(10):
        lista = Lista()

        for j in range(250 * i):
            lista.insertar(random.randint(0, 100000))

        print("Lista generada")
        
        inicio_burbujabi = time.time()
        burbujaBidireccional(lista)
        fin_burbujabi = time.time()

        tiempo_burbujabi = fin_burbujabi - inicio_burbujabi
        print(tiempo_burbujabi)
        total_tiempo_burbujabi += tiempo_burbujabi

    promedio_burbujabi = total_tiempo_burbujabi / 10

    tiempos.insertar(promedio_burbujabi)
    print("Promedio:", promedio_burbujabi)

tiempos.imprimir()
