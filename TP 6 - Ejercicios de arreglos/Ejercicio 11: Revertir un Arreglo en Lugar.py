def revertir_en_lugar(arreglo):
    izquierda = 0
    derecha = len(arreglo) - 1
    
    while izquierda < derecha:
        # Intercambio de valores sin estructuras auxiliares
        arreglo[izquierda], arreglo[derecha] = arreglo[derecha], arreglo[izquierda]
        izquierda += 1
        derecha -= 1
    return arreglo

# Ejemplo de uso
mi_arreglo = [10, 20, 30, 40, 50]
print("Arreglo original:", mi_arreglo)
revertir_en_lugar(mi_arreglo)
print("Arreglo revertido (en lugar):", mi_arreglo)