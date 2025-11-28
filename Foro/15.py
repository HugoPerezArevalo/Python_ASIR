
cadena = input("Introduce una cadena: ")
vocales = "aeiouAEIOU"
nueva_cadena = ""
for caracter in cadena:
    if caracter in vocales:
        nueva_cadena += '*'
    else:
        nueva_cadena += caracter
print("Cadena modificada:", nueva_cadena)