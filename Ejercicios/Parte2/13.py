altura = int(input("Introduce la altura de la escalera de números: "))

if altura <=0:
    print("La altura debe ser un número positivo")
    
else:
    for i in range(1, altura + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()