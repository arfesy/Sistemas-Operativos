print("--- CALIFICACIÓN MÁS ALTA Y MÁS BAJA ---")
cantidad = int(input("¿Cuántas calificaciones desea ingresar?: "))

if cantidad > 0:
    calificacion = float(input("Ingrese la calificación 1: "))
    maxima = calificacion
    minima = calificacion

    for i in range(2, cantidad + 1):
        calificacion = float(input(f"Ingrese la calificación {i}: "))
        if calificacion > maxima:
            maxima = calificacion
        if calificacion < minima:
            minima = calificacion

    print(f"\nLa calificación más alta es: {maxima}")
    print(f"La calificación más baja es: {minima}")
else:
    print("Cantidad no válida.")