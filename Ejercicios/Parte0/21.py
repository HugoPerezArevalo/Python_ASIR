
count = 0
negative_found = False
while count < 100:
    num = float(input("Introduce un número no nulo: "))
    if num == 0:
        print("El número no debe ser cero. Inténtalo de nuevo.")
        continue
    if num < 0:
        negative_found = True
    count += 1
if negative_found:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")
