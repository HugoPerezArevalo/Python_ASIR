
cadena = input("Introduce una cadena: ")
contador_mayusculas = 0
for caracter in cadena:
    if 'A' <= caracter <= 'Z':
        contador_mayusculas += 1
print(f"La cadena contiene {contador_mayusculas} letras mayúsculas.")