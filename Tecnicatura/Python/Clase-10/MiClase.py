class MiClase:

    variable_clase = 'Esta es una variable de clase'

    def __init__(self,variable_intancia):
        self.variable_intancia = variable_intancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_intancia)


print(MiClase.variable_clase)
miClase1 = MiClase('Esta es una variable de instancia ')
print(miClase1.variable_intancia)
print(miClase1.variable_clase)
miClase2 = MiClase('Esta es otra prueba de variable de intancia')
print(miClase2.variable_intancia)
print(miClase2.variable_clase)

MiClase.variable_clase2 = 'Valor de variable clase 2'
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)


MiClase.metodo_estatico()

MiClase.metodo_clase()
miObjeto1 = MiClase('variable de instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()