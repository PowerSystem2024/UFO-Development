# Ejercicio 2: Operaciones de conjuto con listas
# Escriba un programa que tenga 2 lista y que a continuacion 
# cree las siguiente lista (en las que no debes haber repeticion)
# 1 lista de palabras que aparecen en las listas
# 2 lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

lista1 = [1, 2, 3, 4, 3, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 7, 8]

# Eliminar los elementos repetidos de ambas listas con conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Operaciones de conjuntos
union = list(conjunto1 | conjunto2)  # Unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2)  # Solo muestra el conjunto1
solo2 = list(conjunto2 - conjunto1)  # Solo muestra el conjunto2
interseccion = list(conjunto1 & conjunto2)  # Mostramos ambos conjuntos comunes

# Mostramos los resultados
print(f"Lista de números que aparecen en ambas listas (unión): {union}")
print(f"Números que aparecen solo en la primera lista: {solo1}")
print(f"Números que aparecen solo en la segunda lista: {solo2}")
print(f"Números que aparecen en ambas listas (intersección): {interseccion}")