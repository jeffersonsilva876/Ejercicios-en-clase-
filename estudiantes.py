from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArchivos import Archivo
from entidadesUnemi import *
from datetime import date
import time

# Procesos de las Opciones del Menu Mantenimiento
def carreras():
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE CARRERAS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Descripcion Carrera: ")
   gotoxy(33,5)
   descarrera = input()
   archiCarrera = Archivo("./datos/carrera.txt",";")
   carreras = archiCarrera.leer()
   if carreras : idSig = int(carreras[-1][0])+1
   else: idSig=1
   carrera = Carrera(idSig,descarrera)
   datos = carrera.getCarrera()
   datos = ';'.join(datos)
   archiCarrera.escribir([datos],"a")

def materias():
    pass

def profesores():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE PROFESORES")
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula: : ")
   gotoxy(15,6);print("Titulo: : ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   gotoxy(25,4);nom = input()
   gotoxy(25,5);ced = input()
   gotoxy(25,6);tit = input()
   tel=validar.solo_numeros("Error: Solo numeros",25,7)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input().upper()
      archiCarrera = Archivo("./datos/carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
          gotoxy(33,8);print(entCarrera.descripcion)
      else: 
         gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiProfesor = Archivo("./datos/profesor.txt")
        lisProfesores = archiProfesor.leer()
        if lisProfesores : idSig = int(lisProfesores[-1][0])+1
        else: idSig=1
        entProfesor = Profesor(idSig,nom,ced,entCarrera,tit,tel)
        datos = entProfesor.getProfesor()
        datos = ';'.join(datos)
        archiProfesor.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     
# Menu Principal
opc=''
while opc !='5':  
    borrarPantalla()      
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Matriculacion","3) Notas","4) Consultas","5) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='6':
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Carrera","2) Materias","3) Periodos","4) Profesores","5) Estudiantes","6) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                carreras()
            elif opc1 == "4":
                profesores()
                        
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Matriculacion",["1) Matricula","2) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                pass
            elif opc2 == "2":
                pass
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Notas",["1) Notas","2) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                pass
            
    elif opc == "4":
            borrarPantalla()
            menu4 = Menu("Menu Consultas",["1) Carreras","2) Materias","3) Periodos","4) Profesores","5) Estudiantes","6) Notas","7) Matricula","7) Salir"],20,10)
            opc4 = menu4.menu()
            if opc4 == "1":
                borrarPantalla()
                print("Listado de Profesor")
                print("id      Nombre   dpto")
                # leer el archivo carrera y retornar las carrera 
                lista = [["1","Daniel   ",2],["2","Ana",1]]
                archiDepartamento = Archivo("./datos/departamento.txt")
                lisDepartamento = archiDepartamento.buscar(id)
                if lisDepartamento:
                    print(1,"Daniel" ,lisDepartamento[1])
                    print(2,"Ana",2)
                input("      Presione una tecla para continuar...")
    elif opc == "5":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

