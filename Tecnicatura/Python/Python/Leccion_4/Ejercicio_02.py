# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los numeros del 1 al 10, luego modificar los
# elementos de la lista multiplicandolos por los valor ingresado por el usuario
# Ejercicio 2: Modificar los elementos de una lista

numeros = list(range(1, 11))
multiplicador = int(input("Ingrese un número para multiplicar los elementos de la lista: "))
numeros = [num * multiplicador for num in numeros]  # Usamos una comprensión de lista
print("Lista modificada:", numeros)