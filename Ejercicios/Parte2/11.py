altura = int(input("Introduce la altura de la escalera de asteriscos: "))

if altura <=0:
    print("La altura debe ser un número positivo")
    
else:
    for i in range (0, altura, +1):
        asteriscos = '*' * (i +1)
        print (asteriscos)