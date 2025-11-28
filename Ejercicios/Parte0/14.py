
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
if num2 != 0:
    division = num1 / num2
    print(f"La división es: {division}")
else:
    print("Error: División por cero no está definida.")
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"El producto es: {producto}")
