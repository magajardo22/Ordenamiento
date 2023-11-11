from lista import Lista
from all_sort import insercion
import random
import time

tiempos = Lista()

for i in range(1, 6):
    total_tiempo_insercion = 0

    for j in range(10):
        lista = Lista()

        for j in range(250 * i):
            lista.insertar(random.randint(0, 100000))

        print("Lista generada")

        ini_insercion = time.time()
        insercion(lista)
        fin_insercion = time.time()

        tiempo_insercion = fin_insercion - ini_insercion
        print(tiempo_insercion)
        total_tiempo_insercion += tiempo_insercion

    promedio_insercion = total_tiempo_insercion / 10

    tiempos.insertar(promedio_insercion)
    print("Promedio:", promedio_insercion)

tiempos.imprimir()

