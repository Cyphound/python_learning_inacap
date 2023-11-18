import sys
sys.path.append("/Users/bayro/Desktop/Inacap/Segundo Semestre/POO/python_learning_inacap/Ejercicio1/back/back1")
from modulo1 import Persona


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
        print("    Rendimiento : ",self.__rendimiento,"%")
        print("    Titulo      : ",self.__titulo,"\n")
       
class Jugador(Persona):
    def __init__(self, rut, nombre, edad, posicion, numero, goles):
        super().__init__(rut, nombre, edad)
        self.__posicion = posicion
        self.__numero = numero
        self.__goles = goles

    def getPosicion(self):
        return self.__posicion

    def getNumero(self):
        return self.__numero

    def getGoles(self):
        return self.__goles

    def setPosicion(self, nuevaPosicion):
        self.__posicion = nuevaPosicion

    def setNumero(self, nuevoNumero):
        self.__numero = nuevoNumero

    def setGoles(self, nuevosGoles):
        self.__goles = nuevosGoles

    def verJugador(self):
        self.verPersona()
        print("    Posición : ",self.__posicion)
        print("    Número   : ",self.__numero)
        print("    Goles    : ",self.__goles,"\n")

    




