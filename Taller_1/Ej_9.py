# Definimos los pesos de cada producto en gramos
peso_payaso = 112
peso_muñeca = 75

# Pedimos al usuario la cantidad de payasos y muñecas vendidos
num_payasos = int(input("Introduce el número de payasos vendidos: "))
num_muñecas = int(input("Introduce el número de muñecas vendidas: "))

# Calculamos el peso total
peso_total = (num_payasos * peso_payaso) + (num_muñecas * peso_muñeca)

# Mostramos el resultado
print(f"El peso total del paquete es: {peso_total} gramos")

