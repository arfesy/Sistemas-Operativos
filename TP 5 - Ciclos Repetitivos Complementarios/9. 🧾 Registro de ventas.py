def registro_ventas():
    total_vendido = 0.0
    ventas_mayores_1000 = 0
    
    print("--- Registro de Ventas Diarias ---")
    while True:
        respuesta = input("\n¿Desea registrar una venta? (S/N): ").strip().lower()
        if respuesta == 'n' or respuesta == 'no':
            break
        elif respuesta != 's' and respuesta != 'si':
            print("Opción inválida. Ingrese S o N.")
            continue
            
        producto = input("Nombre del producto: ")
        
        try:
            cantidad = int(input(f"Cantidad de '{producto}': "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")
                continue
                
            precio_unitario = float(input("Precio unitario: $"))
            if precio_unitario <= 0:
                print("El precio debe ser mayor a 0.")
                continue
                
            monto_venta = cantidad * precio_unitario
            total_vendido += monto_venta
            
            print(f"Monto de esta venta: ${monto_venta:.2f}")
            if monto_venta > 1000:
                ventas_mayores_1000 += 1
                
        except ValueError:
            print("Error en los datos numéricos de la venta. Registro cancelado.")
            
    print(f"\n--- Cierre de Caja ---")
    print(f"- Total total vendido en el día: ${total_vendido:.2f}")
    print(f"- Cantidad de ventas que superaron los $1000: {ventas_mayores_1000}")

if __name__ == "__main__":
    registro_ventas()