print("--- OPERACIONES CON PARES E IMPARES ---")
n = int(input("¿Cuántos números enteros va a ingresar?: "))

suma_pares = 0
suma_impares = 0
contador_impares = 0

for i in range(1, n + 1):
    numero = int(input(f"Ingrese el número entero {i}: "))
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
        contador_impares += 1

print(f"\nSuma total de los números pares: {suma_pares}")
if contador_impares > 0:
    promedio_impares = suma_impares / contador_impares
    print(f"Promedio de los números impares: {promedio_impares:.2f}")
else:
    print("No se ingresaron números impares, no se puede calcular su promedio.")