
nombre = input("Introduce el nombre del trabajador: ")
horas_trabajadas = float(input("Introduce el número de horas trabajadas en la semana: "))
tarifa_hora = float(input("Introduce la tarifa por hora (€): "))
if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * tarifa_hora
else:
    salario_bruto = (35 * tarifa_hora) + ((horas_trabajadas - 35) * tarifa_hora * 1.5)
if salario_bruto <= 500:
    impuestos = 0
elif salario_bruto <= 900:
    impuestos = (salario_bruto - 500) * 0.25
else:
    impuestos = (400 * 0.25) + ((salario_bruto - 900) * 0.45)
salario_neto = salario_bruto - impuestos
print(f"Trabajador: {nombre}")
print(f"Salario bruto: {salario_bruto:.2f} €")
print(f"Impuestos: {impuestos:.2f} €")
print(f"Salario neto: {salario_neto:.2f} €")
