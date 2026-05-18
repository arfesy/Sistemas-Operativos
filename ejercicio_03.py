print("--- CONTADOR DE POSITIVOS, NEGATIVOS Y CEROS ---")
positivos = 0
negativos = 0
ceros = 0

for i in range(1, 21):
    numero = float(input(f"Ingrese el número {i}: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print(f"\nCantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de ceros: {ceros}")