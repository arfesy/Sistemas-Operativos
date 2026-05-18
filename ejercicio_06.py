print("--- TABLA DE MULTIPLICAR ---")
numero = int(input("Ingrese el número para generar su tabla: "))

print(f"\nTabla del {numero}:")
for i in range(1, 11):
    producto = numero * i
    print(f"{numero} x {i} = {producto}")