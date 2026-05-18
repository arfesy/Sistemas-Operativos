import time

print("--- SIMULACIÓN DE RELOJ DIGITAL ---")
print("Presione Ctrl+C para detener la simulación de las 24 horas.\n")

try:
    for hora in range(24):
        for minuto in range(60):
            for segundo in range(60):
                # El formato :02d asegura que siempre se muestren dos dígitos
                print(f"{hora:02d}:{minuto:02d}:{segundo:02d}", end="\r")
                time.sleep(0.01) # Velocidad acelerada para demostración
except KeyboardInterrupt:
    print("\nSimulación interrumpida por el usuario.")