class VehiculoCarga:
    def __init__(self, patente, cargaMax): #<<Constructor>>
        self.patente = patente
        self.carga = 0
        self.cargaMax = cargaMax
        self.kilometraje = 0
        self.estado = True
        self.__velMax = 250 # Atributo Privado

    def verVehiculo1(self):
        print("Patente:", self.patente)
        print("Carga:", self.carga)
        print("Carga Maxima:", self.cargaMax)
        print("Kilometraje:", self.kilometraje)
        print("Estado:", self.estado, "\n")

    def verVehiculo2(self):
        return "Patente: " + self.patente + "\nCarga: " + str(self.carga) + "\nCarga Maxima: " + str(self.cargaMax) + "\nKilometraje: " + str(self.kilometraje) + "\nEstado: " + str(self.estado) + "\n"
    
    # Implementar un metodo que permita imprimir los datos del vehiculo, pero en el estado, en caso de que el estado sea
    # True, debe imprimir "Disponible", en caso contrario debe imprimir "Ocupado"

    def verVehiculo3(self):
        if self.estado:
            estado = "Disponible"
        else:
            estado = "Ocupado"

        print("Patente:", self.patente)
        print("Carga:", self.carga)
        print("Carga Maxima:", self.cargaMax)
        print("Kilometraje:", self.kilometraje)
        print("Estado:", estado, "\n")
        
        
# Main

vh1 = VehiculoCarga("GKBN-34", 3000) # Creacion de Objeto
vh2 = VehiculoCarga("TRRT-78", 8000) # Invocacion del Constructor

vh1.verVehiculo1()
vh2.verVehiculo1()

print(vh2.verVehiculo2())

vh1.verVehiculo3()
vh2.verVehiculo3()

print(vh1.patente) # No es buena practica
# print(vh1.__velMax) # No es posible acceder a un atributo privado