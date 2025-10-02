def invertir_palabra(palabra):
    pila =[]

    #push:añadir cada letra
    for letra in palabra:
        pila.append(letra)

#pop:extraer en orden inverso
invertida = ""
while pila:
    invertida += pila.pop()

return invertida

print(invertir_palabra("Python"))#nohtyP        