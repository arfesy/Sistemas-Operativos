dolares = float(input("Cantidad de dólares: "))
tipo_cambio = float(input("Precio del dólar hoy: "))

pesos = dolares * tipo_cambio

print(f"Equivale a: ${pesos:.2f} pesos")