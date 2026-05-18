print("--- FILTRAR NÚMEROS POSITIVOS ---")
numeros_positivos = []

for i in range(1, 11):
    numero = float(input(f"Ingrese el número {i}: "))
    if numero > 0:
        numeros_positivos.append(numero)

print("\nLos números positivos ingresados son:")
print(numeros_positivos)