altura = int(input("Introduce la altura de la piramide invertida: "))

if altura <=0:
    print("La altura debe ser un numero positivo")
else:
    for i in range (altura, 0, -1):
        espacios = ' ' * (altura - i)
        asteriscos = '*' * (2 * i - 1)
        print(espacios + asteriscos)
        