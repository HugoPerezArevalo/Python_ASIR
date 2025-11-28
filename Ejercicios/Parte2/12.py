altura = int(input("Introduce la altura de la escalera de números: "))
if altura <= 0:
    print ("La altura debe ser un número positivo")
    
else:
    for i in range(1, altura + 1):
        print(str(i) * i)
