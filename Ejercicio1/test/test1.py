import sys
sys.path.append("/Users/bayro/Desktop/ejercicio1/back/back2")
from modulo2 import *

e = Equipo("EQ1","Boca Juniors",2)
e.verEquipo()


j = Jugador("14-4","Carlos Tévez",30,"Delantero",11,26)
j.verJugador()

dt = Dt("11-2","Filipo",50,"Ex-jugador",75)
dt.verDt() 

e.agregarDt2(dt)
e.agregarJugador1(j)
e.agregarJugador1(Jugador("14-3","Emiliano Martínez",30,"Arquero",1,30))
e.agregarJugador1(Jugador("11-5","Virgil Van Djyk",30,"Defensa",1,30))
e.verEquipo()
print(e.eliminarJugador("14-3"))
e.verEquipo()