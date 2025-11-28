
nota = float(input("Ingrese una nota (o -1 para terminar): "))
hay_nota_diez = False
while nota != -1:
    if nota == 10:
        hay_nota_diez = True
        print("¡Hay una nota de 10!")
    nota = float(input("Ingrese una nota (o -1 para terminar): "))
if not hay_nota_diez:
    print("No hay notas de 10.")