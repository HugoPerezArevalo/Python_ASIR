
n = int(input("Introduce un número impar para el tamaño de la M: "))
if n % 2 == 0 or n <= 0:
    print("El número debe ser impar y positivo.")
else:
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n - 1 or (j == i and i <= n // 2) or (j == n - i - 1 and i <= n // 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()
    