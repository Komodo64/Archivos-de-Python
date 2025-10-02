class RedDistribucion:
    def __init__(self):
        # Diccionario de adyacencia con capacidades: {origen: {destino: capacidad}}
        self.red = {}

    # 1. Agregar una ruta con capacidad
    def agregar_ruta(self, origen, destino, capacidad):
        if origen not in self.red:
            self.red[origen] = {}
        self.red[origen][destino] = capacidad
        print(f"✅ Ruta agregada: {origen} -> {destino} con capacidad {capacidad}")

    # 2. Obtener la capacidad de una ruta específica
    def capacidad_ruta(self, origen, destino):
        return self.red.get(origen, {}).get(destino, None)

    # 3. Listar todas las rutas salientes de un centro
    def rutas_salientes(self, origen):
        return list(self.red.get(origen, {}).items())

    # 4. Encontrar el centro con mayor capacidad total de salida
    def centro_mayor_capacidad(self):
        max_centro = None
        max_capacidad = 0
        for origen, destinos in self.red.items():
            total = sum(destinos.values())
            if total > max_capacidad:
                max_capacidad = total
                max_centro = origen
        return max_centro, max_capacidad

    # 5. Calcular la capacidad total de toda la red
    def capacidad_total(self):
        total = 0
        for destinos in self.red.values():
            total += sum(destinos.values())
        return total
