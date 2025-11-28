
suma_pares = 0
suma_impares = 0
for numero in range(100, 201):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
print(f"Suma de números pares entre 100 y 200: {suma_pares}")
print(f"Suma de números impares entre 100 y 200: {suma_impares}")