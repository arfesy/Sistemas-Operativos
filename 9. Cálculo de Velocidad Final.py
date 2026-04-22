v_inicial = float(input("Velocidad inicial (m/s): "))
aceleracion = float(input("Aceleración (m/s^2): "))
tiempo = float(input("Tiempo (s): "))

# Vf = Vi + a * t
v_final = v_inicial + (aceleracion * tiempo)

print(f"La velocidad final es: {v_final} m/s")