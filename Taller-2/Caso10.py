# Conjunto de correos identificados como SPAM
spam_emails = {"spam1@example.com", "ofertas@mal.com", "dudoso@mail.net"}

# Primer correo entrante
correo_entrante = "usuario.normal@email.com"

if correo_entrante in spam_emails:
    print(f"Alerta de SPAM: {correo_entrante}")
else:
    print(f"Correo seguro: {correo_entrante}")

# Segundo correo entrante
correo_entrante = "ofertas@mal.com"

if correo_entrante in spam_emails:
    print(f"Alerta de SPAM: {correo_entrante}")
else:
    print(f"Correo seguro: {correo_entrante}")

# Registro (log) de verificaciones
log_verificaciones = ["usuario.normal@email.com", "ofertas@mal.com"]

print("\nLog de correos verificados:")
print(log_verificaciones)
