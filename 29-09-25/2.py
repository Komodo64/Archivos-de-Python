from queue import PriorityQueue

cola = PriorityQueue()

# cada elemento es una tupla: (prioridad, valor)
cola.put((1, "Paciente grave"))
cola.put((3, "Paciente leve"))
cola.put((2, "Paciente medio"))

# Desencolar respeta las prioridades, no el orden de llegada
print("Atendido: ", cola.get())
print("Atendido: ", cola.get())
print("Atendido: ", cola.get()) #( )

