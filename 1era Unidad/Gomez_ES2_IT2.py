
class Persona:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

    def mostrarDatos(self):
        print(
            "ID:    ", self.id, "\n"+
            "Nombre:", self.nombre, "\n"+
            "Edad:  ", self.edad, "\n"
        )

    # Getters

    def getID(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    # Setters

    def setID(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

# Clase Alumno

class Alumno(Persona):

    def __init__(self, id, nombre, edad, asistencia):
        super().__init__(id, nombre, edad)
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.asistencia = asistencia
        self.notas = {}
        self.promedio = 0.0
        self.situacion = False

    def mostrarDatos(self):
        print(
            "ID:        ", self.id, "\n"+
            "Nombre:    ", self.nombre, "\n"+
            "Edad:      ", self.edad, "\n"+
            "Asistencia:", self.asistencia, "\n"+
            "Notas:     ", self.notas, "\n"+
            "Promedio:  ", self.promedio, "\n"+
            "Situacion: ", self.defiSituacion(), "\n"
        )

    # Getters

    def getID(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getAsistencia(self):
        return self.asistencia

    def getNotas(self):
        return self.notas

    def getPromedio(self):
        return self.promedio

    def getSituacion(self):
        return self.situacion

    def defiSituacion(self):
        if self.situacion:
            return "Aprobado"
        else:
            return "Reprobado"

    # Setters

    def setID(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setAsistencia(self, asistencia):
        self.asistencia = asistencia

    def setNotas(self, notas):
        self.notas = notas

    def setPromedio(self, promedio):
        self.promedio = promedio

    def setSituacion(self, situacion):
        self.situacion = situacion

    # Capa de Negocio

    def agregarNota(self, numeroNota1, Nota1, numeroNota2, Nota2, numeroNota3, Nota3, numeroNota4, Nota4):
        if len(self.notas) >= 4:
            print("Error, ya hay 4 notas en el alumno")
        else:
            self.notas = {numeroNota1: Nota1, numeroNota2: Nota2, numeroNota3: Nota3, numeroNota4: Nota4}
            print("Notas Agregadas")

    def calcularPromedio(self):
        suma = 0

        for i in range(1, len(self.notas)+1):
            suma += self.notas[i]

        promedio = suma / len(self.notas)

        self.promedio = promedio

        return self.promedio

    def asignarSituacion(self):
        if self.calcularPromedio() == 0:
            print("El promedio no existe")
        elif self.calcularPromedio() >= 7:
            print("El promedio excede el limite")
        else:
            if self.calcularPromedio() >= 4.0:
                self.situacion = True
            else:
                self.situacion = False

    def calcularNotaMaximaMinima(self):

        notaMaxima = 0
        notaMinima = 9999

        for i in range(1, len(self.notas)+1):
            if self.notas[i] > notaMaxima :
                notaMaxima = self.notas[i]

            if self.notas[i] < notaMinima :
                notaMinima = self.notas[i]

        return "Nota Maxima:", notaMaxima, "Nota Minima", notaMinima

# Administrativo

class Administrativo(Persona):
    def __init__(self, id, nombre, edad, cargo):
        super().__init__(id, nombre, edad)
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.sueldo = []

    def mostrarDatos(self):
        print(
            "ID:    ", self.id, "\n"+
            "Nombre:", self.nombre, "\n"+
            "Edad:  ", self.edad, "\n"+
            "Cargo: ", self.cargo, "\n"+
            "Sueldo:", self.sueldo, "\n"
        )

    # Getters

    def getID(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getCargo(self):
        return self.cargo

    def getSueldo(self):
        return self.sueldo

    # Setters

    def setID(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setCargo(self, cargo):
        self.cargo = cargo

    def setSueldo(self, sueldo):
        self.sueldo = sueldo

    # Capa de Negocio

    def agregarSueldoLiquido(self, sueldoBruto, porDesc):

        calc = sueldoBruto * ((1 - (porDesc / 100)))

        sueldoLiquido = calc + (calc * 0.12)

        self.sueldo.append(sueldoLiquido)

    def calcularSumaSueldos(self, cant):
        suma = 0
        if cant > len(self.sueldo):
            print("La cantidad de sueldos a sumar es mayor a la cantidad de sueldos")
        else:
            for i in range(len(self.sueldo)):
                suma += self.sueldo[i]
            return suma

# Main

alumno1 = Alumno(123, "Pedro", 15, 75)
alumno2 = Alumno(456, "Luis", 16, 50)
alumno3 = Alumno(789, "Juan", 14, 90)

print("Alumno 1"+"\n")

alumno1.mostrarDatos()

alumno1.agregarNota(1, 4.7, 2, 3.6, 3, 7.0, 4, 5.1)

print("")

alumno1.asignarSituacion()

alumno1.mostrarDatos()

print("Alumno 2"+"\n")

alumno2.mostrarDatos()

alumno2.agregarNota(1, 2.7, 2, 3.4, 3, 5.6, 4, 1.8)

print("")

alumno2.asignarSituacion()

alumno2.mostrarDatos()

print("Alumno 3"+"\n")

alumno3.mostrarDatos()

alumno3.agregarNota(1, 6.6, 2, 6.1, 3, 7.0, 4, 5.8)

print("")

alumno3.asignarSituacion()

alumno3.mostrarDatos()

alumno3.setEdad(19)

alumno3.mostrarDatos()

adm1 = Administrativo(234, "Antonio", 34, "Dev")
adm2 = Administrativo(534, "Alexis", 65, "Profesor")
adm3 = Administrativo(234, "Andres", 25, "Ayudante")

print("Administrador 1:")
print("")

adm1.agregarSueldoLiquido(1000000, 12.3)

adm1.agregarSueldoLiquido(400000, 4.3)

adm1.mostrarDatos()

print(adm1.calcularSumaSueldos(2))

adm1.calcularSumaSueldos(3)

print("Administrador 1:")
print("")

adm1.agregarSueldoLiquido(1000000, 12.3)

adm1.agregarSueldoLiquido(400000, 4.3)

adm1.mostrarDatos()

print(adm1.calcularSumaSueldos(2))

adm1.calcularSumaSueldos(3)

print("Administrador 2:")
print("")

adm2.agregarSueldoLiquido(1500000, 4.7)

adm2.mostrarDatos()

print(adm2.calcularSumaSueldos(1))

print("Administrador 3:")
print("")

adm1.agregarSueldoLiquido(450000, 7.6)

adm1.agregarSueldoLiquido(400000, 4.1)

adm3.agregarSueldoLiquido(500000, 7.9)

adm1.mostrarDatos()

print(adm1.calcularSumaSueldos(3))

# Diccionar Alumnos

dicAlum = {
    1: alumno1,
    2: alumno2,
    3: Alumno(543, "Tiare", 12, 87)
}

dicAlum[3].agregarNota(1, 3.4, 2, 4.2, 3, 5.7, 4, 6.1)

for i in range(1, len(dicAlum)+1):
    dicAlum[i].mostrarDatos()
