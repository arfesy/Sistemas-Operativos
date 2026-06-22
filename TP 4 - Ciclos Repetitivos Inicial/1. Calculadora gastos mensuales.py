def calculadora_gastos():
    LIMITE_PRESUPUESTO = 50000.0 
    total_gastado = 0.0
    
    print("--- Calculadora de Gastos Mensuales ---")
    while True:
        try:
            gasto = float(input("Ingrese un gasto del mes (0 para finalizar): "))
            if gasto == 0:
                break
            elif gasto < 0:
                print("El gasto no puede ser negativo.")
                continue
            total_gastado += gasto
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            
    print(f"\nTotal gastado en el mes: ${total_gastado:.2f}")
    if total_gastado > LIMITE_PRESUPUESTO:
        print(f" ¡ADVERTENCIA! Se superó el límite presupuestado de ${LIMITE_PRESUPUESTO:.2f}")
    else:
        print("El gasto se mantuvo dentro del presupuesto establecido.")


if __name__ == "__main__":
    calculadora_gastos()