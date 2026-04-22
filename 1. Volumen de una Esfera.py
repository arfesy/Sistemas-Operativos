import math

radio = float(input("Ingrese el radio de la esfera: "))
# Fórmula: (4/3) * PI * radio^3
volumen = (4/3) * math.pi * pow(radio, 3)

print(f"El volumen de la esfera es: {volumen:.2f}")