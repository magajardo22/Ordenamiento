class nodoselfSimple(object):
    info, siguiente = None, None


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


    def insertar(self, info):
        nodo = nodoselfSimple()
        nodo.info = info
        if self.inicio is None:
            nodo.siguiente = self.inicio
            self.inicio = nodo
        else:
            actual = self.inicio
            siguiente = self.inicio.siguiente
            while siguiente is not None:
                actual = actual.siguiente
                siguiente = siguiente.siguiente
            nodo.siguiente = siguiente
            actual.siguiente = nodo
        self.tamanio += 1


    def imprimir(self):
        actual = self.inicio
        txt = "["
        while actual is not None:
            if actual.siguiente != None:
                txt = f"{txt}{actual.info}, "
            else:
                txt = f"{txt}{actual.info}]"
            actual = actual.siguiente
        print(txt)


    def get_tamanio(self):
        return self.tamanio


    def eliminar(self, info):
        data = None
        # saber si es el primero de la self
        if(self.inicio.info == info):
            data = self.inicio
            self.inicio = self.inicio.siguiente
            self.tamanio -= 1
        else:
            actual = self.inicio
            siguiente = self.inicio.siguiente
            while (siguiente is not None and info != siguiente.info):
                actual = actual.siguiente
                siguiente = siguiente.siguiente
            # saber si es el ultimo de la self
            if(siguiente is not None):
                data = siguiente.info
                actual.siguiente = siguiente.siguiente
                self.tamanio -= 1
        return data


    def index_of(self, info):
        actual = self.inicio
        index = 0
        for _ in range(self.tamanio):
            if actual.info == info:
                return index
            index += 1
            actual = actual.siguiente

        return None


    def index(self, indice):
        actual = self.inicio
        for _ in range(indice):
            actual = actual.siguiente
            if actual == None:
                return None
        return actual.info


    def reemplazo(self, indice, info):
        actual = self.inicio
        for _ in range(indice):
            actual = actual.siguiente
            if actual == None:
                return None
        actual.info = info


    def extraer(self, indice):
        actual = self.inicio
        for _ in range(indice):
            actual = actual.siguiente
            if actual == None:
                return None
        data = actual.info
        self.eliminar(data)
        return data


    def index_of_param(self, param):
        actual = self.inicio
        while actual.info is not param:
            pass
