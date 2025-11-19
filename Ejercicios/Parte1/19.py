
saldo = 1000  # Saldo inicial

while True:
    print("\n=== Bienvenido a su Cajero Virtual ===")
    print("1. Ingresar dinero en cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")

    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        monto = float(input("Ingrese la cantidad a depositar: "))
        if monto > 0:
            saldo += monto
            print(f"Has ingresado ${monto:.2f}. Tu nuevo saldo es ${saldo:.2f}.")
        else:
            print("El monto debe ser positivo.")

    elif opcion == "2":
        monto = float(input("Ingrese la cantidad a retirar: "))
        if monto > saldo:
            print("Fondos insuficientes.")
        elif monto <= 0:
            print("El monto debe ser positivo.")
        else:
            saldo -= monto
            print(f"Has retirado ${monto:.2f}. Tu nuevo saldo es ${saldo:.2f}.")

    elif opcion == "3":
        print("Gracias por usar el Cajero Virtual. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
