#Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún 
#número negativo o no.

hay_negativo = False
for _ in range(100):
    numero = int(input("Introduce un número no nulo: "))
    if numero < 0:
        hay_negativo = True
if hay_negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")