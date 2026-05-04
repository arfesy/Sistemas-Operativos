try:
    velocidad = float(input("Ingrese la velocidad del vehículo (km/h): "))

    if velocidad <= 60:
        print("Situación: Dentro del límite permitido.")
    elif 61 <= velocidad <= 80:
        print("Situación: Exceso leve.")
    else:
        print("Situación: Exceso grave. ¡Reduzca la velocidad!")
except ValueError:
    print("Error: Ingrese un valor numérico.")