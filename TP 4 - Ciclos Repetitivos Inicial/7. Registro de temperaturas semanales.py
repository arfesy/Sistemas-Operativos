def temperaturas_semanales():
    DIAS = 7
    temperaturas = []
    dias_calurosos = 0
    
    print("--- Registro de Temperaturas Semanales ---")
    for i in range(1, DIAS + 1):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura máxima del Día {i}: "))
                temperaturas.append(temp)
                if temp > 30:
                    dias_calurosos += 1
                break
            except ValueError:
                print("Entrada inválida. Ingrese un valor numérico.")
                
    media_temperatura = sum(temperaturas) / DIAS
    print(f"\n--- Resultados de la Semana ---")
    print(f"- Temperatura media: {media_temperatura:.2f}°C")
    print(f"- Cantidad de días que superaron los 30°C: {dias_calurosos}")


if __name__ == "__main__":
    temperaturas_semanales()