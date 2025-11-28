
   
n = int(input("Introduce la mitad de la altura del diamante (n): "))
if n <= 0:
    print("La altura debe ser un número positivo.")
else:
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    
    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()