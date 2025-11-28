
notas = []
while True:
    nota = float(input("Introduce una nota (o -1 para terminar): "))
    if nota == -1:
        break
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida. Por favor, introduce una nota entre 0 y 10.")
if 10 in notas:
    print("Hubo al menos una nota con valor 10.")
else:
    print("No hubo ninguna nota con valor 10.")
