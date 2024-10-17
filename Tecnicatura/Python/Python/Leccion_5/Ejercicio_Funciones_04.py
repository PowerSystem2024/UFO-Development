# Ejercicio 4: Calculadora de Impuestos
# Crear una funcion para calcular el total de un pago incluyendo
# un inpuesto aplicado. (IVA)
# Formula: pago_total = pago_sin_impuesto + pago_sin impuesto * (impuesto/100)
# proporcione el pago sin impuesto: 1000
# proporcione el monto del impuesto: 21%
# pago con impuesto: xxxxx

# Creamos la función que calcula el total del pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_total

# Ejecutamos la función
pago_sin_impuesto = float(input('Digite el pago sin impuestos: '))
impuesto = float(input('Digite el monto del impuesto a aplicar: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'El pago con impuesto es: {pago_con_impuesto}')