
n = int(input("Introduce un número impar para el tamaño de la estrella: "))
if n % 2 == 0 or n <= 0:
    print("El número debe ser impar y positivo.")
else:
    for i in range(n):
        for j in range(n):
            if i == n // 2 or j == n // 2 or i == j or i + j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()