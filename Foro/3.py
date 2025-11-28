
cadena = input("Introduce una cadena: ")
caracter = input("Introduce el carácter a buscar: ")
contador = 0
for c in cadena:
    if c == caracter:
        contador += 1
print(f"El carácter '{caracter}' aparece {contador} veces en la cadena.")