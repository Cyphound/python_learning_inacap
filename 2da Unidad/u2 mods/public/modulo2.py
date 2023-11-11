print("Hola desde modulo 2")

def cuentaCaracteres(cadena):
    return "Tu cadena posee " + str(len(cadena)) + " caracteres"


def esPerfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    if suma == numero:
        return "Es perfecto"
    else:
        return "No es perfecto"
