# Ejemplo de ciclo for
# Solicitar un número por teclado y mostrar los números del 1 al número ingresado
n = int(input("Ingresa un número: "))
for i in range(1, n + 1):
    print(i)


# Ejemplo de ciclo while
# Solicitar un número por teclado y contar hacia atrás hasta 0
n = int(input("Ingresa un número: "))
while n >= 0:
    print(n)
    n -= 1

# Ejemplo de ciclo do while (simulado)
# Simular un ciclo do while para solicitar un número hasta que sea positivo
while True:
    n = int(input("Ingresa un número positivo: "))
    if n > 0:
        break  # Sale del ciclo si el número es positivo
print(f"Has ingresado el número positivo: {n}")
