from os import system
import sys

sys.path.append("/Users/bayro/Desktop/Inacap/Segundo Semestre/POO/python_learning_inacap/Ejercicio1/back/back2")
from modulo2 import *
from modulo3 import *


class GestorEquipos:
    
    def __init__(self):
        self.__listaEquipos = []
    
    def getListaEquipos(self):
        return self.__listaEquipos 

    def setListaEquipos(self, equipos):
        self.__listaEquipos = equipos

    def agregarEquipo(self, id, name, rank):
        self.__listaEquipos.append(Equipo(id, name, rank))
        return "Equipo Creado!"
    
    def verEquipos(self):
        for i in range(len(self.__listaEquipos)):
            self.__listaEquipos[i].verEquipo()
    
    def getListaEquipos(self):
        return self.__listaEquipos 

    def buscarEquipo(self, id):
        posicion = -1
        for i in range(len(self.__listaEquipos)):
            if self.__listaEquipos[i].getId() == id:
                posicion  = i
                break
        return posicion
        
    def agregarDtEquipo(self,indice, rut, nombre, edad, titulo, rendimiento):
        self.__listaEquipos[indice].agregarDt1(rut, nombre, edad, titulo, rendimiento)

    def eliminarDt(self, indice):
        self.__listaEquipos[indice].eliminarDt()

    def agregarJugador(self, indice, rut, nombre, edad, posicion, numero, goles):
        self.__listaEquipos[indice].agregarJugador2(rut, nombre, edad, posicion, numero, goles)

    def eliminarJugador(self, indice, rut):
        self.__listaEquipos[indice].eliminarJugador(rut)

    def verJugadoresEquipos(self,indice):
        for jugador in self.__listaEquipos[indice].getPlantel():
            jugador.verJugador()

    def promedioEquipoControl(self, indice):
        prom = self.__listaEquipos[indice].calcularPromedio()

        return prom
    
    def cambioControl(self, origen, destino, rut):
        self.__listaEquipos[destino].agregarJugador1(self.__listaEquipos[origen].cambiarEquipo(rut))