class Colaboraciones:
    def __init__(self):
        # Diccionario: {empleado: {proyectos}}
        self.colaboraciones = {}

    # 1. Agregar un empleado con sus proyectos
    def agregar_empleado(self, empleado, proyectos):
        self.colaboraciones[empleado] = set(proyectos)
        print(f"✅ Empleado {empleado} agregado con proyectos {proyectos}")

    # 2. Encontrar empleados que trabajan en proyectos similares
    def empleados_similares(self, empleado):
        if empleado not in self.colaboraciones:
            return None
        proyectos_empleado = self.colaboraciones[empleado]
        similares = {}
        for otro, proyectos in self.colaboraciones.items():
            if otro != empleado:
                comunes = proyectos_empleado & proyectos
                if comunes:
                    similares[otro] = comunes
        return similares

    # 3. Identificar proyectos en los que NO trabaja un empleado
    def proyectos_no_asignados(self, empleado):
        todos_proyectos = set()
        for proyectos in self.colaboraciones.values():
            todos_proyectos |= proyectos
        return todos_proyectos - self.colaboraciones.get(empleado, set())

    # 4. Formar equipos: empleados que juntos cubran un conjunto de proyectos requeridos
    def formar_equipo(self, proyectos_requeridos):
        proyectos_requeridos = set(proyectos_requeridos)
        empleados = []
        cubiertos = set()
        for empleado, proyectos in self.colaboraciones.items():
            if not proyectos_requeridos - cubiertos:
                break
            if proyectos & proyectos_requeridos:
                empleados.append(empleado)
                cubiertos |= proyectos
        if cubiertos >= proyectos_requeridos:
            return empleados
        return None

    # 5. Calcular el grado de colaboración entre dos empleados (proyectos en común)
    def grado_colaboracion(self, emp1, emp2):
        if emp1 not in self.colaboraciones or emp2 not in self.colaboraciones:
            return 0
        return len(self.colaboraciones[emp1] & self.colaboraciones[emp2])
