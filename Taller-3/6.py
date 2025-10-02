#6. Tarea: Utiliza una tupla de tuplas para almacenar un horario simple donde cada tupla interna
#contenga la materia y la hora. Recorre el horario e imprime cada clase en un formato legible.

# Tupla de tuplas con el horario (materia, hora)
horario = (
    ("Matemáticas", "08:00"),
    ("Historia", "10:00"),
    ("Inglés", "12:00"),
    ("Programación", "14:00"),
    ("Educación Física", "16:00")
)

# Recorrer e imprimir el horario en formato legible
print("📅 Horario de clases:")
for materia, hora in horario:
    print(f"- {materia} a las {hora}")
