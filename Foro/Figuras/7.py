
altura = int(input("Introduce la altura del triángulo invertido: "))
if altura <= 0:
    print("La altura debe ser un número positivo.")
else:
    for i in range(altura):
        for j in range(altura):
            if i == 0 or i == altura - 1 or j == 0 or j == altura - 1:
                print("*", end="")
            elif i % 2 == 1 and (j % 2 == 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()
