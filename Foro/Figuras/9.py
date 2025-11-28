
n = int(input("Introduce un número impar para el tamaño del cuadrado con cuadro hueco: "))
if n % 2 == 0 or n <= 0:
    print("El número debe ser impar y positivo.")
else:
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == n - 1 or j == 0 or j == n - 1 or 
                i == j or i + j == n - 1 or 
                (n // 4 <= i < 3 * n // 4 and n // 4 <= j < 3 * n // 4 and 
                 (i == n // 4 or i == 3 * n // 4 - 1 or j == n // 4 or j == 3 * n // 4 - 1))):
                print("*", end="")
            else:
                print(" ", end="")
        print()