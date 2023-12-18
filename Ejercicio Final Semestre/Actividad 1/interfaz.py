## Bayron Gómez ##

from os import system
from model.ObjetosDAO import *
from model.ObjetosDTO import *

class Inter:
    def __init__(self):
        self.objBd = BdDao()

    def menu(self):
        system("cls")
        print("    MENU PRINCIPAL")
        print("    --------------")
        print("    1. Ver Paises")
        print("    2. Ver Ciudades")
        print("    3. Ver Pais")
        print("    4. Ver Ciudad")
        print("    5. Agregar Pais")
        print("    6. Agregar Ciudad")
        print("    7. Actualizar Pais")
        print("    8. Actualizar Ciudad")
        print("    9. Eliminar Pais")
        print("    10. Eliminar Ciudad")
        print("    11. Salir")
        print("")

    def verPaises(self):
        system("cls")
        self.objBd.verPaises()

    def verCiudades(self):
        system("cls")
        self.objBd.verCiudades()
    
    def verPais(self):
        system("cls")
        id = input("Ingrese el id del pais: ")
        self.objBd.verPais(id)

    def verCiudad(self):
        system("cls")
        id = input("Ingrese el id de la ciudad: ")
        self.objBd.verCiudad(id)

    def agregarPais(self):
        system("cls")
        id = input("Ingrese el id del pais: ")
        nombre = input("Ingrese el nombre del pais: ")
        nHabitantes = input("Ingrese el numero de habitantes del pais: ")
        superficie = input("Ingrese la superficie del pais: ")
        pais = Pais(id, nombre, nHabitantes, superficie)
        print(self.objBd.agregarPais(pais))

    def agregarCiudad(self):
        system("cls")
        id = input("Ingrese el id de la ciudad: ")
        nombre = input("Ingrese el nombre de la ciudad: ")
        postal = input("Ingrese el codigo postal de la ciudad: ")
        pais = input("Ingrese el codigo del pais de la ciudad: ")
        ciudad = Ciudad(id, nombre, postal, pais)
        print(self.objBd.agregarCiudad(ciudad))

    def actualizarPais(self):
        system("cls")
        id = input("Ingrese el id del pais: ")
        nombre = input("Ingrese el nuevo nombre del pais: ")
        nHabitantes = input("Ingrese el nuevo numero de habitantes del pais: ")
        superficie = input("Ingrese la nueva superficie del pais: ")
        print(self.objBd.actualizarPais(id, nombre, nHabitantes, superficie))

    def actualizarCiudad(self):
        system("cls")
        id = input("Ingrese el id de la ciudad: ")
        nombre = input("Ingrese el nuevo nombre de la ciudad: ")
        postal = input("Ingrese el nuevo codigo postal de la ciudad: ")
        pais = input("Ingrese el nuevo codigo del pais de la ciudad: ")
        print(self.objBd.actualizarCiudad(id, nombre, postal, pais))

    def eliminarPais(self):
        system("cls")
        id = input("Ingrese el id del pais: ")
        print(self.objBd.eliminarPais(id))

    def eliminarCiudad(self):
        system("cls")
        id = input("Ingrese el id de la ciudad: ")
        print(self.objBd.eliminarCiudad(id))

    def CargarIu(self):
        while True:
            self.menu()
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                self.verPaises()
            elif opcion == "2":
                self.verCiudades()
            elif opcion == "3":
                self.verPais()
            elif opcion == "4":
                self.verCiudad()
            elif opcion == "5":
                self.agregarPais()
            elif opcion == "6":
                self.agregarCiudad()
            elif opcion == "7":
                self.actualizarPais()
            elif opcion == "8":
                self.actualizarCiudad()
            elif opcion == "9":
                self.eliminarPais()
            elif opcion == "10":
                self.eliminarCiudad()
            else:
                break
            input("Presione una tecla para continuar...")

a = Inter()
a.CargarIu()