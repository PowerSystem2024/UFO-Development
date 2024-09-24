# **TIPO SET**
# El Set pertenece al grupo de las colecciones, al igual que las listas y las tuplas.
# Set = No tiene un orden, no se pueden modificar sus elementos, pero se pueden agregar o eliminar.
# No tiene índice, es decir, no se puede acceder por posiciones como las listas o tuplas.

# Creamos un Set con nombres de planetas
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

# Usamos la función len para obtener la longitud del set
print(len(planetas))  # Salida: 3

# Revisamos si un elemento existe dentro del set (se debe respetar mayúsculas y acentos)
print("Marte" in planetas)  # Salida: True
print("marte" in planetas)  # Salida: False (distingue entre mayúsculas y minúsculas)

# También podemos verificar si un elemento NO está en el set
print("Mercurio" not in planetas)  # Salida: True

# Agregar un elemento al set, los duplicados no se permiten
planetas.add("Tierra")
planetas.add("Tierra")  # Intentar agregar duplicados no genera error, pero no se agregan
print(planetas)  # Salida: {'Marte', 'Jupiter', 'Venus', 'Tierra'}

# Eliminar elementos de un set
planetas.remove("Tierra")  # Si el elemento no existe, genera un error
# planetas.remove("venus")  # Esto genera un error ya que "venus" no existe (es "Venus")

# Para eliminar sin error, podemos usar discard
planetas.discard("Jupiter")  # Si el elemento no está, no genera error
print(planetas)  # Salida: {'Marte', 'Venus'}

# Limpiamos el set, es decir, lo vaciamos
planetas.clear()
print(planetas)  # Salida: set() (un set vacío)

# Eliminar el set completamente
del planetas
# print(planetas)  # Esto generaría un error porque el set ya no existe

# **DICCIONARIOS**
# Al igual que los sets, los diccionarios no tienen un orden fijo.
# Un diccionario está compuesto por pares de clave-valor (key-value), donde cada clave es única.

# Definimos un diccionario con términos de programación
diccionario = {
    "IDE": "Integrated Development Environment",
    "POO": "Programación Orientada a Objetos",
    "SABD": "Sistema de Administración de Base de Datos"
}
print(diccionario)

# Obtenemos la longitud del diccionario
print(len(diccionario))  # Salida: 3

# Acceder a un valor usando la clave
print(diccionario["IDE"])  # Salida: Integrated Development Environment

# Otra forma de recuperar un valor es usando el método get
print(diccionario.get("POO"))  # Salida: Programación Orientada a Objetos

# Modificar un valor dentro del diccionario
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)  # Salida actualizada: {'IDE': 'Entorno de Desarrollo Integrado', ...}

# Recorrer los elementos (sólo imprime las claves)
for i in diccionario:
    print(i)

# Recorrer el diccionario mostrando clave y valor
for i, j in diccionario.items():
    print(i, j)

# Acceder solo a las claves
for i in diccionario.keys():
    print(i)

# Acceder solo a los valores
for j in diccionario.values():
    print(j)

# Verificar si una clave existe en el diccionario
print("IDE" in diccionario)  # Salida: True

# Agregar un nuevo elemento al diccionario
diccionario["PK"] = "Primary Key"
print(diccionario)  # Salida actualizada con PK

# Eliminar un elemento del diccionario usando la clave
diccionario.pop("SABD")
print(diccionario)  # Salida sin SABD

# Vaciar el diccionario
diccionario.clear()
print(diccionario)  # Salida: {}

# Eliminar el diccionario completamente
del diccionario
# print(diccionario)  # Esto generaría un error porque el diccionario ya no existe
