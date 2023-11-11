from lista import Lista
from all_sort import seleccion
import random
import time

tiempos = Lista()

for i in range(1, 6):
    total_tiempo_seleccion = 0

    for j in range(10):
        lista = Lista()

        for j in range(250 * i):
            lista.insertar(random.randint(0, 100000))

        print("Lista generada")

        ini_seleccion = time.time()
        seleccion(lista)
        fin_seleccion = time.time()

        tiempo_seleccion = fin_seleccion - ini_seleccion
        print(tiempo_seleccion)
        total_tiempo_seleccion += tiempo_seleccion

    promedio_seleccion = total_tiempo_seleccion / 10

    tiempos.insertar(promedio_seleccion)
    print("Promedio:", promedio_seleccion)

tiempos.imprimir()


