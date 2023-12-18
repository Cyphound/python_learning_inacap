from os import system
from model.objetosBD import UsuarioDB
#import sys

#sys.path.append("/Users/bayro/Desktop/Inacap/Segundo Semestre/POO/python_learning_inacap/3ra Unidad/model")

class Inter:
    def __init__(self):
        self.objUsuario = UsuarioDB()

    def verUsuarios(self):
        system("cls")
        self.objUsuario.verUusarios()

    def verUsuario(self):
        system("cls")
        id = input(" Ingrese el ID del usuario : ")
        pass

    def agregarUsuario(self):
        system("cls")
        id = input(" Ingrese el ID del usuario : ")
        nombre = input(" Ingrese el nombre del usuario : ")
        edad = int(input(" Ingrese la edad del usuario : "))
        pass

    def menuPrincipal(self):
        print(" Menu opciones de Usuarios ")
        print(" 1. Ver Usuarios")
        print(" 2. Ver Usuario")
        print(" 3. Agregar Usuario")
        print(" 4. Eliminar Usuario")
        print(" 5. Actualizar datos de un Usuario")
        print(" 6. Salir")

    def cargarUi(self):
        sigue = True
        while sigue:
            system("cls")
            self.menuPrincipal()
            opcion = int(input(" Ingrese una opcion : "))
            if opcion == 1:
                self.verUsuarios()
                espera = input(" Presione ENTER para continuar ... ")
            elif opcion == 2:
                self.verUsuario()
                espera = input(" Presione ENTER para continuar ... ")
            elif opcion == 3:
                self.agregarUsuario()
                espera = input(" Presione ENTER para continuar ... ")
            elif opcion == 4:
                espera = input(" Presione ENTER para continuar ... ")
            elif opcion == 5:
                espera = input(" Presione ENTER para continuar ... ")
            else:
                sigue = False

## Main
                
i = Inter()
i.cargarUi()
