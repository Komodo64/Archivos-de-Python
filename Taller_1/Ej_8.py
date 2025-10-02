# Pedimos al usuario los datos
cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (en %): "))
años = int(input("Introduce el número de años: "))

# Cálculo del capital final con interés compuesto
capital = cantidad * (1 + interes / 100) ** años

# Mostramos el resultado
print(f"El capital obtenido tras {años} años será: {capital:.2f}")
