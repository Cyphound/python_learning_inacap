## Bayron Gómez ##

class Ciudad:
    def __init__(self, id, nombre, postal, pais):
        self.__id = id
        self.__nombre = nombre
        self.__postal = postal
        self.__pais = pais

    # Getters
    def getId(self):
        return self.__id
    def getNombre(self):
        return self.__nombre
    def getPostal(self):    
        return self.__postal
    def getPais(self):
        return self.__pais
    
    # Setters
    def setId(self, id):
        self.__id = id
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setPostal(self, postal):
        self.__postal = postal
    def setPais(self, pais):
        self.__pais = pais

    def __str__(self):
        print(" Id : {}, Nombre : {}, Postal : {}".format(self.__id, self.__nombre, self.__postal))

    def verCiudad(self):
        print("    Id               : ",self.__id)
        print("    Nombre           : ",self.__nombre)
        print("    Codigo Postal    : ",self.__postal,"\n")

class Pais:
    def __init__(self, id, nombre, nHabitantes, superficie):
        self.__id = id
        self.__nombre = nombre
        self.__nHabitantes = nHabitantes
        self.__superficie = superficie
        self.__ciudades = []

    # Getters
    def getId(self):
        return self.__id
    def getNombre(self):
        return self.__nombre
    def getNHabitantes(self):
        return self.__nHabitantes
    def getSuperficie(self):
        return self.__superficie
    def getCiudades(self):
        return self.__ciudades
    
    # Setters
    def setId(self, id):
        self.__id = id
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setNHabitantes(self, nHabitantes):
        self.__nHabitantes = nHabitantes
    def setSuperficie(self, superficie):
        self.__superficie = superficie
    def setCiudades(self, ciudades):
        self.__ciudades = ciudades

    def __str__(self):
        print(" Id : {}, Nombre : {}, Nº Habitantes : {}, Superficie : {} {}".format(self.__id, self.__nombre, self.__nHabitantes, self.__superficie, self.mostrarCiudades()))

    def verPais(self):
        print("Id         : ",self.__id)
        print("Nombre     : ",self.__nombre)
        print("Poblacion  : ",self.__nHabitantes)
        print("Superficie : ",self.__superficie)
        if(len(self.__ciudades) == 0):
            print("No hay ciudades aún")
        else:
            print("Ciudades : ")
            for i in range(len(self.__ciudades)):
                self.__ciudades[i].verCiudad()
        print("")
    
    def agregarCiudad(self, ciudad):
        self.__ciudades.append(ciudad)

# Main
estado = False # True para probar las clases     

if estado:
    pais = Pais(1, "Chile", 18000000, 756096)
    ciudad = Ciudad(1, "Santiago", 1, 1)

    pais.agregarCiudad(ciudad)
    pais.verPais()
