def conversor():
    print("1. Celsius a Fahrenheit\n2. Kilómetros a Millas")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        c = float(input("Grados Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C equivalen a {f}°F")
    elif opcion == "2":
        km = float(input("Kilómetros: "))
        millas = km * 0.621371
        print(f"{km} km equivalen a {millas:.2f} millas")

conversor()