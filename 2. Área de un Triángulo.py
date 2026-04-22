import math

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

# Calculamos el semiperímetro
p = (a + b + c) / 2
# Aplicamos la fórmula de Herón
area = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f"El área del triángulo es: {area:.2f}")