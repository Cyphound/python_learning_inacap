# LEER!!!
# Para ejecutar las 4 funcionalidades pedidas, debe cambiar uno por uno los estados a True y asi ejecutar cada funcionalidad
## Bayron Gómez ##

from pymysql import *
import hashlib as hash
import requests as req
import json

url = "https://jsonplaceholder.typicode.com/posts"
lista  = []
listaEnc = []

response = req.get(url)
datos = response.json()
lista.append(datos)

class jsonBd:
    def __init__(self):
        self.conector = connect(
            host='localhost',
            user='root',
            password='',
            db='act_json')
        self.cursor = self.conector.cursor()
        print("Conectado!!")

    def agregarContenidoJson(self, datos):
        try:
            for obj in datos:
                sql = "INSERT INTO json1 (json1.userId, json1.id, json1.title, json1.body) VALUES ('"+str(obj["userId"])+"', '"+str(obj["id"])+"', '"+obj["title"]+"', '"+obj["body"]+"')"
                self.cursor.execute(sql)
                self.conector.commit()
            print("Datos agregados")
        except Exception as e:
            print("Error al agregar datos", e)

    def agregarContenidoEncriptado(self, datos):
        try:
            for obj in datos:
                enc1 = hash.sha256(str(obj["id"]).encode()).hexdigest() # Se encipta en cada iteracion de los datos
                sql = "INSERT INTO json2 (json2.userId, json2.id, json2.title, json2.body) VALUES ('"+str(obj["userId"])+"', '"+enc1+"', '"+obj["title"]+"', '"+obj["body"]+"')"
                self.cursor.execute(sql)
                self.conector.commit()
            print("Datos agregados")
        except Exception as e:
            print("Error al agregar datos", e)

# Main

jsonABd = False

if jsonABd:
    test = jsonBd()
    test.agregarContenidoJson(datos)

jsonAJson = False

if jsonAJson:
    with open('datos.json','w') as file:
        json.dump(lista,file)
        print("Archivo exportado exitosamente")

jsonEncriptadoABd = False

if jsonEncriptadoABd:
    test2 = jsonBd()
    test2.agregarContenidoEncriptado(datos)
            

jsonEncriptadoAJson = False

if jsonEncriptadoAJson:
    for obj in datos:
        enc1 = hash.sha256(str(obj["id"]).encode()).hexdigest() # Se encipta en cada iteracion de los datos
        dic = { # Se crea un diccionario con el id encriptado
            "userId": obj["userId"],
            "id": enc1,
            "title": obj["title"],
            "body": obj["body"]
        }
        listaEnc.append(dic)

    with open('datosEncriptados.json','w') as file:
        json.dump(listaEnc,file)
        print("Archivo exportado exitosamente")
 