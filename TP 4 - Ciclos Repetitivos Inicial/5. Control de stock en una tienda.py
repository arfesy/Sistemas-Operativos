def control_stock():
    STOCK_INICIAL = 100 
    stock_actual = STOCK_INICIAL
    LIMITE_ALERTA = STOCK_INICIAL * 0.10
    
    print("--- Control de Stock en Tienda ---")
    print(f"Stock inicial disponible: {STOCK_INICIAL} unidades.")
    
    while stock_actual > 0:
        try:
            entrada = input(f"Ingrese cantidad vendida (Stock disponible: {stock_actual}) o '0' para finalizar: ")
            if entrada == '0':
                print("Finalizando control a petición del usuario.")
                break
                
            vendidos = int(entrada)
            if vendidos < 0:
                print("La cantidad vendida no puede ser negativa.")
                continue
                
            if vendidos > stock_actual:
                print(f"No hay suficiente stock. Solo quedan {stock_actual} unidades.")
                continue
                
            stock_actual -= vendidos
            
            if 0 < stock_actual <= LIMITE_ALERTA:
                print(f" ¡ALERTA! El stock actual ({stock_actual} unidades) es menor al 10% del stock original.")
                
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
            
    if stock_actual == 0:
        print("El stock se ha agotado por completo.")


if __name__ == "__main__":
    control_stock()