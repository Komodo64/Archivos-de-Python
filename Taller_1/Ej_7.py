# Pedimos al usuario dos números enteros
n = int(input("Introduce el primer número (n): "))
m = int(input("Introduce el segundo número (m): "))

# Calculamos cociente y resto
c = n // m
r = n % m

# Mostramos el resultado
print(f"{n} entre {m} da un cociente {c} y un resto {r}")
