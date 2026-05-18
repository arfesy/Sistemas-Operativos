print("--- CONTROL DE MAYORÍA DE EDAD ---")
n = int(input("Ingrese la cantidad total de personas (N): "))
mayores_edad = 0

for i in range(1, n + 1):
    edad = int(input(f"Ingrese la edad de la persona {i}: "))
    if edad >= 18:
        mayores_edad += 1

print(f"\nTotal de personas mayores o iguales a 18 años: {mayores_edad}")