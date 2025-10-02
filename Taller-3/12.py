#12. Tarea: Tienes una lista de tuplas que representan las ventas de una tienda. Cada tupla contiene
#el nombre del producto, su categoría y el monto de la venta. Tu objetivo es calcular el total de ventas
#para cada categoría y almacenarlo en un diccionario.
#("Laptop", "Electrónica", 1500),
#("Camisa", "Ropa", 80),
#("Mouse", "Electrónica", 50),
#("Pantalón", "Ropa", 120),
#("Teclado", "Electrónica", 70)

# Lista de tuplas con las ventas
ventas = [
    ("Laptop", "Electrónica", 1500),
    ("Camisa", "Ropa", 80),
    ("Mouse", "Electrónica", 50),
    ("Pantalón", "Ropa", 120),
    ("Teclado", "Electrónica", 70)
]

# Diccionario para acumular ventas por categoría
totales = {}

# Recorrer las ventas
for producto, categoria, monto in ventas:
    if categoria in totales:
        totales[categoria] += monto
    else:
        totales[categoria] = monto

# Mostrar resultado
print("Total de ventas por categoría:", totales)

