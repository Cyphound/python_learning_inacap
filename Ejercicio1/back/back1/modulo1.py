
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