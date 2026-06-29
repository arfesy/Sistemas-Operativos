def segundo_mayor(arreglo):
    if len(arreglo) < 2:
        return None
    
    mayor = segundo = float('-inf')
    for numero in arreglo:
        if numero > mayor:
            segundo = mayor
            mayor = numero
        elif numero > segundo and numero != mayor:
            segundo = numero
            
    return segundo if segundo != float('-inf') else None

# Ejemplo de uso
mi_arreglo = [12, 35, 1, 10, 34, 1]
print("Arreglo:", mi_arreglo)
print("Segundo mayor elemento:", segundo_mayor(mi_arreglo))