def tabla_multiplicar():
    print("--- Tabla de Multiplicar Personalizada ---")
    while True:
        try:
            numero = int(input("Ingrese el número para generar la tabla: "))
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
            
    print(f"\nTabla del {numero}:")
    for i in range(1, 13):
        resultado = numero * i
        print(f"{numero} x {i:2d} = {resultado}")

if __name__ == "__main__":
    tabla_multiplicar()