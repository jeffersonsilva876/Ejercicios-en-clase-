import os
class Matriz:
    def __init__(self,matriz,fila,col):
        self.matriz = matriz
        self.fila = fila
        self.col = col


    def ingresar(self):
        self.matriz=[]
        for fila in range(self.fila):
            columnas= []
            os.system("cls")
            for col in range(self.col):
                valor = int(input("Fila[{}] Col[{}]: ".format(fila,col)))
                columnas.append(valor)
            self.matriz.append(columnas)

    def presentar(self):
        # os.system("cls")
        print("_______")
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                #print(columna[col],end=" ")
                print("[{}]".format(int(self.matriz[fila][col])),end=" ")
            print("")

    def buscar(self,valor):
        enc ={}
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz)):
                if self.matriz[fila][col] == (valor):
                    enc["fila"]=fila
                    enc["col"]=col
                    break
            if enc: break
        return enc

    def buscarw(self,valor):
        enc ={}
        fila = 0
        band = True
        while fila < len(self.matriz) and band:
            col =0
            while col < len(self.matriz) and band:
                if self.matriz[fila][col] == valor:
                    enc["fila"]=fila
                    enc["col"]=col
                    band = False
                else: col+=1
            fila += 1
        return enc

    def suma(self,matriz2):
        matrizSuma = []
        for fila in range(self.fila):
            columnas = []
            for col in range(self.col):
                valor = self.matriz[fila][col]+ matriz2[fila][col]
                columnas.append(valor)
            matrizSuma.append(columnas)
        return matrizSuma
# print(numeros[0],numeros[0][1])
numeros=[[2,3],[2,3]]
mat1 = Matriz(numeros,2,2)
mat2 = Matriz(numeros,2,2)
# mat1.ingresar()
# mat2.ingresar()
mat1.presentar()
mat2.presentar()
mat1.matriz = mat1.suma(mat2.matriz)
mat1.presentar()
# resp = mat.buscar(5)
# if resp: print("El valor se encuentra en: ",resp)
# else: print("No se encuentra el valor")
# resp = mat.buscarw(55)
# if resp: print("El valor se encuentra en: ",resp)
# else: print("No se encuentra el valor")