try:
    edad = int(input("Ingrese su edad: "))

    if edad < 0:
        print("Error: La edad no puede ser negativa.")
    elif edad < 18:
        print("Categoría: Menor de edad.")
    elif edad >= 18 and edad <= 64:
        print("Categoría: Adulto.")
    else:
        print("Categoría: Adulto mayor.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")