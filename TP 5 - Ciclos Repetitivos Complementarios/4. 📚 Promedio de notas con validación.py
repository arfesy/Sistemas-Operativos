def promedio_notas_validacion():
    suma_notas = 0.0
    notas_validas = 0
    fuera_de_rango = 0
    BANDERA_SALIDA = -1
    
    print("--- Promedio de Notas con Validación ---")
    while True:
        try:
            nota = float(input(f"Ingrese una nota (o {BANDERA_SALIDA} para salir): "))
            if nota == BANDERA_SALIDA:
                break
                
            if 1 <= nota <= 10:
                suma_notas += nota
                notas_validas += 1
            else:
                print("⚠️ Nota fuera del rango permitido (debe ser entre 1 y 10).")
                fuera_de_rango += 1
        except ValueError:
            print("Entrada inválida. Por favor ingrese una nota numérica.")
            
    print(f"\n--- Resumen ---")
    if notas_validas > 0:
        promedio = suma_notas / notas_validas
        print(f"- Promedio de notas válidas: {promedio:.2f}")
        print(f"- Cantidad de notas válidas ingresadas: {notas_validas}")
    else:
        print("- No se ingresaron notas válidas para promediar.")
    print(f"- Cantidad de notas fuera de rango: {fuera_de_rango}")

if __name__ == "__main__":
    promedio_notas_validacion()