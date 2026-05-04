try:
    dia = int(input("Ingrese un número del 1 al 7 (1: Lunes, 7: Domingo): "))

    if 1 <= dia <= 5:
        print("Es un día laboral. 💼")
    elif dia == 6 or dia == 7:
        print("Es fin de semana. 🥳")
    else:
        print("Número fuera de rango. Ingrese un valor del 1 al 7.")
except ValueError:
    print("Error: Por favor ingrese un número entero.")