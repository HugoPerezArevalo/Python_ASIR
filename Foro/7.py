
cadena = input("Introduce una cadena: ")
caracter_a_reemplazar = input("Introduce el carácter a reemplazar: ")
caracter_nuevo = input("Introduce el nuevo carácter: ")
nueva_cadena = ""
for caracter in cadena:
    if caracter == caracter_a_reemplazar:
        nueva_cadena += caracter_nuevo
    else:
        nueva_cadena += caracter
print("Cadena modificada:", nueva_cadena)
