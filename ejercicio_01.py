print("--- PROMEDIO DE 7 CALIFICACIONES ---")
suma_calificaciones = 0

for i in range(1, 8):
    calificacion = float(input(f"Ingrese la calificación {i}: "))
    suma_calificaciones += calificacion

promedio = suma_calificaciones / 7
print(f"\nEl promedio final del alumno es: {promedio:.2f}")