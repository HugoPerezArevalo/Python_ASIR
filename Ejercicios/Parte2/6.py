
n = int(input("Introduce un número entero positivo: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("El factorial de", n, "es", factorial)
    