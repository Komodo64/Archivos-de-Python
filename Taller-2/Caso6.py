# Datos iniciales
tallas_disponibles = ["S", "M", "L", "M"]

# 1. Crear conjunto sin duplicados
tallas_unicas = set(tallas_disponibles)

# 2. Nueva talla que llegó
nueva_talla = "XL"
tallas_unicas.add(nueva_talla)

# 3. Llegó más stock de talla "S"
tallas_unicas.add("S")  # no pasa nada porque ya existe en el set

# 4. Mostrar conjunto final
print("Tallas únicas disponibles:", tallas_unicas)
