class VehiculoCarga:
    def __init__(self, patente, cargaMax, capacidadEstanque, rendimiento):  # <<Constructor>>
        self.__patente = patente
        self.__carga = 0
        self.__cargaMax = cargaMax
        self.__kilometraje = 0
        self.__estado = True
        self.__capacidadEstanque = capacidadEstanque
        self.__nivelBencina = 10
        self.__rendimiento = rendimiento

    def verVehiculo1(self):
        print("Patente:           ", self.__patente)
        print("Carga:             ", self.__carga)
        print("Carga Maxima:      ", self.__cargaMax)
        print("Kilometraje:       ", self.__kilometraje)
        print("Estado:            ", self.getEstado())
        print("Capacidad Estanque:", self.__capacidadEstanque)
        print("Nivel Bencina:     ", self.__nivelBencina)
        print("Rendimiento:       ", self.__rendimiento, "\n")

    def verVehiculo2(self):
        return "Patente: " + self.__patente + "\nCarga: " + str(self.__carga) + "\nCarga Maxima: " + str(
            self.__cargaMax) + "\nKilometraje: " + str(self.__kilometraje) + "\nEstado: " + str(
            self.__estado) + "\n" + "Capacidad Estanque: " + str(self.__capacidadEstanque) + "\nNivel Bencina: " + str(
            self.__nivelBencina) + "\nRendimiento: " + str(self.__rendimiento) + "\n"
    # Getters

    def getPatente(self):
        return self.__patente

    def getCarga(self):
        return self.__carga

    def getCargaMax(self):
        return self.__cargaMax

    def getKilometraje(self):
        return self.__kilometraje

    def isEstado(self):
        return self.__estado

    def getEstado(self):
        if self.__estado:
            return "Disponible"
        else:
            return "Ocupado"

    def getCapacidadEstanque(self):
        return self.__capacidadEstanque

    def getNivelBencina(self):
        return self.__nivelBencina

    def getRendimiento(self):
        return self.__rendimiento

    # Setters

    def setPatente(self, nuevaPatente):
        self.__patente = nuevaPatente

    def setCarga(self, nuevaCarga):
        self.__carga = nuevaCarga

    def setCargaMax(self, nuevaCargaMax):
        self.__cargaMax = nuevaCargaMax

    def setKilometraje(self, nuevoKilometraje):
        self.__kilometraje = nuevoKilometraje

    def setEstado(self, nuevoEstado):
        self.__estado = nuevoEstado

    def setCapacidadEstanque(self, nuevaCapacidadEstanque):
        self.__capacidadEstanque = nuevaCapacidadEstanque

    def setNivelBencina(self, nuevoNivelBencina):
        self.__nivelBencina = nuevoNivelBencina

    def setRendimiento(self, nuevoRendimiento):
        self.__rendimiento = nuevoRendimiento

    # Capa logicas de negocio <<Business Logic Layer>> (BLL)
    # Carga del vehiculo, no puede superar la carga maxima
    # Si la carga supera la carga maxima, se debe imprimir un mensaje de error y no se debe cargar el vehiculo

    def cargarVehiculo(self, carga):

        if self.__carga + carga > self.__cargaMax:
            return "No se puede cargar el vehiculo, la carga supera la carga maxima, la carga restante es de " + str(
                self.__cargaMax - self.__carga) + " kg."
        else:
            self.__carga += carga
            return "Vehiculo cargado con " + str(carga) + " kg de carga"

    # Implementar el metodo descargarVehiculo, que permita descargar el vehiculo
    # cuidando que la carga del vehiculo no sea menor a 0

    def descargarVehiculo(self, descarga):

        if self.__carga - descarga <= 0:
            return "No se puede descargar el vehiculo, la carga es menor a 0, la carga restante es de " + str(
                self.__carga) + " kg."
        else:
            self.__carga -= descarga
            return "Vehiculo descargado con " + str(descarga) + " kg de carga"

    # Metodo para iniciar el viaje

    def iniciarViaje(self):
        if self.__nivelBencina >= self.__capacidadEstanque * 0.6:
            if self.__carga == self.__cargaMax:
                if self.__estado:
                    self.__estado = False
                    mensaje = "Viaje iniciado"
                else:
                    mensaje = "El vehiculo ya se encuentra en viaje"
            else:
                mensaje = "El vehiculo no se encuentra cargado"
        else:
            mensaje = "El vehiculo no tiene bencina suficiente"

        print(mensaje)

    # Metodo para verificar si se puede realizar el viaje

    def verificarViaje(self, kilometros):
        if self.__rendimiento * self.__nivelBencina > kilometros:
            return "El viaje se puede realizar"
        else:
            return "El viaje no se puede realizar"

# Main

vh1 = VehiculoCarga("GKBN-34", 3000, 50, 25)  # Creacion de Objeto
vh2 = VehiculoCarga("TRRT-78", 8000, 40, 20)  # Invocacion del Constructor

vh1.verVehiculo1()
vh2.verVehiculo1()

print(vh2.verVehiculo2())

print(vh1.getEstado())

vh2.setKilometraje(1000)
vh2.verVehiculo1()

print(vh2.getRendimiento(), "\n")

vh2.setRendimiento(3)
vh2.verVehiculo1()

vh1.setNivelBencina(30)
vh1.cargarVehiculo(3000)
vh1.iniciarViaje()

print("")

vh1.verVehiculo1()

vh2.iniciarViaje()

print("")

print(vh1.verificarViaje(500))
print(vh1.verificarViaje(20))

print("")

listaVehiculo = [VehiculoCarga("XDLO-25", 7000, 80, 15),
                 VehiculoCarga("UWUA-17", 9400, 90, 12),
                 VehiculoCarga("LAGH-34", 12000, 65, 30)]

for i in range(len(listaVehiculo)):
    listaVehiculo[i].verVehiculo1()
    print("")

diccionarioVehiculo = {
    1: vh1,
    2: vh2,
    3: VehiculoCarga("WDOR-89", 10000, 78, 27)
}

for i in diccionarioVehiculo.values():
    i.verVehiculo1()