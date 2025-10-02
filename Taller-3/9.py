#9. Tarea: Crea un diccionario donde las claves sean nombres de estudiantes y los valores sean listas
# de sus notas. Añade una nueva nota a la lista de un estudiante existente.

# Diccionario con estudiantes y sus notas
estudiantes = {
    "Ana": [8.5, 9.0, 7.5],
    "Luis": [6.0, 7.0, 8.0],
    "Marta": [9.5, 9.0, 8.5]
}

# Mostrar notas actuales
print("Notas actuales:", estudiantes)

# Pedir estudiante y nueva nota
nombre = input("Digite el nombre del estudiante: ")
nueva_nota = float(input("Digite la nueva nota: "))

# Añadir la nueva nota si el estudiante existe
if nombre in estudiantes:
    estudiantes[nombre].append(nueva_nota)
    print(f"✅ Nota añadida a {nombre}")
else:
    print("❌ El estudiante no existe en el diccionario.")

# Mostrar resultado final
print("Notas actualizadas:", estudiantes)
