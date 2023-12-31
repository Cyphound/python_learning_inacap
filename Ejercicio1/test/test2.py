from os import system
import sys
#from back.back2.modulo3 import Jugador
sys.path.append("/Users/bayro/Desktop/Inacap/Segundo Semestre/POO/python_learning_inacap/Ejercicio1/back/back2")
from modulo2 import *
from modulo3 import *

class interfaz:
    def __init__(self):
        self.__listaEquipo = []

    def getListaEquipos(self):
        return self.__listaEquipo

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
        self.__listaEquipo.append(Equipo(id, name, rank))
        print("Equipo Creado! ")


    def verEquipos(self):
        system("cls")
        for i in range(len(ui.getListaEquipos())):
            ui.getListaEquipos()[i].verEquipo()

    # Si lo encuentra, arroja la posición en la lista, caso contrario arroja -1
    def buscarEquipo(self, id):
        posicion = -1
        for i in range(len(self.__listaEquipo)):
            if self.__listaEquipo[i].getId() == id:
                posicion  = i
                break
        return posicion

    def agregarDtEquipo(self):
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        eqAgr = self.buscarEquipo(id)
        msg = "El equipo no existe!"
        if eqAgr  != -1:
            print("Equipo : ",self.__listaEquipo[eqAgr].getNombre(),"\n")
            rut = input("Ingrese el Rut de Dt : ")
            nombre = input("Ingrese el Nombre del Dt : ")
            edad = int(input("Ingrese la Edad del Dt : "))
            titulo = input("Ingrese el Título del Dt : ")
            rendi = input("Ingrese el rendimiento del Dt : ")
            #dt = Dt(rut, nombre, edad, titulo, rendi)
            #self.__listaEquipo[eqAgr].agregarDt2(dt)
            self.__listaEquipo[eqAgr].agregarDt1(rut, nombre, edad, titulo, rendi)
            msg = "Dt agregado correctamente!"
  
        return msg

    def agregarJugadorEquipo(self):
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        eqAgr = self.buscarEquipo(id)
        msg = "El equipo no existe!"
        if eqAgr  != -1:
            print("Equipo : ",self.__listaEquipo[eqAgr].getNombre(),"\n")
            rut = input("Ingrese el Rut del Jugador : ")
            nombre = input("Ingrese el Nombre del Jugador : ")
            edad = int(input("Ingrese la Edad del Jugador : "))
            posicion = input("Ingrese la Posición del Jugador : ")
            numero = int(input("Ingrese el número del Jugador : "))
            goles = int(input("Ingrese la cantidad de Goles del Jugador : "))
            self.__listaEquipo[eqAgr].agregarJugador2(rut, nombre, edad, posicion, numero, goles)
            msg = "Dt agregado correctamente!"
  
        return msg

   
    def eliminarJugadorEquipo(self):
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        eqAgr = self.buscarEquipo(id)
        msg = "El equipo no existe!"
        if eqAgr  != -1:
            print("Equipo : ",self.__listaEquipo[eqAgr].getNombre(),"\n")
            rut = input("Ingrese el Rut del Jugador : ")
            msg = self.__listaEquipo[eqAgr].eliminarJugador(rut)
        return msg

    def eliminarDtEquipo(self):
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        eqAgr = self.buscarEquipo(id)
        msg = "El equipo no existe!"
        if eqAgr  != -1:
            print("Equipo : ",self.__listaEquipo[eqAgr].getNombre(),"\n")
            self.__listaEquipo[eqAgr].eliminarDt()
            msg = "Dt eliminado correctamente!"
        return msg
    
    def verJugadoresEquipo(self):
        system("cls")
        id = input("Ingrese el Id del Equipo : ")
        eqAgr = self.buscarEquipo(id)
        msg = "El equipo no existe!"
        if eqAgr  != -1:
            print("Equipo : ",self.__listaEquipo[eqAgr].getNombre(),"\n")
            print("")
            for i in range(len(ui.getListaEquipos())):
                if id == self.__listaEquipo[i].getId():
                    for jugador in self.__listaEquipo[i].getPlantel():
                        jugador.verJugador()
        else:
            return msg   

    def cargar(self):
        sigue = True
        while(sigue):
            system("cls")
            self.menuOpciones1()
            opc = int(input(" Ingrese una opción : "))
            if opc == 1:
                self.agregarEquipo()
                espera = input("presione ENTER para continuar . . . ")
            elif opc == 2:
                self.verEquipos()
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


#ui.getListaEquipos().append(Equipo("EQ1","Boca Juniors",2))
#for i in range(len(ui.getListaEquipos())):
#    ui.getListaEquipos()[i].verEquipo()
