class Rectangulo:
    """
    Crear una clase rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular_area utlizando la frmula:
    area = base * altura. Pero la base y la altura debenser ingresada por
    usuario y los objetos deben ser 3.
    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return  self.altura * self.base

base = int(input('Digite el numero para la base del rectangulo: '))
altura = int(input('Digite el numero para la altura del rectangulo: '))
rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')

