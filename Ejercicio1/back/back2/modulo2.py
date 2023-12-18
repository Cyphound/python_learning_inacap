from modulo3 import *
class Equipo:
    def __init__(self, id, nombre, rank):
        self.__id = id
        self.__nombre = nombre
        self.__rank = rank
        self.__dirige = None
        self.__plantel = []

    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def getRank(self):
        return self.__rank

    def getDirige(self):
        return self.__dirige
    
    def getPlantel(self):
        return self.__plantel

    def setPlantel(self, plantel):
        self.__plantel = plantel

    def setDirige(self, dirige):
        self.__dirige = dirige

    def setId(self, id):
        self.__id = id
    
    def setRank(self, rank):
        self.__rank = rank

    def setNombre(self, nombre):
        self.__nombre = nombre

    def verEquipo(self):
        print("Id      : ",self.__id)
        print("Nombre  : ",self.__nombre)
        print("Ranking : ",self.__rank)
        if(self.__dirige == None):
            print("Equipo sin Dt aún!")
        else:
            print("Técnico : ")
            self.__dirige.verDt()
        if(len(self.__plantel) == 0):
            print("No hay jugadores aún")
        else:
            print("Plantel : ")
            for i in range(len(self.__plantel)):
                self.__plantel[i].verJugador()
        print("")

    
    def agregarDt1(self, rut, nombre, edad, titulo, rendimiento):
        self.__dirige = Dt(rut, nombre, edad, titulo, rendimiento)
    
    def agregarDt2(self, dt):
        self.__dirige = dt
    
    def agregarJugador1(self, jugador):
        self.__plantel.append(jugador)
    
    def agregarJugador2(self, rut, nombre, edad, posicion, numero, goles):
        self.__plantel.append(Jugador(rut, nombre, edad, posicion, numero, goles))

    def eliminarJugador(self, rut):
        inElim = -1
        msg = "Jugador no existe en el equipo!"
        for i in range(len(self.__plantel)):
            if self.__plantel[i].getRut() == rut:
                inElim = i
                break
        if inElim  != -1:
            self.__plantel.pop(inElim)
            msg = "Jugador eliminado correctamente!"                
        return msg

    def eliminarDt(self):
        self.__dirige = None

    def calcularPromedio(self):
        acum = 0
        
        for jugador in range(len(self.__plantel)):
            acum += jugador.getEdad()

        promedio = acum / len(self.__plantel)

        return promedio
    
    def cambiarEquipo(self, rut):
        a = -1
        for jugador in range(self.__plantel):
            if jugador.getRut() == rut:
                cambio = jugador.pop(jugador)
                a = 1
                break      

        if a == -1:
            print("El jugador no existe")
        else:
            return cambio
            

            
        


        

