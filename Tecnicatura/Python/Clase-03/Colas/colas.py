#Colas con listas
#Estructura de datos de tipo "fifo" (first input / first output)

cola = ["Leandro", "Agustin", "Ines", "Amanda"]

#Agregamos elementos al final
cola.append("Andrea")
cola.append("Olga")
print(cola)

#Sacamos elementos de la cola
seRetira = cola.pop(0) #En este caso sacamos al primero de la "cola" simulando que ya lo antendieron
print(f"Antendido el cliente/a: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Antendido el cliente/a: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Antendido el cliente/a: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Antendido el cliente/a: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Antendido el cliente/a: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Antendido el cliente/a: {seRetira}")
print(cola)

print('se puede recorrer la lista con algun bucle ')

personas = ['Leandro', 'Ivan', 'Alan', 'Mauro', 'Dario', 'Oscar', 'Sandra']

print('')
print('Atención a pacientes de una clínica.')
print('')
print('Los pacientes son: Leandro, Ivan, alan, Mauro, Dario, Oscar, Sandra ')

while personas:
    persona = personas.pop(0)
    print(f'el Paciente {persona} ha sido atendido')

print('No quedan más pacientes por atender.')


# En Python, cualquier objeto puede evaluarse en un contexto de verdadero (True) o falso (False). Para listas, se consideran True cuando tienen elementos y False cuando están vacías.

# Al escribir while personas:, estás diciéndole a Python que siga ejecutando el bucle mientras personas sea True, es decir, mientras contenga elementos. Cuando personas esté vacía, se evaluará como False, y el bucle se detendrá.

# Aquí tienes una explicación paso a paso:

# Lista con elementos: Al inicio, personas tiene varios elementos (["Ana", "Juan", "Luis", "Maria", "Carlos"]). Esto se evalúa como True, por lo que el bucle while se ejecuta.

# Remoción de elementos: Con cada iteración del bucle, el método pop(0) elimina el primer elemento de la lista, reduciendo su tamaño.

# Lista vacía: Cuando todos los elementos han sido eliminados, personas se convierte en una lista vacía ([]), que se evalúa como False. En ese momento, el bucle while termina.

# Este comportamiento es muy útil, ya que te permite usar estructuras como listas, cadenas o diccionarios en condiciones sin tener que verificar manualmente si están vacíos o no.