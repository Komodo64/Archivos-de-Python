d1 = {
    "Nombre": "Brandon",
    "Edad": 19,
    "Documento": 1016595304,
}
print (d1)

print(d1["Nombre"])
print(d1.get("Nombre"))

#cambiar nombre
d1["Nombre"] = "Komodo"
print(d1)

#añadir direccion
d1["Direccion"] = "Carrera 119a"
print(d1)

#iterar, imprime los key del diccionario
for x in d1:
    print(x)

#imprime los value del diccionario
for x in d1:
    print(d1[x])

#imprime los keys y value del diccionario
for x, y in d1.items():
    print(x, y)    

#Diccionarios anidados

anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}
d = {
    "anidado1" : anidado1,
    "anidado2" : anidado2
}   
print(d)

#clear() borrar lista
d = {"a": 1, "b": 2}
d.clear()
print(d)

#metodo get
d = {"a": 1, "b": 2}
print(d.get("a"))
print(d.get("z","No encontrado"))

#metodo items
d = {"a": 1, "b": 2}
it = d.items()
print(it)
print(list(it))
print(list(it)[0][0])

#metodo key()
d = {"a": 1, "b": 2}
k = d.keys()
print(k)
print(list(k))

#metodo values()
d = {"a": 1, "b": 2}
print(list(d.values()))

#metodo pop
d = {"a":1, "b": 2}
d.pop("a")
print(d)

d = {"a":1, "b": 2}
d.pop("c", -1)
print(d)

#metodo popitem()
d = {"a":1, "b":2}
d.popitem()
print(d)

#metodo update
d1 = {"a":1, "b":2}
d2 = {"a":0, "d":400}
d1.update(d2)
print(d1)
