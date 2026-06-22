def control_combustible():
    total_litros = 0.0
    cantidad_cargas = 0
    alertas_carga_minima = 0
    
    print("--- Control de Carga de Combustible ---")
    while True:
        try:
            entrada = input("Ingrese los litros de la carga (o 'salir' para terminar): ")
            if entrada.lower() == 'salir':
                break
            
            litros = float(entrada)
            if litros <= 0:
                print("La carga debe ser mayor a 0 litros.")
                continue
                
            total_litros += litros
            cantidad_cargas += 1
            
            if litros < 5:
                print(" Alerta: Carga inferior a 5 litros (sospecha de error o recarga mínima).")
                alertas_carga_minima += 1
                
        except ValueError:
            print("Entrada inválida. Ingrese un número o escriba 'salir'.")
            
    if cantidad_cargas > 0:
        promedio = total_litros / cantidad_cargas
        print(f"\n--- Resumen del Control ---")
        print(f"- Total cargado: {total_litros:.2f} litros")
        print(f"- Promedio por carga: {promedio:.2f} litros")
        print(f"- Cargas inferiores a 5L: {alertas_carga_minima}")
    else:
        print("No se registraron cargas de combustible.")


if __name__ == "__main__":
    control_combustible()