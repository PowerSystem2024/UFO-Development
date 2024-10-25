# Ejercicio 1: Verificar si un elemento está en el set
# y agregarlo solo si no está.

# Creamos un set de animales
animales = {"perro", "gato", "conejo"}

# Verificamos si "loro" está en el set y lo agregamos solo si no está
if "loro" not in animales:
    animales.add("loro")

print(animales)  # Salida: {'perro', 'gato', 'conejo', 'loro'}

#Ejercicio 2: Convertir un diccionario en una lista de claves
# y valores por separado.

# Creamos un diccionario de frutas
frutas = {"manzana": 1.2, "banana": 0.8, "naranja": 0.9}

# Obtenemos las claves y los valores por separado
claves = list(frutas.keys())
valores = list(frutas.values())

print(claves)  # Salida: ['manzana', 'banana', 'naranja']
print(valores)  # Salida: [1.2, 0.8, 0.9]

# Ejercicio 3: Fusionar dos sets sin duplicados.

# Creamos dos sets de colores
colores_primarios = {"rojo", "azul", "amarillo"}
colores_secundarios = {"verde", "naranja", "morado", "rojo"}

# Usamos la operación de unión para fusionar ambos sets
colores_fusionados = colores_primarios.union(colores_secundarios)

print(colores_fusionados)  # Salida: {'azul', 'verde', 'naranja', 'amarillo', 'morado', 'rojo'}
