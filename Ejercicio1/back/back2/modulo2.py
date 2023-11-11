
from modulo3 import *

class Equipo:
    def __init__(self, id, nombre, rank):
        self.__id = id
        self.__nombre = nombre
        self.__rank = rank
        self.__dirige = None
        self.__jugadores = None ## Se agrega el atributo jugadores

    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def getRank(self):
        return self.__rank

    def getDirige(self):
        return self.__dirige

    def getJugadores(self): ## Get de jugadores
        return self.__jugadores

    def setDirige(self, dirige):
        self.__dirige = dirige

    def setJugadores(self, jugadores): ## Set de jugadores
        self.__jugadores = jugadores

    def setId(self, id):
        self.__id = id

    def setRank(self, rank):
        self.__rank = rank

    def setNombre(self, nombre):
        self.__nombre = nombre

    def verEquipo(self):
        print("Id      : ", self.__id)
        print("Nombre  : ", self.__nombre)
        print("Ranking : ", self.__rank)
        if (self.__dirige == None):
            print("Equipo sin Dt aún!")
        else:
            print("Técnico : ")
            self.__dirige.verDt()
        ## Si no hay jugadores, se imprime un "Error"
        if (self.__jugadores == None):
            print("Equipo sin jugadores aún!", "\n")
            ## Agrege un salto de linea para que se vea mejor la impresion
        else:
            ## Si hay jugadores, se imprimen mediante un for que recorre la lista
            print("Jugadores : ")
            for i in self.__jugadores:
                i.verJugador()

    def agregarDt1(self, rut, nombre, edad, titulo, rendimiento):
        self.__dirige = Dt(rut, nombre, edad, titulo, rendimiento)

    def agregarDt2(self, dt):
        self.__dirige = dt

    ## Metodo 1 para agregar jugadores, se crea el objeto jugador en el mismo metodo
    def agregarJugador1(self, rut, nombre, edad, posicion, numero, goles):
        if self.__jugadores == None:
            self.__jugadores = []
        jugador = Jugador(rut, nombre, edad, posicion, numero, goles)

        self.__jugadores.append(jugador)

    ## Metodo 2 para agregar jugadores, se recibe el objeto jugador como parametro
    def agregarJugador2(self, jugador):
        if self.__jugadores == None:
            self.__jugadores = []
        self.__jugadores.append(jugador)

    def eliminarJugador(self, rut):
        
        eliminacion = False

        for i in range(len(self.__jugadores)):
            if rut == self.__jugadores[i].rut:
                self.__jugadores.pop(i)
                eliminacion = True

        if eliminacion:
            print("Jugador Eliminado", "\n")
        else:
            print("Jugador no encontrado!", "\n")

    def eliminarDt(self):
        self.__dirige = None
        print("Dt Eliminado", "\n")
            
