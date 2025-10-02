from collections import deque

class RedSocial:
    def __init__(self):
        # Representamos la red como un grafo: {usuario: [amigos]}
        self.red = {}

    # 1. Crear conexiones (agregar usuarios y enlaces bidireccionales)
    def conectar(self, u1, u2):
        if u1 not in self.red:
            self.red[u1] = []
        if u2 not in self.red:
            self.red[u2] = []
        self.red[u1].append(u2)
        self.red[u2].append(u1)

    # 2. Simular propagación desde un usuario inicial hasta N niveles
    def propagar(self, inicio, niveles):
        if inicio not in self.red:
            return {}

        visitados = set([inicio])
        cola = deque([(inicio, 0)])  # (usuario, nivel)
        propagacion = {0: [inicio]}  # diccionario: nivel -> usuarios

        while cola:
            usuario, nivel = cola.popleft()
            if nivel < niveles:  # solo propagamos hasta el nivel N
                for vecino in self.red[usuario]:
                    if vecino not in visitados:
                        visitados.add(vecino)
                        cola.append((vecino, nivel + 1))
                        if nivel + 1 not in propagacion:
                            propagacion[nivel + 1] = []
                        propagacion[nivel + 1].append(vecino)

        return propagacion

    # 3. Calcular a cuántos usuarios llega la información después de N niveles
    def alcance_total(self, inicio, niveles):
        propagacion = self.propagar(inicio, niveles)
        todos = set()
        for usuarios in propagacion.values():
            todos.update(usuarios)
        return len(todos) - 1  # menos el usuario inicial

    # 4. Encontrar el usuario con mayor alcance (máximo difusor)
    def mayor_alcance(self, niveles):
        max_usuario = None
        max_alcance = -1
        for usuario in self.red:
            alcance = self.alcance_total(usuario, niveles)
            if alcance > max_alcance:
                max_alcance = alcance
                max_usuario = usuario
        return max_usuario, max_alcance
