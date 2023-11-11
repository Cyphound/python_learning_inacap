
class VehiculoCarga:
    def __init__(self, patente, cargaMax): #<<Constructor>>
        self.__patente = patente
        self.__carga = 0
        self.__cargaMax = cargaMax
        self.__kilometraje = 0
        self.__estado = True

    def verVehiculo1(self):
        print("Patente:", self.__patente)
        print("Carga:", self.__carga)
        print("Carga Maxima:", self.__cargaMax)
        print("Kilometraje:", self.__kilometraje)
        print("Estado:", self.getEstado(), "\n")

    def verVehiculo2(self):
        return "Patente: " + self.__patente + "\nCarga: " + str(self.__carga) + "\nCarga Maxima: " + str(self.__cargaMax) + "\nKilometraje: " + str(self.__kilometraje) + "\nEstado: " + str(self.__estado) + "\n"
        
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

    # Capa logicas de negocio <<Business Logic Layer>> (BLL)
    # Carga del vehiculo, no puede superar la carga maxima
    # Si la carga supera la carga maxima, se debe imprimir un mensaje de error y no se debe cargar el vehiculo

    def cargarVehiculo(self, carga):

        if self.__carga + carga > self.__cargaMax:
            return "No se puede cargar el vehiculo, la carga supera la carga maxima, la carga restante es de "+str(self.__cargaMax - self.__carga)+" kg."
        else: 
            self.__carga += carga
            return "Vehiculo cargado con "+str(carga)+" kg de carga"
        
    # Implementar el metodo descargarVehiculo, que permita descargar el vehiculo
    # cuidando que la carga del vehiculo no sea menor a 0

    def descargarVehiculo(self, descarga):
            
            if self.__carga - descarga <= 0:
                return "No se puede descargar el vehiculo, la carga es menor a 0, la carga restante es de "+str(self.__carga)+" kg."
            else: 
                self.__carga -= descarga
                return "Vehiculo descargado con "+str(descarga)+" kg de carga"

# Main

vh1 = VehiculoCarga("GKBN-34", 3000) # Creacion de Objeto
vh2 = VehiculoCarga("TRRT-78", 8000) # Invocacion del Constructor

vh1.verVehiculo1()
vh2.verVehiculo1()

print(vh2.verVehiculo2())

print(vh1.getEstado())

vh2.setKilometraje(1000)
vh2.verVehiculo1()

print(vh1.cargarVehiculo(1000))
vh1.verVehiculo1()
print(vh1.cargarVehiculo(1500))
vh1.verVehiculo1()

print(vh1.cargarVehiculo(2000))
vh1.verVehiculo1()

print(vh1.descargarVehiculo(500))
vh1.verVehiculo1()

print(vh1.descargarVehiculo(5000))
vh1.verVehiculo1()