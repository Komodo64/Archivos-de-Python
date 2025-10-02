# Grafo para representar estaciones del metro
class Metro:
    def __init__(self):
        self.grafo = {}  # Diccionario {estación: [conexiones]}

    # 1. Agregar nueva estación
    def agregar_estacion(self, estacion):
        if estacion not in self.grafo:
            self.grafo[estacion] = []
            print(f"✅ Estación '{estacion}' agregada.")
        else:
            print(f"⚠️ La estación '{estacion}' ya existe.")

    # 2. Conectar dos estaciones
    def conectar_estaciones(self, est1, est2):
        if est1 not in self.grafo:
            self.agregar_estacion(est1)
        if est2 not in self.grafo:
            self.agregar_estacion(est2)

        if est2 not in self.grafo[est1]:
            self.grafo[est1].append(est2)
        if est1 not in self.grafo[est2]:
            self.grafo[est2].append(est1)

        print(f"🚇 Conexión creada entre '{est1}' y '{est2}'.")

    # 3. Encontrar estaciones conectadas directamente
    def estaciones_conectadas(self, estacion):
        if estacion in self.grafo:
            return self.grafo[estacion]
        else:
            return []

    # 4. Contar total de estaciones
    def contar_estaciones(self):
        return len(self.grafo)

    # 5. Determinar si dos estaciones están conectadas directamente
    def estan_conectadas(self, est1, est2):
        return est2 in self.grafo.get(est1, [])
