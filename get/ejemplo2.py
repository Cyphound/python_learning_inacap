import requests as req

url = "https://randomuser.me/api?format=docx"

try:
    res = req.get(url)
    if res.status_code == 200:
        print("Codigo de respuesta: " + str(res.status_code))
        print("Contenido : ")
        print(type(res.content))
        print(type(res.text))
        print("Contenido JSON")
        contenidoJson = res.json()
        print(type(contenidoJson))
        
        print(contenidoJson)
        print("#"*50)
        
        for obj in contenidoJson["results"]:
            print(obj["location"]["timezone"]["description"])

except Exception as es:
    print("Problemas : " + str(es.args))