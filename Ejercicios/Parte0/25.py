
calificacion = float(input("Introduce una calificación numérica entre 0 y 10: "))
if 0 <= calificacion < 3:
    print("Calificación alfabética: Muy Deficiente")
elif 3 <= calificacion < 5:
    print("Calificación alfabética: Insuficiente")
elif 5 <= calificacion < 6:
    print("Calificación alfabética: Suficiente")
elif 6 <= calificacion < 7:
    print("Calificación alfabética: Bien")
elif 7 <= calificacion < 9:
    print("Calificación alfabética: Notable")
elif 9 <= calificacion <= 10:
    print("Calificación alfabética: Sobresaliente")
else:
    print("Calificación fuera de rango. Por favor, introduce un valor entre 0 y 10.")