
positivos = 0
negativos = 0
while True:
    num = int(input("Introduce un número no nulo (0 para terminar): "))
    if num == 0:
        break
    if num > 0:
        positivos += 1
    else:
        negativos += 1
if negativos > 0:
    print("Se ha leído al menos un número negativo.")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")