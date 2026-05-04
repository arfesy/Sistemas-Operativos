def calculadora_propinas():
    cuenta = float(input("Total de la cuenta: $"))
    porcentaje = float(input("Porcentaje de propina (ej. 10, 15, 20): "))
    
    propina = cuenta * (porcentaje / 100)
    total = cuenta + propina
    
    print(f"\nResumen:")
    print(f"Propina: ${propina:.2f}")
    print(f"Total a pagar: ${total:.2f}")

calculadora_propinas()