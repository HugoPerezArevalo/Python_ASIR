
cadena = input("Introduce una cadena: ")
vocales = "aeiouAEIOU"
contador = 0
for caracter in cadena:
    if caracter in vocales:
        contador += 1
print(f"La cadena contiene {contador} vocales.")