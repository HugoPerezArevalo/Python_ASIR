#Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contien
cadena = input("Introduce una cadena: ")
contador_numeros = 0
for caracter in cadena:
    if '0' <= caracter <= '9':
        contador_numeros += 1
print(f"La cadena contiene {contador_numeros} caracteres numéricos.")
