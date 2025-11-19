
num = int(input("Ingrese un número entre 0 y 99999: "))


if 0 <= num <= 99999:

    cifras = len(str(num))
    print(f"El número {num} tiene {cifras} cifra(s).")
else:
    print("El número ingresado está fuera del rango permitido (0 a 99999).")
