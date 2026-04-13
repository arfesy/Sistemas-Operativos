print("-------------------------------------------------------")
print("Ejercicio10: CALCULAR ÁREA Y VOLUMEN DEL CILINDRO.")
print("-------------------------------------------------------")
PI = 3.1416
print("Ingrese Radio y Alto: ")
radio = float( input("Radio: "))
alto = float ( input("Alto: "))
vol = PI * radio**2 * alto
are = 2*PI*radio*(radio + alto)
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Volumen:", vol)
print("área:", are)