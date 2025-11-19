
nombre = input("Ingrese el nombre del postulante: ")
facultad = input("Ingrese la facultad a estudiar (Ingenieria, Medicina, Derecho, Arquitectura): ")
importe = 0
mensualidad = 0
if facultad == "Ingenieria":
    importe = 5000
    mensualidad = 800
elif facultad == "Medicina":
    importe = 7000
    mensualidad = 1200
elif facultad == "Derecho":
    importe = 4000
    mensualidad = 600
elif facultad == "Arquitectura":
    importe = 6000
    mensualidad = 900
else:
    print("Facultad no válida.")
    exit()
igv = (importe + mensualidad) * 0.18
monto_final = importe + mensualidad + igv
print(f"Postulante: {nombre}")
print(f"Facultad: {facultad}")
print(f"Importe: S/{importe}")
print(f"Mensualidad: S/{mensualidad}")
print(f"IGV (18%): S/{igv}")
print(f"Monto final a pagar: S/{monto_final}")