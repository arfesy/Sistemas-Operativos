def rotar_derecha(arreglo):
    if not arreglo:
        return arreglo
    
    ultimo = arreglo[-1] # Guardamos el último elemento
    
    # Desplazamos los elementos hacia la derecha
    for i in range(len(arreglo) - 1, 0, -1):
        arreglo[i] = arreglo[i - 1]
        
    arreglo[0] = ultimo # Colocamos el último en la primera posición
    return arreglo

# Ejemplo de uso
mi_arreglo = [1, 2, 3, 4, 5]
print("Arreglo original:", mi_arreglo)
print("Arreglo rotado a la derecha:", rotar_derecha(mi_arreglo.copy()))