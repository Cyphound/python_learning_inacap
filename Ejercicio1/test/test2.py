
import sys
from os import system
sys.path.append('/Users/bayro/Desktop/Inacap/Segundo Semestre/POO/python_learning_inacap/Ejercicio1/back/back2')
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
        print("   5. Eliminar al DT de un Equipo : ")
        print("   6. Eliminar a un jugador de un Equipo : ")
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

    def agregarJugador(self):
        estado = False
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        for i in range(len(ui.getListaEquipo())):
            if id == ui.getListaEquipo()[i].getId():
                rut = input("Ingrese el Rut del Jugador : ")
                nombre = input("Ingrese el nombre del Jugador : ")
                edad = int(input("Ingrese la edad del Jugador : "))
                posicion = input("Ingrese la posicion del Jugador : ")
                numero = int(input("Ingrese el numero del Jugador : "))
                goles = int(input("Ingrese la cantidad de goles del Jugador : "))
                ui.getListaEquipo()[i].agregarJugador1(rut, nombre, edad, posicion, numero, goles)
                print("Jugador agregado!")
                estado = True
                break

        if estado == False:
            print("Equipo no encontrado")

    def sacarDt(self):
        estado = 1
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        for i in range(len(ui.getListaEquipo())):
            if id == ui.getListaEquipo()[i].getId():
                if ui.getListaEquipo()[i].getDirige() == None:
                    estado = 2
                    break
                else:
                    ui.getListaEquipo()[i].eliminarDt()
                    estado = 3
                    break

        if estado == 1:
            print("Equipo no encontrado!")
        elif estado == 2:
            print("Equipo no posee DT!")
        else:
            print("DT Eliminado!")

    def sacarJugador(self):
        estado = 1
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        rut = input("Ingrese el Rut del jugador : ")
        for i in range(len(ui.getListaEquipo())):
            if id == ui.getListaEquipo()[i].getId():
                for jugador in ui.getListaEquipo()[i].getJugadores():
                    if jugador.getRut() != rut:
                        estado = 2
                    else:
                        ui.getListaEquipo()[i].eliminarJugador(rut)
                        estado = 3
                        break

        if estado == 1:
            print("Equipo no encontrado!")
        elif estado == 2:
            print("Ningun jugador coincide con el Rut ingresado")
        else:
            print("Jugador Eliminado!")

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
            elif opc == 4:
                self.agregarJugador()
                g = input("Presione ENTER para continuar . . .")
            elif opc == 5:
                self.sacarDt()
                g = input("Presione ENTER para continuar . . .")
            elif opc == 6:
                self.sacarJugador()
                g = input("Presione ENTER para continuar . . .")
            else:
                opcion = False
    
# Main

ui = interfaz()
ui.cargar()




#ui.getListaEquipo().append(Equipo("Eq-008", "Deportes Iquique", 10))
#for i in range(len(ui.getListaEquipo())):
#    ui.getListaEquipo()[i].verEquipo()