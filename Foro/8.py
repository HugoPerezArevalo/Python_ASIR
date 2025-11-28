
cadena = input("Introduce una cadena: ")
cadena_mayusculas = ""
for caracter in cadena:
    if 'a' <= caracter <= 'z':
        caracter_mayuscula = chr(ord(caracter) - (ord('a') - ord('A')))
        cadena_mayusculas += caracter_mayuscula
    else:
        cadena_mayusculas += caracter
print("Cadena en mayúsculas:", cadena_mayusculas)
cadena_minusculas = ""
for caracter in cadena:
    if 'A' <= caracter <= 'Z':
        caracter_minuscula = chr(ord(caracter) + (ord('a') - ord('A')))
        cadena_minusculas += caracter_minuscula
    else:
        cadena_minusculas += caracter
print("Cadena en minúsculas:", cadena_minusculas)