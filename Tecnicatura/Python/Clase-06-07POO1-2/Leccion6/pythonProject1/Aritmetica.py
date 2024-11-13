class Aritmetica:
    """
    El nombre de este tipo de comentario es : DocStrig
    esto es documentacion de la calse python
    vamos a hacer en esta clase algunas operaciones de: suma, resta, multiplicacion y mas
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # Metodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return  self.operandoA - self.operandoB

    def multiplicacion(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB



aritmetica1 = Aritmetica(7, 9)
print(aritmetica1.sumar())
print(f'La suma de los numeros es: {aritmetica1.sumar()}')
print(f'la resta de los nuimeros es: {aritmetica1.resta()}')
print(f'La multiplicacion de los numewros es: {aritmetica1.multiplicacion()}')
print(f'La division de los numeros es: {aritmetica1.dividir():.2f}')