print("--- SUMA DE NÚMEROS PARES HASTA N ---")
n = int(input("Ingrese el valor límite superior (N): "))
suma_pares = 0

for i in range(2, n + 1, 2):
    suma_pares += i

print(f"La suma de los números pares desde 2 hasta {n} es: {suma_pares}")