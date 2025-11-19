num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))


mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)


print(f"\nEl número mayor es: {mayor}")
print(f"El número menor es: {menor}")


if num1 == num2 == num3:
    print("Los tres números son iguales.")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Hay dos números iguales.")
else:
    print("Todos los números son diferentes.")
