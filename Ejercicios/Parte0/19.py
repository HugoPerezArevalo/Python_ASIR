
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))
if num1 >= num2 and num1 >= num3:
    mayor = num1
    if num2 >= num3:
        menor = num3
    else:
        menor = num2
elif num2 >= num1 and num2 >= num3:
    mayor = num2
    if num1 >= num3:
        menor = num3
    else:
        menor = num1
else:
    mayor = num3
    if num1 >= num2:
        menor = num2
    else:
        menor = num1
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
if num1 == num2 == num3:
    print("Los tres números son iguales.")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Hay números iguales.")
else:
    print("No hay números iguales.")