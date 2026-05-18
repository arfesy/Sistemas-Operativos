print("--- CONVERTIR NEGATIVOS A POSITIVOS ---")
resultados = []

for i in range(1, 16):
    while True:
        numero = float(input(f"Ingrese el número negativo {i}: "))
        if numero < 0:
            break
        print("Por favor, ingrese un número que sea estrictamente menor que cero.")
    
    positivo = numero * -1
    resultados.append(positivo)

print("\nLos números convertidos a positivos son:")
print(resultados)