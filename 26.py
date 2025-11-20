print("=== LANZAMIENTO DE TRES DADOS ===")

d1 = int(input("Ingrese el valor del dado 1: "))
d2 = int(input("Ingrese el valor del dado 2: "))
d3 = int(input("Ingrese el valor del dado 3: "))

cantidad_seis = (d1 == 6) + (d2 == 6) + (d3 == 6)

match cantidad_seis:
    case 3:
        mensaje = "Excelente"
    case 2:
        mensaje = "Muy bien"
    case 1:
        mensaje = "Regular"
    case 0:
        mensaje = "Pésimo"
    case _:
        mensaje = "Error inesperado"

print(f"\nResultado: {mensaje}")
