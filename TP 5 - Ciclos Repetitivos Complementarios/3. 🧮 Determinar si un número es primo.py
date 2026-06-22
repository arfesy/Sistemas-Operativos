def es_primo():
    print("--- Verificador de Números Primos ---")
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
            
    if numero <= 1:
        primo = False
    else:
        primo = True
        
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                primo = False
                break
                
    if primo:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")

if __name__ == "__main__":
    es_primo()