print('Ejercicio 3:')
print('Crear un rango de 3 a 10 pero con incremento')
print('de 2 en 2. Ejemplo de ejecución: 3,5,7,9 ')

# Aclaro que decidí hacer el ejercicio de esta manera
# porque personalmente creo que el ej. del aula no refleja
# el resultado que se espera ya que los valores no aparecen uno
# al lado del otro.

print("Desarrollo")
valores = [] # creo una lista vacia fuera del ciclo for
for i in range(6):
    valores.append(i) # Agrego un elemento al final en cada iteración
valores.append(10) # Si quisiera agregar un valor más al final de la lista lo podría hacer de esta forma
print(valores) # Imprimo los valores

# Error que cometí. En un primer intento cree la lista vacia
# dentro del ciclo for con lo que al imprimir solo me imprima el valor 9 y 10
# porque con cada iteración la lista vacia se volvía a crear
# y al final solo imprimía los valores agregados a la última lista vacia creada!
