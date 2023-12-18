import requests as req

url = "https://jsonplaceholder.typicode.com/posts"

response = req.get(url)
datos = response.json()
print(datos)
print(type(datos))
print(type(response))
print("#"*60)

for obj in datos:
    print(obj["title"])
    print("7u"*30)
    print(obj["body"])
    print("Uw"*30)