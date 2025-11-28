
cantidad = int(input("Introduce una cantidad de euros (múltiplo de 5 €): "))
if cantidad % 5 != 0 or cantidad < 0:
    print("Por favor, introduce una cantidad válida (múltiplo de 5 €).")
else:
    billetes = [500, 200, 100, 50, 20, 10, 5]
    resultado = {}
    
    for billete in billetes:
        if cantidad >= billete:
            num_billetes = cantidad // billete
            cantidad -= num_billetes * billete
            resultado[billete] = num_billetes
    
    print("Desglose de billetes necesarios:")
    for billete, num in resultado.items():
        print(f"{num} billete(s) de {billete} €")