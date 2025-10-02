# Precio habitual de una barra de pan
precio_barra = 4000

# Descuento por no ser del día (60%)
descuento = 0.60

# Pedimos al usuario cuántas barras no son del día se han vendido
barras_no_frescas = int(input("Introduce el número de barras vendidas que no son del día: "))

# Calculamos el precio con descuento
precio_descuento = precio_barra * (1 - descuento)

# Calculamos el coste total
coste_total = barras_no_frescas * precio_descuento

# Mostramos los resultados
print(f"Precio habitual de una barra de pan: ${precio_barra}")
print(f"Descuento por no ser fresca: {descuento * 100}%")
print(f"Coste final total: ${coste_total:.0f}")
