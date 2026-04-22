parcial1 = float(input("Nota Parcial 1 (30%): "))
parcial2 = float(input("Nota Parcial 2 (30%): "))
examen_final = float(input("Nota Examen Final (40%): "))

nota_final = (parcial1 * 0.3) + (parcial2 * 0.3) + (examen_final * 0.4)

print(f"La calificación final es: {nota_final}")