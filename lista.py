class Lista:
    def __init__(self,tam=3):
        self.lista=[]
        self.longitud = 0
        self.size = tam

    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud += 1
            return True
        else:
            return False

    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            x = "el valor en la posicion {} es {}".format(pos,self.lista[pos])
            return x

    def obtenerEliminando(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            eliminado = self.lista[pos]
            self.lista = self.lista[:pos] + self.lista[pos+1:]
            print( "La lista queda tal que: {} y el elemento eliminado es {}".format(self.lista,eliminado))
            #listaAux = []
            # for ind in range(pos):
            #     listaAux += [self.lista[ind]]
            # for ind in range(pos+1,self.longitud):
            #     listaAux += [self.lista[ind]]
            # self.longitud -= -1
            # self.lista[pos] = listaAux
            # print(eliminado,self.lista)

    #busca un valor en la lista y coloca la posicion de ese valor en la lista
    def buscar(self,dato):
        if dato in self.lista:
            self.res = self.lista.index(dato)
            print("la posicion del dato es ",self.res)
            return True
        else:
            return False

    #busca un dato con el metodo buscar y si no lo encuentra lo inserta
    # usar appendemetodo
    def insertar(self,dato):
        if self.buscar(dato) == False:
            self.size += 1
            self.append(dato)
        return self.lista

    # busca el dato con el metodo buscar y si lo encuntra lo elimina de la lista
    def eliminar(self,dato):
        if self.buscar(dato) == True:
            self.obtenerEliminando(self.res)
        else:
            False

    def mostrar(self):
        print("{:3}{:9}{}".format("","lista","posicion"))
        for pos, ele in enumerate(self.lista):
            print("[{:10}] {:3}".format(ele,pos))
#
# lista1 = Lista()
# lista1.append("Daniel")
# lista1.append(52)
# lista1.append(True)
# # print(lista1.obtener(1))
# lista1.eliminar("Daniel")
# print(lista1.buscar(52))
# print(lista1.insertar(53))
#lista1.append("Milagro")
# lista1.mostrar()
# lista1.mostrar()
# posicion = int(input("Ingrese posicion para obtener: "))
# resp = lista1.obtenerEliminando(posicion)
# if resp == None:
#     print("Posicion no Valida. verifique la lista...!!!")
# else:
#     print("El elemento de la posicion: {} indicado es: {} ".format(posicion,resp))