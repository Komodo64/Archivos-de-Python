from collection import deque

jugadores = deque(["Carolina", "Darian", "Jefry", "Adrian"])

for i in range(10)
turno = jugadores.popleft()
print("turno de: ", turno)
jugadores.append(turno)

print("Cola final: ", jugadores)
