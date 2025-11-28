
n = int(input("Introduce la altura de la pirámide (n): "))
if n <= 0:
    print("La altura debe ser un número positivo.")
else:
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == n - 1 or j % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()