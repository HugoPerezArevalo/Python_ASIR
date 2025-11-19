
nombre = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))
tarifa_hora = float(input("Ingrese la tarifa por hora (€): "))


if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * tarifa_hora
else:
    horas_normales = 35
    horas_extra = horas_trabajadas - 35
    salario_bruto = (horas_normales * tarifa_hora) + (horas_extra * tarifa_hora * 1.5)


if salario_bruto <= 500:
    impuesto = 0
elif salario_bruto <= 900:
    impuesto = (salario_bruto - 500) * 0.25
else:
    impuesto = (400 * 0.25) + ((salario_bruto - 900) * 0.45)


salario_neto = salario_bruto - impuesto



print(f"Nombre del trabajador: {nombre}")
print(f"Salario bruto: €{salario_bruto:.2f}")
print(f"Impuestos: €{impuesto:.2f}")
print(f"Salario neto: €{salario_neto:.2f}")
