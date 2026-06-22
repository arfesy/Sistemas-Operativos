def analizar_numeros():
    positivos = 0
    negativos = 0
    ceros = 0
    CANTIDAD = 20
    
    print("--- Análisis de Números Positivos, Negativos y Ceros ---")
    for i in range(1, CANTIDAD + 1):
        while True:
            try:
                num = float(input(f"Ingrese el número {i} de {CANTIDAD}: "))
                if num > 0:
                    positivos += 1
                elif num < 0:
                    negativos += 1
                else:
                    ceros += 1
                break
            except ValueError:
                print("Entrada inválida. Ingrese un número válido.")
                
    print(f"\n--- Resultados ---")
    print(f"- Números positivos: {positivos}")
    print(f"- Números negativos: {negativos}")
    print(f"- Números iguales a cero: {ceros}")

if __name__ == "__main__":
    analizar_numeros()