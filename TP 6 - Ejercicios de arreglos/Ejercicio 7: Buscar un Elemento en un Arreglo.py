def buscar_elemento(arreglo, numero_buscado):
    for numero in arreglo:
        if numero == numero_buscado:
            return True
    return False

# Ejemplo de uso
mi_arreglo = [10, 23, 45, 70, 11, 15]
buscado = 70
print("Arreglo:", mi_arreglo)
print(f"¿Está el número {buscado} presente?:", buscar_elemento(mi_arreglo, buscado))