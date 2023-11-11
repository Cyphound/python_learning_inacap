
## Bayron Gómez
## Comentare todo lo que hare para que se pueda entender mejor el codigo :b


class Persona:
    def __init__(self, rut, nombre, edad):
        self.edad = edad
        self.nombre = nombre
        self.rut = rut

    def getRut(self):
        return self.nombre

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def setRut(self, rut):
        self.rut = rut

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def verPersona(self):
        print("  Rut         : ", self.rut)
        print("  Nombre      : ", self.nombre)
        print("  Edad        : ", self.edad)

    def __str__(self):
        return "  Rut         : " + self.rut + "\n  Nombre      : " + self.nombre + "\n  Edad        : " + str(
            self.edad) + "\n"


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


## Se crea la clase Jugador que hereda de Persona
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


## Main

## Dejare esta parte tal como esta y creare otro equipo para demostrar el funcionamiento de este
a = Persona("14-6", "Emerson Ilaja", 48)
a.verPersona()
print(a)

b = Dt("50-9", "Manuel Pellegrini", 70, "Ingeniero Civil", 75)
b.verDt()

c = Equipo("Eq-001", "Cobreloa", 12)
c.verEquipo()

c.agregarDt1("12-4", "Emiliano Astorga", 60, "Ex-Jugador", 70)
c.verEquipo()

d = Equipo("Eq-002", "Colo-Colo", 17)
d.agregarDt2(b)
d.verEquipo()


## Prueba con un equipo propio

e1 = Equipo("Eq-008", "Deportes Iquique", 10)

e1.verEquipo() ## Se imprime el equipo sin Dt ni jugadores

## Se crean los objetos Dt y Jugador para agregarlos al equipo
dt1 = Dt("15-8", "Brayan Calderon", 45, "Ingeniero", 80)
j1 = Jugador("7-9", "Pablo Parra", 25, "Delantero", 10, 5)

## Se usan los metodos para agregar un dt en parametros y otro con el objeto
e1.agregarDt1("19-7", "Nicolas Larcamon", 55, "Abogado", 65)
e1.agregarDt2(dt1)

e1.verEquipo() ## Se imprime el equipo con los Dt pero sin jugadores

## Se usan los metodos para agregar un jugador en parametros y otro con el objeto
e1.agregarJugador1("13-1", "Juan Lopez", 21, "Defensa", 5, 1)
e1.agregarJugador2(j1)

e1.verEquipo() ## Se imprime el equipo con Dt y jugadores
