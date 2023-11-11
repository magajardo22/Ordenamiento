from lista import Lista

def burbuja(lista):
    tamanio_lista = lista.get_tamanio()
    for i in range(tamanio_lista - 1):
        for j in range(tamanio_lista - i - 1):
            indice_actual = j
            indice_siguiente = j + 1
            if lista.index(indice_actual) > lista.index(indice_siguiente):
                elemento_actual = lista.index(indice_actual)
                lista.reemplazo(indice_actual, lista.index(indice_siguiente))
                lista.reemplazo(indice_siguiente, elemento_actual)

def burbujaMejorada(lista):
    i = 0
    control = True
    while i <= lista.get_tamanio() - 2 and control:
        control = False
        for j in range(0, lista.get_tamanio() - i - 1):
            if lista.index(j) > lista.index(j + 1):
                lista.reemplazo(j, j + 1)
                control = True
        i += 1

def burbujaBidireccional(lista):
    izquierda = 0
    derecha = lista.get_tamanio() - 1
    control = True
    while izquierda < derecha and control:
        control = False
        for i in range(izquierda, derecha):
            if lista.index(i) > lista.index(i + 1):
                lista.reemplazo(i, i + 1)
                control = True
        derecha -= 1
        for j in range(derecha, izquierda, -1):
            if lista.index(j) < lista.index(j - 1):
                lista.reemplazo(j, j - 1)
                control = True
        izquierda += 1

def seleccion(lista):
    for i in range(0, lista.get_tamanio() - 1):
        minimo = i
        for j in range(i + 1, lista.get_tamanio()):
            if lista.index(j) < lista.index(minimo):
                minimo = j
        lista.reemplazo(i, minimo)

def insercion(lista):
    for i in range(1, lista.get_tamanio()):
        actual = lista.index(i)
        k = i
        while k > 0 and lista.index(k - 1) > actual:
            lista.reemplazo(k, lista.index(k - 1))
            k -= 1
        lista.reemplazo(k, actual)

def ordenamientoRapido(lista, primero, ultimo):
    if primero < ultimo:
        pivote = ultimo
        izquierda = primero
        derecha = ultimo - 1
        while izquierda < derecha:
            while izquierda <= derecha and lista.index(izquierda) < lista.index(pivote):
                izquierda += 1
            while derecha >= izquierda and lista.index(derecha) > lista.index(pivote):
                derecha -= 1
            if izquierda < derecha:
                lista.reemplazo(izquierda, derecha)
        if lista.index(pivote) < lista.index(izquierda):
            lista.reemplazo(izquierda, pivote)
        ordenamientoRapido(lista, primero, izquierda - 1)
        ordenamientoRapido(lista, izquierda + 1, ultimo)


def ordenamientoMezcla(lista):
    if lista.get_tamanio() <= 1:
        return lista
    medio = lista.get_tamanio() // 2
    izquierda = Lista()
    for i in range(medio):
        izquierda.insertar(lista.index(i))
    derecha = Lista()
    for i in range(medio, lista.get_tamanio()):
        derecha.insertar(lista.index(i))
    izquierda = ordenamientoMezcla(izquierda)
    derecha = ordenamientoMezcla(derecha)
    return mezcla(izquierda, derecha)

def mezcla(izquierda, derecha):
    lista_mezclada = Lista()
    i = j = 0
    while i < izquierda.get_tamanio() and j < derecha.get_tamanio():
        if izquierda.index(i) <= derecha.index(j):
            lista_mezclada.insertar(izquierda.extraer(0))
            i += 1
        else:
            lista_mezclada.insertar(derecha.extraer(0))
            j += 1
    while i < izquierda.get_tamanio():
        lista_mezclada.insertar(izquierda.extraer(0))
        i += 1
    while j < derecha.get_tamanio():
        lista_mezclada.insertar(derecha.extraer(0))
        j += 1
    return lista_mezclada


