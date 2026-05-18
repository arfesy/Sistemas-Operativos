print("--- PROMEDIO DE EDADES ---")
cantidad = int(input("¿De cuántas personas calculará el promedio de edad?: "))

if cantidad > 0:
    suma_edades = 0
    for i in range(1, cantidad + 1):
        edad = int(input(f"Ingrese la edad de la persona {i}: "))
        suma_edades += edad

    promedio = suma_edades / cantidad
    print(f"\nEl promedio de edad del grupo es: {promedio:.1f} años")
else:
    print("Cantidad inválida.")