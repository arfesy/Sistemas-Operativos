def encontrar_indice(arreglo, numero_buscado):
    for i in range(len(arreglo)):
        if arreglo[i] == numero_buscado:
            return i # Retorna el índice de la primera aparición
    return -1 # Retorna -1 si no se encuentra

# Ejemplo de uso
mi_arreglo = [20, 40, 50, 40, 60]
buscado = 40
print("Arreglo:", mi_arreglo)
print(f"Índice de la primera aparición de {buscado}:", encontrar_indice(mi_arreglo, buscado))