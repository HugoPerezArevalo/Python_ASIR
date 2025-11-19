monto = float(input("Introduce el monto de compra: "))
dia = str(input("Introduce el dia de la semana: "))

if dia == 'martes' or 'jueves':
    desc = monto * 0.15
    final = monto - desc
    print ('El precio final de compra es de', final, "El descuento es de", desc)

else:
    print ("No se aplica descuento ese dia de la semana")
    print ('El precio final de compra es de', monto)
