def seguimiento_actividad():
    DIAS_SEMANA = 7
    minutos_por_dia = []
    total_minutos = 0
    
    print("--- Seguimiento de Actividad Física Semanal ---")
    for i in range(1, DIAS_SEMANA + 1):
        while True:
            try:
                minutos = int(input(f"Ingrese los minutos de ejercicio del Día {i}: "))
                if minutos < 0:
                    print("Los minutos no pueden ser negativos.")
                    continue
                minutos_por_dia.append(minutos)
                total_minutos += minutos
                break
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")
                

    max_actividad = minutos_por_dia[0]
    min_actividad = minutos_por_dia[0]
    dia_max = 1
    dia_min = 1
    
    for indice in range(1, len(minutos_por_dia)):
        if minutos_por_dia[indice] > max_actividad:
            max_actividad = minutos_por_dia[indice]
            dia_max = indice + 1
        if minutos_por_dia[indice] < min_actividad:
            min_actividad = minutos_por_dia[indice]
            dia_min = indice + 1
            
    promedio_semanal = total_minutos / DIAS_SEMANA
    
    print(f"\n--- Resumen de la Actividad ---")
    print(f"- Promedio semanal: {promedio_semanal:.2f} minutos/día")
    print(f"- Día de mayor actividad: Día {dia_max} ({max_actividad} minutos)")
    print(f"- Día de menor actividad: Día {dia_min} ({min_actividad} minutos)")

if __name__ == "__main__":
    seguimiento_actividad()