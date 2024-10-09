# Diccionario: Llave:valor >>> 'Maradona':10
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}
print(diccionario)
print(len(diccionario))

# Un diccionario se parece a un tipo set, no tiene indice, entonces para acceder a un elemento lo hacemos utilizando llaves.
# Accedemos a un diccionario con la llave (key) por ej.. una key es POO, otra es IDE, otra es SABD
# hay que tener cuidado al escribir las llaves, no cometer errores en mayusculas, minusculas o en la palabra.

# Acceder a un elemento
print(diccionario['IDE'])

# Otra forma de recuperar un elemento:
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificar los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)
# COMO VEMOS, UN DICCIONARIO PUEDE MODIFICARSE!

# DICCIONARIO PARTE 2
# COMO RECORRER LOS ELEMENTOS
print("-----------------------------------")
for llave in diccionario:           # con el ciclo for solo nos permite acceder a las llaver, no al valor
    print(llave)                    # Para acceder al valor debemos hacer con una función

print("-----------------------------------")

# ACCEDER A LOS ELEMENTOS DE UNA DICCIONARIO CON LA FUNCIÓN items                                    
for llave, valor in diccionario.items():    # de la siguiente manera
    print(llave, valor)
print("-----------------------------------")

# puede ponerse tambien: for llave, valor in diccionario.keys(): ; for llave, valor in diccionario.values():

for llave in diccionario.keys():
    print(llave)

print("-----------------------------------")

# Para comprobar la existencia de algún elemento:
print('IDE' in diccionario) # NOS DEVUELVE UN BOOLEANO

print("-----------------------------------")

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

print("-----------------------------------")

# ELIMINAR UN ELEMENTO
diccionario.pop('SABD') # SE ELIMINA TANTO LA LLAVE COMO SU VALOR
print(diccionario)

print("-----------------------------------")

# VACIAR UN DICCIONARIO
diccionario.clear()
print(diccionario)

print("-----------------------------------")

# Eliminar el diccionario
del diccionario 

