import math

lado = float(input("Ingrese la medida del lado: "))
# Fórmula: (3 * sqrt(3) * lado^2) / 2
area = (3 * math.sqrt(3) * pow(lado, 2)) / 2

print(f"El área del hexágono es: {area:.2f}")