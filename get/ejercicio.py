import requests as req
import json

url = "https://jsonplaceholder.typicode.com/posts"
lista = []

try:
    response = req.get(url)
    datos = response.json()
    lista.append(datos)
    with open('datos.json','w') as file:
        json.dump(lista,file)
        print("Archivo exportado exitosamente")
except Exception as es:
    print("Problemas : " + str(es.args))