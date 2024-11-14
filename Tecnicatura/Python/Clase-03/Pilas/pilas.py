#Pilas usando listas
pila = [1, 2, 3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Elimar elementos desde el fina
elementoBorrado =  pila.pop() #Elimina el ultimo elemento y lo guarda en la variable
print(f"Sacamos el elmento {elementoBorrado}")
print(f"La pila que ahora asi: {pila}")

# A las listas en Python a veces se les llama "pilas" porque pueden utilizarse para implementar el comportamiento de una pila o stack en informática, que es una estructura de datos donde los elementos se agregan y eliminan siguiendo el principio LIFO (Last In, First Out), es decir, el último elemento en entrar es el primero en salir.

# En Python, las listas son estructuras de datos flexibles que permiten agregar o eliminar elementos de cualquier posición. Sin embargo, si usamos los métodos:

# append() para agregar elementos al final de la lista.
# pop() sin argumentos para eliminar el último elemento agregado.
# la lista se comporta como una pila, con el último elemento agregado siendo el primero en salir.

# Por lo tanto, aunque técnicamente las listas en Python no son pilas, su versatilidad permite que funcionen como una pila cuando se usan de esta manera.