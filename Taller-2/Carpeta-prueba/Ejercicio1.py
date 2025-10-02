correos = ["Komodooo64@gmail.com", "Dragon@gmail.com", "Komodooo64@gmail.com",]

# Convertir todo a minúsculas antes de pasarlo al set
correos_no_rep = [e.lower() for e in correos]

emails_unicos = list(set(correos_no_rep))

print(emails_unicos)
