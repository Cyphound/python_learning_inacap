class Persona:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

        def getId(self):
            return self.id
        def getNombre(self):
            return self.nombre
        def getEdad(self):
            return self.edad
        def setId(self, id):
            self.id = id
        def setNombre(self, nombre):
            self.nombre = nombre
        def setEdad(self, edad):
            self.edad = edad
        def __str__(self):
            return "Id: " + str(self.id) + " Nombre: " + self.nombre + " Edad: " + str(self.edad)

p = Persona(1, "Juan", 28)
print(p)