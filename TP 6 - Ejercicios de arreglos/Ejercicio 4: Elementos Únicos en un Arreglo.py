def elementos_unicos(arreglo):
    unicos = []
    for numero in arreglo:
        if arreglo.count(numero) == 1:
            unicos.append(numero)
    return unicos

# Ejemplo de uso
mi_arreglo = [4, 5, 4, 6, 7, 5, 8, 9]
print("Arreglo:", mi_arreglo)
print("Elementos únicos (que no se repiten):", elementos_unicos(mi_arreglo))