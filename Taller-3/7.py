#7. Tarea: Tienes dos listas de invitados a una fiesta. Combínalas en una sola lista que no contenga
#nombres repetidos.
#invitados_dia = ["Ana", "Luis", "Marta", "Pedro"]
#invitados_noche = ["Luis", "Sofía", "Ana", "Juan"]

# Listas de invitados
invitados_dia = ["Ana", "Luis", "Marta", "Pedro"]
invitados_noche = ["Luis", "Sofía", "Ana", "Juan"]

# Combinar listas sin duplicados usando set
invitados_totales = list(set(invitados_dia + invitados_noche))

# Mostrar lista final
print("Lista de invitados sin repetidos:", invitados_totales)
