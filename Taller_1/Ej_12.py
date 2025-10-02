# Pedimos al usuario cuántas palabras quiere ingresar
n = int(input("¿Cuántas palabras quieres guardar en la lista? "))

# Creamos una lista vacía
palabras = []

# Pedimos las palabras al usuario y las agregamos a la lista
for i in range(n):
    palabra = input(f"Introduce la palabra {i+1}: ")
    palabras.append(palabra)

# Mostramos la lista completa
print("La lista de palabras es:", palabras)
