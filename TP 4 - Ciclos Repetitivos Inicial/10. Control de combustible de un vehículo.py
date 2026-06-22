def control_combustible_vehiculo():
    LITROS_POR_KM = 0.07
    DISTANCIA_A_VERIFICAR = 50.0
    combustible_actual = 0.0
    litros_necesarios_50km = DISTANCIA_A_VERIFICAR * LITROS_POR_KM
    
    print("--- Control de Combustible del Vehículo ---")
    while True:
        print(f"\nCombustible en tanque: {combustible_actual:.2f} litros.")
        
        
        if combustible_actual >= litros_necesarios_50km:
            print(f" Combustible suficiente para recorrer {DISTANCIA_A_VERIFICAR} km.")
        else:
            print(f" Alerta: Combustible INSUFICIENTE para recorrer {DISTANCIA_A_VERIFICAR} km (Faltan {(litros_necesarios_50km - combustible_actual):.2f}L).")
            
        print("1. Registrar Carga de Combustible")
        print("2. Registrar Consumo (Viaje realizado)")
        print("3. Detener Simulador")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                carga = float(input("Ingrese los litros cargados: "))
                if carga > 0:
                    combustible_actual += carga
                else:
                    print("La carga debe ser un número positivo.")
            except ValueError:
                print("Entrada inválida.")
                
        elif opcion == "2":
            try:
                km = float(input("Ingrese los kilómetros recorridos en el viaje: "))
                if km > 0:
                    consumido = km * LITROS_POR_KM
                    if consumido <= combustible_actual:
                        combustible_actual -= consumido
                        print(f"Viaje completado. Se consumieron {consumido:.2f} litros.")
                    else:
                        print(" Error: No hay suficiente combustible para realizar este viaje.")
                else:
                    print("Los kilómetros deben ser mayores a 0.")
            except ValueError:
                print("Entrada inválida.")
                
        elif opcion == "3":
            print("Deteniendo el programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el ejercicio
if __name__ == "__main__":
    control_combustible_vehiculo()