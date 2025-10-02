# Pedimos al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Calculamos la suma usando la fórmula
suma = n * (n + 1) // 2   # usamos // para obtener entero

# Mostramos el resultado
print(f"La suma de los {n} primeros enteros positivos es: {suma}")
