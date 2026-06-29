def contar_pares(arreglo):
    contador = 0
    for numero in arreglo:
        if numero % 2 == 0:
            contador += 1
    return contador

# Ejemplo de uso
mi_arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Arreglo:", mi_arreglo)
print("Cantidad de números pares:", contar_pares(mi_arreglo))