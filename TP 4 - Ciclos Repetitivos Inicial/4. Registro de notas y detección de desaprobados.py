def registro_notas():
    aprobados = 0
    desaprobados = 0
    ALUMNOS = 10
    
    print("--- Registro de Notas de Alumnos ---")
    for i in range(1, ALUMNOS + 1):
        while True:
            try:
                nota = float(input(f"Ingrese la nota del alumno {i} de 10: "))
                if 0 <= nota <= 10:
                    if nota >= 6:
                        aprobados += 1
                    else:
                        desaprobados += 1
                    break
                else:
                    print("La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Entrada inválida. Ingrese un número válido.")
                
    print(f"\n--- Resultados Finales ---")
    print(f"- Alumnos aprobados (nota >= 6): {aprobados}")
    print(f"- Alumnos desaprobados: {desaprobados}")


if __name__ == "__main__":
    registro_notas()