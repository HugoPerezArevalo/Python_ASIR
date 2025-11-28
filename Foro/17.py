
cadena = input("Introduce una cadena: ")
nueva_cadena = ""
for caracter in cadena:
    if cadena.count(caracter) > 1 and caracter not in nueva_cadena:
        nueva_cadena += caracter
print("Cadena con caracteres repetidos:", nueva_cadena)