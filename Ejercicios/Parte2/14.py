altura = int(input("Introduce la altura de la piramide: "))
if altura <=0:
    print("La altura debe ser un numero positivo")
else:
    for i in range (1, altura, +1):
        espacios = ' ' * (altura - i)
        asterioscos = '*' * (2 * i -1)
        print (espacios + asterioscos)