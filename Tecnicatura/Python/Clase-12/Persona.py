class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self,other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self,otro):#sub es subtraccion
        return self.edad+otro.edad

persona1 = Persona('Dario',36)
persona2 = Persona('Benitez',5)


#persona1.__add__(persona2)sintaxis interna y automatica

print(persona1+persona2)
print(persona1-persona2)