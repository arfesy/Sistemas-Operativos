def presupuesto():
    ingresos = float(input("Ingresos totales: $"))
    gastos = {}
    
    while True:
        cat = input("Categoría de gasto (o 'fin' para terminar): ")
        if cat.lower() == 'fin': break
        monto = float(input(f"Monto para {cat}: $"))
        gastos[cat] = monto

    total_gastos = sum(gastos.values())
    saldo = ingresos - total_gastos
    
    print(f"\nSaldo disponible: ${saldo:.2f}")
    for cat, monto in gastos.items():
        porcentaje = (monto / ingresos) * 100
        print(f"  > {cat}: {porcentaje:.1f}% del presupuesto")

presupuesto()