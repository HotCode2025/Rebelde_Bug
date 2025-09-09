# Ejercicio 4: Calculadora de Impuestos
# Crear una función para calcular el total de un pago incluyendo
# un impuesto aplicado. (IVA)
# Fórmula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxx

# 1. Definir la función
def calcular_pago_con_impuesto(pago_sin_impuesto, impuesto):

    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_total

# 2. Pedir datos al usuario
pago_base = float(input("Ingrese el pago sin impuesto: "))
iva = float(input("Ingrese el porcentaje de impuesto (%): "))

# 3. Calcular el pago con impuesto
total = calcular_pago_con_impuesto(pago_base, iva)

# 4. Mostrar el resultado
print(f"\nPago sin impuesto: {pago_base}")
print(f"Impuesto aplicado: {iva}%")
print(f"Pago total con impuesto: {total}")