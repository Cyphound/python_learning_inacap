class Cuenta:
    def __init__(self, nro, saldo, tipo):
        self.__nro = nro
        self.__saldo = saldo
        self.__estado = True
        self.__tipo = tipo

    def verDatos(self):
        print("Numero de Cuenta: ", self.__nro)
        print("Saldo:            ", self.__saldo)
        print("Estado:           ", self.getEstado())
        print("Tipo:             ", self.__tipo, "\n")

    # Getters

    def getNro(self):
        return self.__nro

    def getSaldo(self):
        return self.__saldo

    def isEstado(self):
        return self.__estado

    def getEstado(self):
        if self.__estado:
            return "Habilitada"
        else:
            return "Inhabilitada"

    def getTipo(self):
        return self.__tipo

    # Setters

    def setNro(self, nuevoNro):
        self.__nro = nuevoNro

    def setSaldo(self, nuevoSaldo):
        self.__saldo = nuevoSaldo

    def setEstado(self, nuevoEstado):
        self.__estado = nuevoEstado

    def setTipo(self, nuevoTipo):
        self.__tipo = nuevoTipo


# Main

c1 = Cuenta(123, 100000, "Cuenta Corriente")
c2 = Cuenta(456, 200000, "Cuenta Vista")

c1.verDatos()
c2.verDatos()

c2.setEstado(False)
c2.verDatos()
