def serie_fibonacci_limite():
    print("--- Serie de Fibonacci (hasta valores <= 10.000) ---")
    
    
    a = 0
    b = 1
    
    print(a, end=" ")
    while b <= 10000:
        print(b, end=" ")
        
        siguiente = a + b
        a = b
        b = siguiente
    print()  

if __name__ == "__main__":
    serie_fibonacci_limite()