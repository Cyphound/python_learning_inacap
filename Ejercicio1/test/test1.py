
import sys

sys.path.append('/Users/bayro/Desktop/Inacap/Segundo Semestre/POO/python_learning_inacap/Ejercicio1/back/back2')

from modulo2 import *

e1 = Equipo("Eq-008", "Deportes Iquique", 10)

e1.verEquipo()

## Se crean los objetos Dt y Jugador para agregarlos al equipo
dt1 = Dt("15-8", "Brayan Calderon", 45, "Ingeniero", 80)
j1 = Jugador("7-9", "Pablo Parra", 25, "Delantero", 10, 5)

e1.agregarDt2(dt1)

e1.verEquipo() ## Se imprime el equipo con los Dt pero sin jugadores

## Se usan los metodos para agregar un jugador en parametros y otro con el objeto
e1.agregarJugador1("13-1", "Juan Lopez", 21, "Defensa", 5, 1)
e1.agregarJugador2(j1)
e1.agregarJugador1("14-6", "Santiago Araya", 23, "Mediocampista", 12, 7)

e1.verEquipo() ## Se imprime el equipo con Dt y jugadores

e1.eliminarJugador("14-6")

e1.verEquipo()

e1.eliminarDt()

e1.verEquipo()
