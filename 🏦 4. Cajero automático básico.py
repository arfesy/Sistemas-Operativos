try:
    saldo = float(input("Ingrese su saldo actual: $"))
    monto_a_retirar = float(input("Ingrese el monto que desea retirar: $"))

    if monto_a_retirar > 0 and monto_a_retirar <= saldo:
        saldo -= monto_a_retirar
        print(f"Operación exitosa. Ha retirado: ${monto_a_retirar}")
        print(f"Su saldo restante es: ${saldo}")
    elif monto_a_retirar > saldo:
        print("Error: Fondos insuficientes.")
    else:
        print("Error: El monto a retirar debe ser mayor a 0.")
except ValueError:
    print("Error: Ingrese valores numéricos válidos.")