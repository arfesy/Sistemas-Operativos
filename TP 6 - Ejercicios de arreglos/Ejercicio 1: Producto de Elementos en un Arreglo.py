def producto_arreglo(arreglo):
    if not arreglo:
        return 0
    resultado = 1
    for numero in arreglo:
        resultado *= numero
    return resultado

# Ejemplo de uso
mi_arreglo = [2, 3, 4, 5]
print("Arreglo:", mi_arreglo)
print("Producto de los elementos:", producto_arreglo(mi_arreglo))