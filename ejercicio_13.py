print("--- CALCULO DE FACTORIAL ---")
while True:
    n = int(input("Ingrese un número entero positivo (N): "))
    if n >= 0:
        break
    print("El número debe ser mayor o igual a cero.")

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"El factorial de {n} (¡{n}!) es: {factorial}")