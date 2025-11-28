
cadena = input("Introduce una cadena: ")
vocales = "aeiouAEIOU "
nueva_cadena = ""
for caracter in cadena:
    if caracter not in vocales:
        nueva_cadena += caracter
print("Cadena con consonantes:", nueva_cadena)
