
cadena = input("Introduce una cadena: ")
vocales = "aeiouAEIOU"
nueva_cadena = ""
for caracter in cadena:
    if caracter in vocales:
        nueva_cadena += caracter * 2
    else:
        nueva_cadena += caracter
print("Cadena modificada:", nueva_cadena)