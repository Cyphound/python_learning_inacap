#print("Hola Mundo 1")

def saludar1():
    print("Hola Mundo 2")

def saludar2(msg):
    print(msg)

def saludar3():
    return "Hola Mundo 3"

def divisiones(numero):
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)

def divisiones2(numero):
    lista = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            lista.append(i)

    return lista

class Persona:
    def __init__(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def getRut(self):
        return self.rut

    def setNombre(self, nombre):
        self.nombre = nombre

    def setRut(self, rut):
        self.rut = rut

    def verPersona(self):
        print("Nombre : ",self.nombre)
        print("Rut    : ",self.rut)

    def __str__(self) -> str:
        return "Nombre : "+self.nombre+"\nRut    : "+self.rut+"\n"
