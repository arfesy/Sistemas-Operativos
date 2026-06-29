def sumar_correspondientes(arreglo1, arreglo2):
    if len(arreglo1) != len(arreglo2):
        return None # Deben tener la misma longitud
    
    resultado = []
    for i in range(len(arreglo1)):
        resultado.append(arreglo1[i] + arreglo2[i])
    return resultado

# Ejemplo de uso
a1 = [1, 2, 3, 4]
a2 = [5, 6, 7, 8]
print("Arreglo 1:", a1)
print("Arreglo 2:", a2)
print("Suma de elementos correspondientes:", sumar_correspondientes(a1, a2))