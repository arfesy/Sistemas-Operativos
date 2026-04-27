print("-------------------------------------------------------")
print("Ejercicio 12: ÁREA DE UN TRIÁNGULO.")
print("-------------------------------------------------------")

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

s = (a + b + c) / 2 
area = (s * (s - a) * (s - b) * (s - c))**0.5

print("\nSALIDA: ")
print("-------------------------------------------------------")
print("El área es:", area)