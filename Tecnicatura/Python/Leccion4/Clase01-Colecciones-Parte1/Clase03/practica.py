 # Ejemplo de generación de números aleatorios
import random

# Generar un número aleatorio entre 1 y 10
random_number = random.randint(1, 10)
print(f"Número aleatorio generado: {random_number}")

# Ejemplo de creación de una lista
# Crear una lista de nombres
nombres = []
num_nombres = int(input("¿Cuántos nombres deseas ingresar? "))

for _ in range(num_nombres):
    nombre = input("Ingresa un nombre: ")
    nombres.append(nombre)

print("Lista de nombres:", nombres)

# Ejemplo de creación de un diccionario
# Crear un diccionario de estudiantes con sus calificaciones
calificaciones = {}

num_estudiantes = int(input("¿Cuántos estudiantes deseas ingresar? "))

for _ in range(num_estudiantes):
    nombre = input("Ingresa el nombre del estudiante: ")
    calificacion = float(input("Ingresa la calificación del estudiante: "))
    calificaciones[nombre] = calificacion

print("Diccionario de calificaciones:", calificaciones)
