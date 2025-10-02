class SistemaCursos:
    def __init__(self):
        # Diccionario: {curso: [lista de prerrequisitos]}
        self.cursos = {}

    # 1. Agregar un curso con sus prerrequisitos
    def agregar_curso(self, curso, prerrequisitos=None):
        if prerrequisitos is None:
            prerrequisitos = []
        self.cursos[curso] = prerrequisitos
        print(f"✅ Curso '{curso}' agregado con prerrequisitos {prerrequisitos}")

    # 2. Listar prerrequisitos directos de un curso
    def listar_prerrequisitos(self, curso):
        return self.cursos.get(curso, [])

    # 3. Encontrar cursos que no tienen prerrequisitos (cursos iniciales)
    def cursos_iniciales(self):
        return [curso for curso, prereqs in self.cursos.items() if not prereqs]

    # 4. Verificar si un estudiante puede tomar un curso
    def puede_tomar(self, curso, completados):
        prereqs = self.cursos.get(curso, [])
        return all(p in completados for p in prereqs)

    # 5. Sugerir qué cursos puede tomar un estudiante según completados
    def sugerir_cursos(self, completados):
        sugerencias = []
        for curso, prereqs in self.cursos.items():
            if curso not in completados and all(p in completados for p in prereqs):
                sugerencias.append(curso)
        return sugerencias
