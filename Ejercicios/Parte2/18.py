
A = float(input("Ingrese la base A: "))
B = int(input("Ingrese el exponente B (entero no negativo): "))
resultado = 1
for _ in range(B):
    resultado *= A
print(f"{A} elevado a {B} es: {resultado}")
