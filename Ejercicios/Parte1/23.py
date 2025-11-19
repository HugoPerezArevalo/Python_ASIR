precio_compra = float(input("Introduce el precio de la compra: "))
metodo_pago = str(input("Introduce el metodo de pago (contado o tarjeta): "))

if metodo_pago == "contado":
    descuento = precio_compra * 0.05
    precio_final = precio_compra - descuento
    print (f"El precio final pagando al contado es de {precio_final}")
    
elif metodo_pago == "tarjeta":
    suma = precio_compra * 0.03
    precio_final = precio_compra + suma
    print (f"El precio final pagando con tarjeta es de {precio_final}")
