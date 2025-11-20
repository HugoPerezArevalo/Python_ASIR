precioVenta = float(input("Introduce el precio de venta: "))
precioReal = float(input("Introduce el precio real: "))

descuento = ((precioReal - precioVenta) / precioReal) * 100
print ("El descuento es del: ", descuento,"%")