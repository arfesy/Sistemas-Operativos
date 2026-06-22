def simulador_compras_limite():
    LIMITE_DIARIO = 20000.0
    total_compras = 0.0
    
    print("--- Simulador de Compras con Límite Diario ---")
    while total_compras < LIMITE_DIARIO:
        try:
            print(f"Saldo restante disponible: ${LIMITE_DIARIO - total_compras:.2f}")
            entrada = input("Ingrese el valor de la compra (o '0' para salir): ")
            if entrada == '0':
                break
                
            valor = float(entrada)
            if valor < 0:
                print("El valor de la compra no puede ser negativo.")
                continue
                
            if total_compras + valor > LIMITE_DIARIO:
                print(f" Compra rechazada. Excede el límite diario de ${LIMITE_DIARIO:.2f}.")
                continue
                
            total_compras += valor
            
        except ValueError:
            print("Entrada inválida. Ingrese un valor numérico.")
            
    print(f"\nCompras finalizadas. Total gastado hoy: ${total_compras:.2f}")
    if total_compras >= LIMITE_DIARIO:
        print("Has alcanzado el límite máximo permitido de $20.000.")


if __name__ == "__main__":
    simulador_compras_limite()