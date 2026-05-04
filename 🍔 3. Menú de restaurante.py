def mostrar_menu():
    print("\n--- MENÚ DEL RESTAURANTE ---")
    print("1. Hamburguesa")
    print("2. Pizza")
    print("3. Ensalada")
    print("4. Salir")

opcion = 0
while opcion != 4:
    mostrar_menu()
    try:
        opcion = int(input("Elija una opción (1-4): "))

        match opcion:
            case 1:
                print("Has elegido: Hamburguesa 🍔")
            case 2:
                print("Has elegido: Pizza 🍕")
            case 3:
                print("Has elegido: Ensalada 🥗")
            case 4:
                print("Gracias por visitarnos. ¡Adiós!")
            case _:
                print("Opción no válida. Intente de nuevo.")
    except ValueError:
        print("Error: Ingrese el número de la opción.")