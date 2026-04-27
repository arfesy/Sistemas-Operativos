print("-------------------------------------------------------")
print("Ejercicio 15: SUELDO BRUTO Y NETO.")
print("-------------------------------------------------------")


horas = float(input("Horas trabajadas: "))
costo = float(input("Costo por hora: "))

sueldo_bruto = horas * costo
descuento = sueldo_bruto * 0.10
sueldo_neto = sueldo_bruto - descuento

print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Sueldo Bruto:", sueldo_bruto)
print("Sueldo Neto:", sueldo_neto)