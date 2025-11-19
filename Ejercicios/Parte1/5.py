from math import pi

radio = float(input("Introduce el radio del circulo: "))
diametro = radio / 2
longitudR = diametro / 2
longitudC = pi * diametro
area = pi * radio**2
volumen = 4/3 * pi * radio**3
print ("El area es: ", area)
print ("El volumen es: ", volumen)
print ("El diametro es: ", diametro)
print ("La longitud del radio es: ", longitudR)
print ("La longitud del circulo es: ", longitudC)