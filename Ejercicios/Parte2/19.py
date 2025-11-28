
minimo = 1
maximo = 100
print("Piensa un número entre 1 y 100 (incluidos) y yo intentaré adivinarlo.")
input("Pulsa Enter cuando estés listo...")
while True:
    intento = (minimo + maximo) // 2
    print(f"¿Es tu número {intento}?")
    respuesta = input("Responde con 'mayor', 'menor' o 'igual': ").strip().lower()
    
    match respuesta:
        case 'igual':
            print(f"¡He adivinado tu número! Es {intento}.")
            break
        case 'mayor':
            minimo = intento + 1
        case 'menor':
            maximo = intento - 1
        case _:
            print("Respuesta no válida. Por favor, responde con 'mayor', 'menor' o 'igual'.")
