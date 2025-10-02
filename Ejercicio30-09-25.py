# Grafo con ciudades y distancias
grafo = {
    'A': {'B': 5, 'C': 8, 'D': 9},
    'B': {'A': 5, 'E': 15, 'F': 7},
    'C': {'A': 8, 'G': 12, 'H': 10},
    'D': {'A': 9, 'I': 11, 'J': 6},
    'E': {'B': 15, 'K': 9, 'L': 13},
    'F': {'B': 7, 'M': 8, 'N': 6},
    'G': {'C': 12, 'O': 10, 'P': 5},
    'H': {'C': 10, 'Q': 11, 'R': 7},
    'I': {'D': 11, 'S': 14, 'T': 8},
    'J': {'D': 6, 'U': 9, 'V': 12},
    'K': {'E': 9},
    'L': {'E': 13},
    'M': {'F': 8},
    'N': {'F': 6},
    'O': {'G': 10},
    'P': {'G': 5},
    'Q': {'H': 11},
    'R': {'H': 7},
    'S': {'I': 14},
    'T': {'I': 8},
    'U': {'J': 9},
    'V': {'J': 12}
}


# Función para encontrar todas las rutas con DFS
def dfs_todas_rutas(grafo, origen, destino, visitados=None, camino=None, distancia=0):
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []

    camino = camino + [origen]
    if origen == destino:
        return [(camino, distancia)]

    rutas = []
    for vecino, peso in grafo.get(origen, {}).items():
        if vecino not in visitados and vecino not in camino:
            rutas.extend(
                dfs_todas_rutas(grafo, vecino, destino, visitados, camino, distancia + peso)
            )

    return rutas


# Función para encontrar la ruta más corta usando DFS
def ruta_mas_corta(grafo, origen, destino):
    rutas = dfs_todas_rutas(grafo, origen, destino)
    if not rutas:
        return None

    # Seleccionar la ruta con menor distancia
    camino_min, distancia_min = min(rutas, key=lambda x: x[1])
    return "".join(camino_min), distancia_min


# ------------------ PRUEBAS ------------------
print(ruta_mas_corta(grafo, "A", "K"))   # ejemplo: ('ABEK', 29)
print(ruta_mas_corta(grafo, "A", "R"))   # ejemplo: ('ACHR', 25)
print(ruta_mas_corta(grafo, "M", "Q"))   # ('FMC...Q') o None si no hay camino
