def control_ejercicio():
    total_minutos = 0
    DIAS = 7
    
    print("--- Control de Ejercicio Semanal ---")
    for i in range(1, DIAS + 1):
        while True:
            try:
                minutos = int(input(f"Minutos de ejercicio del Día {i}: "))
                if minutos < 0:
                    print("Los minutos no pueden ser negativos.")
                    continue
                total_minutos += minutos
                break
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")
                
    promedio_diario = total_minutos / DIAS
    print(f"\nPromedio diario de ejercicio: {promedio_diario:.2f} minutos.")
    if promedio_diario < 30:
        print("💡 Sugerencia: Deberías aumentar la actividad física. Se recomiendan al menos 30 minutos diarios.")
    else:
        print("¡Buen trabajo! Cumples con los niveles de actividad física recomendados.")


if __name__ == "__main__":
    control_ejercicio()