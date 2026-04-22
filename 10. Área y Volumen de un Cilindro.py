import math

radio = float(input("Radio de la base: "))
altura = float(input("Altura del cilindro: "))

volumen = math.pi * pow(radio, 2) * altura
area_total = 2 * math.pi * radio * (radio + altura)

print(f"Volumen: {volumen:.2f}")
print(f"Área Total: {area_total:.2f}")