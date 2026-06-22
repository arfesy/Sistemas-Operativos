def seguimiento_agua():
    total_vasos = 0
    DIAS_SEMANA = 7
    
    print("--- Seguimiento de Hábitos Saludables (Agua) ---")
    for i in range(1, DIAS_SEMANA + 1):
        while True:
            try:
                vasos = int(input(f"Vasos de agua tomados el Día {i}: "))
                if vasos < 0:
                    print("La cantidad de vasos no puede ser negativa.")
                    continue
                total_vasos += vasos
                break
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
                
    promedio_diario = total_vasos / DIAS_SEMANA
    print(f"\nTu promedio diario de consumo de agua es de {promedio_diario:.2f} vasos.")
    if promedio_diario < 8:
        print(" Recomendación: Deberías aumentar el consumo de agua. Lo ideal son al menos 8 vasos al día.")
    else:
        print("¡Excelente! Mantienes una hidratación adecuada.")


if __name__ == "__main__":
    seguimiento_agua()