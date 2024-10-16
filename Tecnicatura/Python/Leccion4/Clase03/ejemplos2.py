# Ejemplos de uso de diccionarios
# Almacenar información de contacto:
contactos = {
    "Juan": "1234-5678",
    "Ana": "9876-5432",
    "Luis": "5555-5555"
}

# Acceder a un número de contacto
nombre = input("Ingresa el nombre del contacto: ")
if nombre in contactos:
    print(f"Número de {nombre}: {contactos[nombre]}")
else:
    print("Contacto no encontrado.")
