# 1. Inicialización
frontend = {'HTML', 'CSS', 'JavaScript', 'React'}
backend = {'Python', 'SQL', 'JavaScript', 'Django'}

# 2. Actualización de equipos
frontend.add('Vue.js')     # Se añade Vue.js al equipo Frontend
backend.discard('Django')  # Se elimina Django del equipo Backend

# 3. Análisis de habilidades
# a) Unión de ambos equipos (todas las habilidades únicas)
habilidades_totales = frontend | backend

# b) Intersección (habilidades en común)
habilidades_comunes = frontend & backend

# c) Diferencia (habilidades exclusivas de Frontend)
habilidades_frontend_exclusivas = frontend - backend

# Mostrar resultados
print("Habilidades únicas en la empresa:", habilidades_totales)
print("Habilidades en común:", habilidades_comunes)
print("Habilidades exclusivas de Frontend:", habilidades_frontend_exclusivas)
