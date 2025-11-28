
cadena = input("Introduce una cadena: ")
nueva_cadena = ""
for caracter in cadena:
    
    if caracter != " ":
        nueva_cadena += caracter
print("Cadena filtrada (sin espacios):", nueva_cadena)