# Datos iniciales: conjunto de asistentes que ya ingresaron
asistentes_ingresados = {"ID_1122", "ID_3344"}

# 1. Nueva persona llegando
persona_llegando = "ID_5566"

# 2. Verificar si ya ingresó
if persona_llegando in asistentes_ingresados:
    print("La persona con ID", persona_llegando, "ya ingresó anteriormente.")
else:
    asistentes_ingresados.add(persona_llegando)  # se agrega al conjunto
    print("Bienvenido,", persona_llegando)

# 3. Ahora llega la persona ID_1122
persona_llegando = "ID_1122"

if persona_llegando in asistentes_ingresados:
    print("La persona con ID", persona_llegando, "ya había ingresado antes.")
else:
    asistentes_ingresados.add(persona_llegando)
    print("Bienvenido,", persona_llegando)

# 4. Mostrar conjunto final
print("Asistentes registrados al evento:", asistentes_ingresados)
