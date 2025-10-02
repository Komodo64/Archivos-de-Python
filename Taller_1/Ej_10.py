# Pedimos al usuario la cantidad inicial depositada
deposito = float(input("Introduce la cantidad depositada en la cuenta de ahorros: "))

# Definimos el interés anual
interes = 0.04

# Calculamos el saldo tras cada año con interés compuesto
año1 = deposito * (1 + interes)
año2 = año1 * (1 + interes)
año3 = año2 * (1 + interes)

# Mostramos los resultados redondeados a 2 decimales
print(f"Saldo tras el primer año: {año1:.2f}")
print(f"Saldo tras el segundo año: {año2:.2f}")
print(f"Saldo tras el tercer año: {año3:.2f}")
