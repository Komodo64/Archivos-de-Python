# Pedimos al usuario cuántas palabras quiere ingresar
n = int(input("¿Cuántas palabras quieres guardar en la lista? "))

# Creamos la lista vacía
palabras = []

# Solicitamos las palabras
for i in range(n):
    palabra = input(f"Introduce la palabra {i+1}: ")
    palabras.append(palabra)

# Mostramos la lista inicial
print("La lista original es:", palabras)

# Pedimos las palabras para reemplazar
antigua = input("Introduce la palabra que quieres sustituir: ")
nueva = input("Introduce la palabra por la que la quieres reemplazar: ")

# Sustituimos todas las ocurrencias
for i in range(len(palabras)):
    if palabras[i] == antigua:
        palabras[i] = nueva

# Mostramos la lista resultante
print("La lista modificada es:", palabras)
