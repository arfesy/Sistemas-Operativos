def suma_digitos():
    print("--- Suma de los Dígitos ---")
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero >= 0:
                break
            print("El número debe ser positivo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
            
    numero_original = numero
    suma = 0
    
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero = numero // 10
        
    print(f"La suma de los dígitos de {numero_original} es: {suma}")

if __name__ == "__main__":
    suma_digitos()