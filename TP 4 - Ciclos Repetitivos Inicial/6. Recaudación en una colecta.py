def recaudacion_colecta():
    total_recaudado = 0.0
    mayor_donacion = 0.0
    cantidad_aportantes = 0
    
    print("--- Simulación de Colecta ---")
    while True:
        try:
            entrada = input("Ingrese el monto de la donación (o 'fin' para terminar): ")
            if entrada.lower() == 'fin':
                break
                
            donacion = float(entrada)
            if donacion <= 0:
                print("La donación debe ser un monto mayor a 0.")
                continue
                
            total_recaudado += donacion
            cantidad_aportantes += 1
            
            if donacion > mayor_donacion:
                mayor_donacion = donacion
                
        except ValueError:
            print("Entrada inválida. Ingrese un monto numérico o escriba 'fin'.")
            
    print(f"\n--- Resumen de la Colecta ---")
    print(f"- Total recaudado: ${total_recaudado:.2f}")
    print(f"- Cantidad de personas que aportaron: {cantidad_aportantes}")
    print(f"- Mayor donación recibida: ${mayor_donacion:.2f}")


if __name__ == "__main__":
    recaudacion_colecta()