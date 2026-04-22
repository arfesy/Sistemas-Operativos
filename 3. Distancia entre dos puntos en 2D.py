import math

x1, y1 = float(input("x1: ")), float(input("y1: "))
x2, y2 = float(input("x2: ")), float(input("y2: "))

# Teorema de Pitágoras aplicado a coordenadas
distancia = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print(f"La distancia entre los puntos es: {distancia:.2f}")