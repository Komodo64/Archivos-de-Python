# Pedimos al usuario cuántas palabras quiere ingresar
n = int(input("¿Cuántas palabras quieres guardar en la lista? "))

# Creamos la lista vacía
palabras = []

# Solicitamos las palabras
for i in range(n):
    palabra = input(f"Introduce la palabra {i+1}: ")
    palabras.append(palabra)

# Creamos una nueva lista invertida (distinta de la original)
palabras_invertidas = palabras[::-1]

# Mostramos ambas listas
print("Lista original:", palabras)
print("Lista invertida:", palabras_invertidas)
