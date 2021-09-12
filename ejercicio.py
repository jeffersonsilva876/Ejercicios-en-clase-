lista = [[10,30,40], [70,85,90], [25,35,55], [43,75,90]]

acum = 0 
for fila in range(0,len(lista)):
    print(fila,end=" ")
    acump= 0
    for col in range(0,len(lista[fila])):
        print("[{}]".format(lista[fila][col]),end=" ")
        acum=acum + lista[fila][col]
        acump+= lista[fila][col]
    print(acump)
print("La suma total de elementos:{}".format(acum))