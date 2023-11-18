
from os import system
import sys
#from back.back2.modulo3 import Jugador
sys.path.append("/Users/bayro/Desktop/Inacap/Segundo Semestre/POO/python_learning_inacap/Ejercicio1/control")

from controlEquipos import *

class interfaz:
    def __init__(self):
        self.__control = GestorEquipos()

    def getControl(self):
        return self.__control

    def menuOpciones1(self):
        system("cls")
        print("Equipo - Menú de opciones")
        print("   1. Agregar Equipo : ")
        print("   2. Ver Equipos : ")
        print("   3. Agregar Dt a un Equipo : ")
        print("   4. Agregar un Jugador a un Equipo : ")
        print("   5. Eliminar a un Jugador de un Equipo : ")
        print("   6. Eliminar al Dt de un Equipo : ")
        print("   7. Ver Jugadores de un Equipo : ")
        print("   8. Salir")
    
    def agregarEquipo(self):
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        name = input("Ingrese el Nombre del Equipo : ")
        rank = int(input("Ingrese el Ranking Mundial del Equipo : ")) 
        return self.__control.agregarEquipo(id, name, rank)

    def verEquipos1(self): #Versión para visualizar equipos que le entrega la labor al controlador
        system("cls")
        self.__control.verEquipos()
        
    def verEquipos2(self): #Versión para visualizar equipos que recibe desde el controlador la lista del equipo y la recorre y muestra en el método
        system("cls")
        equipos = self.__control.getListaEquipos() #se obtiene la lista del equipo
        for i in range(len(equipos)):
            print("Id      : ",equipos[i].getId())
            print("Nombre  : ",equipos[i].getNombre())
            print("Ranking : ",equipos[i].getRank())
            if(equipos[i].getDirige() == None):
                print("Equipo sin Dt aún!")
            else:
                print("Técnico : ")
                equipos[i].getDirige().verDt()
            if(len(equipos[i].getPlantel()) == 0):
                print("No hay jugadores aún")
            else:
                print("Plantel : ")
                for jugador in equipos[i].getPlantel():
                    jugador.verJugador()
            print("")

    def buscarEquipo(self, id):
        system("cls")
        return self.__control.buscarEquipo(id)

    def agregarDtEquipo(self):
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        eqAgr = self.buscarEquipo(id)
        msg = "El equipo no existe!"
        if eqAgr  != -1:
            print("Equipo : ",self.__control.getListaEquipos()[eqAgr].getNombre(),"\n")
            rut = input("Ingrese el Rut de Dt : ")
            nombre = input("Ingrese el Nombre del Dt : ")
            edad = int(input("Ingrese la Edad del Dt : "))
            titulo = input("Ingrese el Título del Dt : ")
            rendi = input("Ingrese el rendimiento del Dt : ")
            self.__control.agregarDtEquipo(eqAgr, rut, nombre, edad, titulo, rendi)           
            msg = "Dt agregado correctamente!"  
        return msg


    def agregarJugadorEquipo(self):
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        eqAgr = self.buscarEquipo(id)
        msg = "El equipo no existe!"
        if eqAgr  != -1:
            print("Equipo : ",self.__control.getListaEquipos()[eqAgr].getNombre(),"\n")
            rut = input("Ingrese el Rut del Jugador : ")
            nombre = input("Ingrese el Nombre del Jugador : ")
            edad = int(input("Ingrese la Edad del Jugador : "))
            posicion = input("Ingrese la posicion del Jugador : ")
            numero = int(input("Ingrese el numero del Jugador : "))
            goles = int(input("Ingrese los goles del Jugador : "))
            self.__control.agregarJugador(eqAgr, rut, nombre, edad, posicion, numero, goles)           
            msg = "Jugador agregado correctamente!"  
        return msg 

   
    def eliminarJugadorEquipo(self):
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        eqAgr = self.buscarEquipo(id)
        msg = "El equipo no existe!"
        if eqAgr  != -1:
            print("Equipo : ",self.__control.getListaEquipos()[eqAgr].getNombre(),"\n")
            rut = input("Ingrese el Rut del Jugador : ")
            self.__control.eliminarJugador(eqAgr, rut)
            msg = "Jugador eliminado correctamente!"
        return msg

    def eliminarDtEquipo(self):
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        eqAgr = self.buscarEquipo(id)
        msg = "El equipo no existe!"
        if eqAgr  != -1:
            print("Equipo : ",self.__control.getListaEquipos()[eqAgr].getNombre(),"\n")
            self.__control.eliminarDt(eqAgr)
            msg = "Dt eliminado correctamente!"
        return msg
    
    def verJugadoresEquipo(self):
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        eqAgr = self.buscarEquipo(id)
        msg = "El equipo no existe!"
        if eqAgr  != -1:
            print("Equipo : ",self.__control.getListaEquipos()[eqAgr].getNombre(),"\n")
            print("")
            self.__control.verJugadoresEquipos(eqAgr)
        else:
            print(msg)

    def cargar(self):
        sigue = True
        while(sigue):
            system("cls")
            self.menuOpciones1()
            opc = int(input(" Ingrese una opción : "))
            if opc == 1:
                print(self.agregarEquipo())
                espera = input("presione ENTER para continuar . . . ")
            elif opc == 2:
                self.verEquipos2()
                espera = input("presione ENTER para continuar . . . ")
            elif opc == 3:
                print(self.agregarDtEquipo())
                espera = input("presione ENTER para continuar . . . ")
            elif opc == 4:
                print(self.agregarJugadorEquipo())
                g = input("presione ENTER para continuar . . . ")
            elif opc == 5:
                print(self.eliminarJugadorEquipo())
                g = input("presione ENTER para continuar . . . ")
            elif opc == 6:
                print(self.eliminarDtEquipo())
                g = input("presione ENTER para continuar . . . ")
            elif opc == 7:
                self.verJugadoresEquipo()
                g = input("presione ENTER para continuar . . . ")
            else:
                sigue = False

ui = interfaz()
ui.cargar()