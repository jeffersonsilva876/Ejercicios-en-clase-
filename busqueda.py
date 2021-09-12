class Lista:
    def __init__(self,listas):
        self.__lista = listas

    @property #para atributos privados
    def lista(self): #getproperty
        # if self.__lista != None:
        #     return self.__lista
        # else: print("Ingrese Lista")
        return self.__lista

    # @lista.setter
    # def lista(self,value): #setproperty
    #     self.__lista = value
    def ordenarQuickSort(self):
        pass

    def busquedaLineal(self,buscado):
        pos = 0
        enc = False
        lon = len(self.__lista)
        # recorre un valor en la lista: retorna posicion si lo encuentra
        while pos < lon and enc== False:
            if self.__lista[pos]["nombre"] == buscado:
                enc = True
            else:
                pos = pos + 1

        if enc: return pos
        else: return -1

    def ordenar(self,orden):
        orden = orden.lower()
        if orden == "asc":
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self.__lista[pos]["nombre"] > self.__lista[sig]["nombre"]:
                        aux = self.__lista[pos]
                        self.__lista[pos]=self.__lista[sig]
                        self.__lista[sig]=aux
        else:
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self.__lista[pos]["nombre"] < self.__lista[sig]["nombre"]:
                        aux = self.__lista[pos]
                        self.__lista[pos]=self.__lista[sig]
                        self.__lista[sig]=aux

    def busquedaBinaria(self,buscado):
        self.ordenar("asc")
        fin =len(self.lista)-1 #guarda la posicion final del segmento
        inicio = 0 #guarda la posicion incial del segmento
        enc = False
        #se busca mientras que la posicion inicial sea menor que la final
        while inicio <= fin and enc ==False:
            medio=(inicio+fin)//2
            if self.lista[medio]["nombre"] == buscado: enc = True
            elif self.lista[medio]["nombre"] > buscado: fin = medio-1
            else: inicio = medio+1
        if enc: return medio
        else: return -1


notas = [
    {"nombre":"Daniel","n1":20,"n2":40},
    {"nombre":"Danny","n1":30,"n2":50},
    {"nombre":"Dayana","n1":40,"n2":50},
    {"nombre":"Erick","n1":50,"n2":40},
    {"nombre":"Romina","n1":55,"n2":40}
]
bus = Lista(notas)
# bus.lista=[3,5]
# print(bus.lista)
# posicion = bus.busquedaLineal("Dayana")
posicion = bus.busquedaBinaria("Erick")
if posicion != -1:
    print(bus.lista[posicion])
else:
    print("Nombre no se encuentra en la lista")
# bus.busquedaLineal("Daniel")
# bus.ordenar("ASC")
# print(bus.lista)