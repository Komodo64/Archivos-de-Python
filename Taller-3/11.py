#11. Tarea: Tienes una lista de diccionarios, donde cada diccionario representa a un estudiante. Escribe
#un programa que filtre a los estudiantes que tienen un promedio superior a 4.0 y cree una nueva lista
#que contenga solo los nombres de esos estudiantes
#{"nombre": "Ana", "promedio": 4.5, "curso": "10A"},
#{"nombre": "Luis", "promedio": 3.8, "curso": "10B"},
#{"nombre": "Marta", "promedio": 4.8, "curso": "10A"},
#{"nombre": "Pedro", "promedio": 3.9, "curso": "10C"},
#{"nombre": "Sofía", "promedio": 4.2, "curso": "10B"}

# Lista de diccionarios con los estudiantes
estudiantes = [
    {"nombre": "Ana", "promedio": 4.5, "curso": "10A"},
    {"nombre": "Luis", "promedio": 3.8, "curso": "10B"},
    {"nombre": "Marta", "promedio": 4.8, "curso": "10A"},
    {"nombre": "Pedro", "promedio": 3.9, "curso": "10C"},
    {"nombre": "Sofía", "promedio": 4.2, "curso": "10B"}
]

# Filtrar estudiantes con promedio > 4.0
aprobados = [est["nombre"] for est in estudiantes if est["promedio"] > 4.0]

# Mostrar resultados
print("Estudiantes con promedio mayor a 4.0:", aprobados)
