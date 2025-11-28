
cadena = input("Introduce una cadena: ")
caracter_a_buscar = input("Introduce el carácter a buscar: ")
encontrado = False
for caracter in cadena:
    if caracter == caracter_a_buscar:
        encontrado = True
        break
if encontrado:
    print(f"El carácter '{caracter_a_buscar}' se encuentra en la cadena.")
else:
    print(f"El carácter '{caracter_a_buscar}' no se encuentra en la cadena.")