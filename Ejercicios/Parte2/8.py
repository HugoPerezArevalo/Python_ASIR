
numeros_positivos = 0
numeros_negativos = 0
for _ in range(100):
    numero = int(input("Introduce un número no nulo: "))
    if numero > 0:
        numeros_positivos += 1
    else:
        numeros_negativos += 1
print("Números positivos leídos:", numeros_positivos)
print("Números negativos leídos:", numeros_negativos)