
def main():
    positivos = 0
    negativos = 0
    hay_negativo = False

    while True:
        numero = int(input("Introduce un número (0 para terminar): "))
        if numero == 0:
            break
        elif numero > 0:
            positivos += 1
        else:
            negativos += 1
            hay_negativo = True

    print(f"Números positivos leídos: {positivos}")
    print(f"Números negativos leídos: {negativos}")
    if hay_negativo:
        print("Se ha leído al menos un número negativo.")
    else:
        print("No se ha leído ningún número negativo.")
