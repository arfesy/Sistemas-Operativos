def carrito_compras():
    total_acumulado = 0.0
    total_items = 0
    
    print("--- Carrito de Compras ---")
    while True:
        try:
            print(f"\n[Ítems actuales en carrito: {total_items} | Total: ${total_acumulado:.2f}]")
            opcion = input("¿Desea agregar un producto? (S/N): ").strip().lower()
            if opcion == 'n' or opcion == 'no':
                break
            elif opcion != 's' and opcion != 'si':
                print("Opción inválida. Responda 'S' para sí o 'N' para no.")
                continue
                
            precio = float(input("Ingrese el precio del producto: $"))
            if precio <= 0:
                print("El precio debe ser mayor a 0.")
                continue
                
            cantidad = int(input("Ingrese la cantidad de unidades: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")
                continue
                
            total_acumulado += (precio * cantidad)
            total_items += cantidad
            
        except ValueError:
            print("Error de carga. Asegúrese de ingresar números correctos.")
            
    print(f"\n--- Compra Finalizada ---")
    print(f"- Cantidad total de ítems comprados: {total_items}")
    print(f"- Total neto acumulado: ${total_acumulado:.2f}")

if __name__ == "__main__":
    carrito_compras()