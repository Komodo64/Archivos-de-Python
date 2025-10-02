# Datos iniciales
ingredientes_masa = ["harina", "mantequilla", "agua", "sal"]
ingredientes_relleno = ["queso", "espinaca", "huevo", "sal"]

# 1. Combinar las dos listas
ingredientes_totales = ingredientes_masa + ingredientes_relleno
print("Ingredientes combinados:", ingredientes_totales)

# 2. Eliminar duplicados usando un conjunto
ingredientes_sin_duplicados = set(ingredientes_totales)

# 3. Convertir de nuevo a lista (opcional, si queremos lista en lugar de set)
lista_compras = list(ingredientes_sin_duplicados)

# 4. Mostrar la lista de compras final
print("Lista de compras final:", lista_compras)
