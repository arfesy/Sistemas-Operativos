def esta_ordenado(arreglo):
    for i in range(len(arreglo) - 1):
        if arreglo[i] > arreglo[i + 1]:
            return False # Si el actual es mayor que el siguiente, no está ordenado ascendentemente
    return True

# Ejemplo de uso
arreglo_a = [1, 2, 5, 7, 10]
arreglo_b = [1, 5, 3, 7, 2]
print(f"¿El arreglo {arreglo_a} está ordenado?:", esta_ordenado(arreglo_a))
print(f"¿El arreglo {arreglo_b} está ordenado?:", esta_ordenado(arreglo_b))