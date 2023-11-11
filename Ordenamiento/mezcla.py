from lista import Lista
from all_sort import ordenamientoMezcla
import random
import time

tiempos = Lista()

for i in range(1, 6):
    total_tiempo_mezcla = 0

    for j in range(10):
        lista = Lista()

        for j in range(250 * i):
            lista.insertar(random.randint(0, 100000))

        print("Lista generada")

        ini_mezcla = time.time()
        ordenamientoMezcla(lista)
        fin_mezcla = time.time()

        tiempo_mezcla = fin_mezcla - ini_mezcla
        print(tiempo_mezcla)
        total_tiempo_mezcla += tiempo_mezcla

    promedio_mezcla = total_tiempo_mezcla / 10

    tiempos.insertar(promedio_mezcla)
    print("Promedio:", promedio_mezcla)

tiempos.imprimir()

