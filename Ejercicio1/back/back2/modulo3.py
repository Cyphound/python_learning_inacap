
import sys

sys.path.append('/Users/bayro/Desktop/Inacap/Segundo Semestre/POO/python_learning_inacap/Ejercicio1/back/back1')

from modulo1 import *

class Dt(Persona):
    def __init__(self, rut, nombre, edad, titulo, rendimiento):
        super().__init__(rut, nombre, edad)
        self.__titulo = titulo
        self.__rendimiento = rendimiento

    def getTitulo(self):
        return self.__titulo

    def getRendimiento(self):
        return self.__rendimiento

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setRendimeinto(self, rendimiento):
        self.__rendimiento = rendimiento

    def verDt(self):
        self.verPersona()
        print("  Rendimiento : ", self.__rendimiento, "%")
        print("  Titulo      : ", self.__titulo, "\n")

class Jugador(Persona):
    ## Se agregan los atributos acorde al diagrama mostrado
    def __init__(self, rut, nombre, edad, posicion, numero, goles):
        super().__init__(rut, nombre, edad)
        self.__posicion = posicion
        self.__numero = numero
        self.__goles = goles

    ## Getters
    def getPosicion(self):
        return self.__posicion

    def getNumero(self):
        return self.__numero

    def getGoles(self):
        return self.__goles

    ## Setters
    def setPosicion(self, posicion):
        self.__posicion = posicion

    def setNumero(self, numero):
        self.__numero = numero

    def setGoles(self, goles):
        self.__goles = goles

    ## Método para ver los datos del jugador heredando el método verPersona
    def verJugador(self):
        self.verPersona()
        print("  Posición    : ", self.__posicion)
        print("  Número      : ", self.__numero)
        print("  Goles       : ", self.__goles, "\n")


