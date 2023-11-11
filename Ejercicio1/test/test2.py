
import sys
from os import system
sys.path.append('/Inacap/Segundo Semestre/POO/Ejercicio1/back/back2')
from modulo2 import *

class interfaz:
    def __init__(self):
        self.__listaEquipo = []

    def getListaEquipo(self):
        return self.__listaEquipo
    
    def menuOpciones1(self):
        system("cls")
        print("Equipo - Menú de opciones")
        print("   1. Agregar Equipo : ")
        print("   2. Ver Equipos : ")
        print("   3. Agregar DT a un Equipo : ")
        print("   4. Agregar un jugador a un Equipo : ")
        print("   5. Eliminar a un jugador de un Equipo : ")
        print("   6. Eliminar al DT de un Equipo : ")
        print("   7. Salir")

    def agregarEquipo(self):
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        name = input("Ingrese el nombre del Equipo : ")
        ranking = int(input("Ingrese el ranking del Equipo : "))
        self.__listaEquipo.append(Equipo(id, name, ranking))
        print("Equipo creado!")

    def verEquipo(self):
        system("cls")
        for i in range(len(ui.getListaEquipo())):
            ui.getListaEquipo()[i].verEquipo()

    def agregarDt(self):
        estado = False
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        for i in range(len(ui.getListaEquipo())):
            if id == ui.getListaEquipo()[i].getId():
                rut = input("Ingrese el Rut del DT : ")
                nombre = input("Ingrese el nombre del DT : ")
                edad = int(input("Ingrese la edad del DT : "))
                titulo = input("Ingrese el titulo del DT : ")
                rendimiento = int(input("Ingrese el rendimiento del DT : "))
                ui.getListaEquipo()[i].agregarDt1(rut, nombre, edad, titulo, rendimiento)
                print("Dt agregado!")
                estado = True
                break

        if estado == False:
            print("Equipo no encontrado")


    def cargar(self):
        opcion = True
        while(opcion):
            system("cls")
            self.menuOpciones1()
            opc = int(input(" Ingrese una opción : "))
            if opc == 1:
                self.agregarEquipo()
                g = input("Presione ENTER para continuar . . .")
            elif opc == 2:
                self.verEquipo()
                g = input("Presione ENTER para continuar . . .")
            elif opc == 3:
                self.agregarDt()
                g = input("Presione ENTER para continuar . . .")
            else:
                opcion = False
    
ui = interfaz()
ui.cargar()




#ui.getListaEquipo().append(Equipo("Eq-008", "Deportes Iquique", 10))
#for i in range(len(ui.getListaEquipo())):
#    ui.getListaEquipo()[i].verEquipo()