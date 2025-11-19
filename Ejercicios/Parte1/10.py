n1 = float(input("Introduce el primer numero: "))
n2 = float(input("Introduce el segundo numero: "))
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2


if n1 or n2 != 0:
    division = n1 / n2
else:
    print("No se puede dividir entre 0")
    
print ("La suma es: ", suma, "La resta es: ", resta, "La multiplicacion es: ", multiplicacion, "La division es: ", division)