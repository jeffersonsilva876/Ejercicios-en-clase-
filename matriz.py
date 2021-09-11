class Matriz:
    def __init__(self,matriz):
        self.matriz = matriz
        
    def mostrar(self):
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
               print(self.matriz[fila][col],end=" ")
            print()

numeros=[[10,20,30,70],[60,100,90],[25,35,55,67,54]]
mat= Matriz(numeros)
mat.mostrar()