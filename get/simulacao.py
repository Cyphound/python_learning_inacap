import math, time
from os import system

class Poblacion:
    def __init__(self, poblacion_inicial, tasa_crecimiento):
        self.poblacion = poblacion_inicial
        self.tasa_crecimiento = tasa_crecimiento

    def crecimiento_exponencial(self, tiempo):
        crecimiento = self.poblacion * math.exp(self.tasa_crecimiento * tiempo)
        return crecimiento

    def afectar_crecimiento(self, intensidad_enfermedad, tiempo_enfermedad, poblacion):
        factor_enfermedad = math.exp(-intensidad_enfermedad * tiempo_enfermedad)
        self.poblacion = self.poblacion * factor_enfermedad
        return self.poblacion


poblacion_inicial = 10
tasa_crecimiento = 0.2

intensidad_enfermedad = 0.4
tiempo_enfermedad = 5

tiempo_simulado = 10
poblacion_obj = Poblacion(poblacion_inicial, tasa_crecimiento)
crecimiento_simulado = poblacion_obj.crecimiento_exponencial(1)
j = 1

for i in range(1, tiempo_simulado+1):
  system("cls")
  print(f"Población después de {i} meses (crecimiento exponencial): {round(crecimiento_simulado)}")
  if i == 1: i += 1
  if j < tiempo_enfermedad:
    poblacion_obj.afectar_crecimiento(intensidad_enfermedad, j, crecimiento_simulado)
    print(f"Población afectada por enfermedad: {round(poblacion_obj.poblacion)}, despues de {j} meses")
    j += 1
  crecimiento_simulado = poblacion_obj.crecimiento_exponencial(i)
  time.sleep(1)

