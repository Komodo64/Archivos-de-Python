# Pedimos al usuario cuántas palabras quiere ingresar
n = int(input("¿Cuántas palabras quieres guardar en la lista? "))

# Creamos la lista vacía
palabras = []

# Solicitamos las palabras
for i in range(n):
    palabra = input(f"Introduce la palabra {i+1}: ")
    palabras.append(palabra)

# Mostramos la lista
print("La lista de palabras es:", palabras)

# Pedimos una palabra a buscar
buscar = input("Introduce una palabra para saber cuántas veces aparece: ")

# Contamos cuántas veces aparece
cantidad = palabras.count(buscar)

# Mostramos el resultado
print(f"La palabra '{buscar}' aparece {cantidad} veces en la lista.")
