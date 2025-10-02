#1. Tarea: Crea una lista de compras. Añade "leche" y "pan" al inicio. Luego, añade "huevos" al final.
#Finalmente, elimina "pan" de la lista y muestra la lista final.

# Lista de compras vacía
lista = []

# Añadir "leche" y "pan" al inicio
lista.insert(0, "pan")
lista.insert(0, "leche")

# Añadir "huevos" al final
lista.append("huevos")

# Eliminar "pan"
lista.remove("pan")

# Mostrar la lista final
print(lista)

