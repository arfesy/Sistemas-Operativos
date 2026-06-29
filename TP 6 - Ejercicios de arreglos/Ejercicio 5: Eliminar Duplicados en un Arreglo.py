def eliminar_duplicados(arreglo):
    resultado = []
    for numero in arreglo:
        if numero not in resultado:
            resultado.append(numero)
    return resultado

# Ejemplo de uso
mi_arreglo = [1, 2, 2, 3, 4, 4, 5, 1]
print("Arreglo original:", mi_arreglo)
print("Arreglo sin duplicados:", eliminar_duplicados(mi_arreglo))