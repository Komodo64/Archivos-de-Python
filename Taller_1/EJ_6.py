# Pedimos el peso en kilogramos
peso = float(input("Introduce tu peso en kg: "))

# Pedimos la estatura en metros
estatura = float(input("Introduce tu estatura en metros: "))

# Calculamos el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Mostramos el resultado redondeado a 2 decimales
print(f"Tu índice de masa corporal es {imc:.2f}")

