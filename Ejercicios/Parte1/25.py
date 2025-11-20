
print("=== MATRÍCULA UNIVERSITARIA ===")

nombre = input("Ingrese el nombre del postulante: ")
facultad = input("Ingrese la facultad: ")


fac = facultad.lower()


importe = 0
mensualidad = 0

match fac:
    case "ing. de sistemas" | "sistemas" | "ingeniería de sistemas":
        importe = 350
        mensualidad = 650

    case "derecho":
        importe = 300
        mensualidad = 550

    case "ing. naviera" | "naviera" | "ingeniería naviera":
        importe = 300
        mensualidad = 500

    case "ing. pesquera" | "pesquera" | "ingeniería pesquera":
        importe = 310
        mensualidad = 460

    case "contabilidad":
        importe = 280
        mensualidad = 490

    case "administración":
        importe = 360
        mensualidad = 520

    case _:
        print("Facultad no válida")
        exit()



subtotal = importe + mensualidad
igv = subtotal * 0.18
total_pagar = subtotal + igv


print("\n=== RESULTADOS ===")
print(f"Postulante: {nombre}")
print(f"Facultad: {facultad}")
print(f"Importe de matrícula: ${importe}")
print(f"Mensualidad: ${mensualidad}")
print(f"IGV (18%): ${igv:.2f}")
print(f"Monto total a pagar: ${total_pagar:.2f}")
