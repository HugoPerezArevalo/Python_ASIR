
suma_pares = 0
suma_impares = 0
for numero in range(100, 201):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
print("Suma de los números pares:", suma_pares)
print("Suma de los números impares:", suma_impares)