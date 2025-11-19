calificacion = float(input("Ingrese una calificación entre 0 y 10: "))


if 0 <= calificacion <= 10:
    match calificacion:
        case c if 0 <= c < 3:
            resultado = "Muy Deficiente"
        case c if 3 <= c < 5:
            resultado = "Insuficiente"
        case c if 5 <= c < 6:
            resultado = "Suficiente"
        case c if 6 <= c < 7:
            resultado = "Bien"
        case c if 7 <= c < 9:
            resultado = "Notable"
        case c if 9 <= c <= 10:
            resultado = "Sobresaliente"
    print(f"La calificación {calificacion} equivale a: {resultado}")
else:
    print("Error: la calificación debe estar entre 0 y 10.")
