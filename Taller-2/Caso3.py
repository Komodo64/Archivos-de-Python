# Datos iniciales
tareas = ["Enviar reporte", "Revisar correos"]

# 1. Añadir nueva tarea
nueva_tarea = "Llamar al cliente"
tareas.append(nueva_tarea)  # usamos append para agregar al final de la lista

# 2. Mostrar lista actualizada
print("Lista actualizada de tareas:", tareas)

# 3. Marcar la primera tarea como completada
tareas[0] = tareas[0] + " (Completada)"  # modificamos el primer elemento

# 4. Mostrar lista final
print("Lista final de tareas:", tareas)
