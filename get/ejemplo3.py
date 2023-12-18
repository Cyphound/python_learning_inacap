import json

contenido =[]

for i in range(3):
    persona = {}
    nombre = input("Ingrese nombre : ")
    edad = input("Ingrese edad : ")
    persona ['nombre'] = nombre
    persona ['edad'] = edad
    contenido.append(persona)

print(contenido)
with open('contenido.json','w') as file:
    json.dump(contenido,file)
    print("Archivo exportado exitosamente")