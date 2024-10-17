# Ejercicio 3: agregar personajes a una lista
# Escribir un programa donde cree una lista con los siguientes personajes de Los Vengadore
# Nombre : Capitan America
# Clase: Soldado
# Raza: Humano

# Nombre: Thor
# Clase: Dios del trueno
# Raza: Asgardiano

# Nombre:Doctor Strange
# Clase: Mago
# Raza: Humano

personajes = []

# Creamos diccionarios para cada personaje y los agregamos a la lista
personajes.append({'Nombre': 'Capitán América', 'Clase': 'Soldado', 'Raza': 'Humano'})
personajes.append({'Nombre': 'Thor', 'Clase': 'Dios del Trueno', 'Raza': 'Asgardiano'})
personajes.append({'Nombre': 'Doctor Strange', 'Clase': 'Mago', 'Raza': 'Humano'})

# Mostramos la lista de personajes
for personaje in personajes:
    print(f"Nombre: {personaje['Nombre']}, Clase: {personaje['Clase']}, Raza: {personaje['Raza']}")