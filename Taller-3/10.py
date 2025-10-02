#10. Tarea: Dada una lista de números, crea una nueva lista que contenga únicamente los números
# pares de la lista original, utilizando una lista por comprensión.

# Lista de números (ejemplo)
numeros = [3, 6, 9, 12, 15, 18, 21, 24]

# Nueva lista con solo los números pares
pares = [n for n in numeros if n % 2 == 0]

# Mostrar resultados
print("Lista original:", numeros)
print("Números pares:", pares)
