# TP3 - Ejercicios de Recursividad / Lógica
# Alumno: Giuliano Valentino

import random

def calcular_promedio_notas():
    print("--- Ejercicio 1: Promedio de Notas ---")
    notas = []
    for i in range(1, 6):
        while True:
            try:
                nota = float(input(f"Ingrese la nota del alumno {i}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Por favor, ingrese una nota válida entre 0 y 10.")
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
    
    promedio = sum(notas) / len(notas)
    print(f"El promedio de las notas es: {promedio:.2f}")
    if promedio > 7:
        print("¡El promedio supera 7!")

def clasificar_edades():
    print("\n--- Ejercicio 2: Clasificar Edades ---")
    ninos = 0
    adolescentes = 0
    adultos = 0
    
    while True:
        try:
            edad = int(input("Ingrese una edad (0 para terminar): "))
            if edad == 0:
                break
            elif edad < 0:
                print("Por favor, ingrese una edad válida.")
                continue
            
            if edad < 13:
                ninos += 1
            elif 13 <= edad <= 17:
                adolescentes += 1
            else:
                adultos += 1
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
            
    print(f"Clasificación:\nNiños (<13): {ninos}\nAdolescentes (13-17): {adolescentes}\nAdultos (18+): {adultos}")

# 3. Simular compra en supermercado
def simular_compra():
    print("\n--- Ejercicio 3: Simular Compra ---")
    total = 0.0
    while True:
        try:
            precio = float(input("Ingrese el precio del producto (0 para terminar): "))
            if precio == 0:
                break
            elif precio < 0:
                print("El precio no puede ser negativo.")
                continue
            total += precio
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
            
    print(f"Total inicial: ${total:.2f}")
    if total > 10000:
        descuento = total * 0.10
        total -= descuento
        print(f"Se aplicó un 10% de descuento (${descuento:.2f}). Total con descuento: ${total:.2f}")

def adivinar_numero_secreto():
    print("\n--- Ejercicio 4: Número Secreto ---")
    numero_secreto = random.randint(1, 10)
    intentos = 3
    
    while intentos > 0:
        try:
            posible_numero = int(input(f"Adivine el número del 1 al 10 (Intentos restantes: {intentos}): "))
            if posible_numero == numero_secreto:
                print("¡Felicidades! Has adivinado el número secreto.")
                return
            else:
                print("Número incorrecto.")
                intentos -= 1
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            
    print(f"Lo siento, te has quedado sin intentos. El número era {numero_secreto}.")

def es_primo():
    print("\n--- Ejercicio 5: Determinar si es Primo ---")
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero <= 1:
            print(f"El número {numero} no es primo.")
            return
        
        primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                primo = False
                break
                
        if primo:
            print(f"El número {numero} es primo.")
        else:
            print(f"El número {numero} no es primo.")
    except ValueError:
        print("Entrada inválida.")

def validar_contrasena():
    print("\n--- Ejercicio 6: Validar Contraseña ---")
    CONTRASENA_CORRECTA = "admin123"
    intentos = 3
    
    while intentos > 0:
        ingreso = input(f"Ingrese la contraseña (Intentos restantes: {intentos}): ")
        if ingreso == CONTRASENA_CORRECTA:
            print("Acceso concedido.")
            return
        else:
            print("Contraseña incorrecta.")
            intentos -= 1
            
    print("Acceso bloqueado tras 3 intentos fallidos.")

def promedio_positivos_negativos():
    print("\n--- Ejercicio 7: Promedio de Positivos y Negativos ---")
    positivos = []
    negativos = []
    
    for i in range(1, 11):
        while True:
            try:
                num = float(input(f"Ingrese el número {i} de 10: "))
                if num > 0:
                    positivos.append(num)
                elif num < 0:
                    negativos.append(num)
                break
            except ValueError:
                print("Entrada inválida.")
                
    if positivos:
        print(f"Promedio de positivos: {sum(positivos)/len(positivos):.2f} (Cantidad: {len(positivos)})")
    else:
        print("No se ingresaron números positivos.")
        
    if negativos:
        print(f"Promedio de negativos: {sum(negativos)/len(negativos):.2f} (Cantidad: {len(negativos)})")
    else:
        print("No se ingresaron números negativos.")

def determinar_pares():
    print("\n--- Ejercicio 8: Determinar si hay Pares ---")
    hay_par = False
    for i in range(1, 6):
        while True:
            try:
                num = int(input(f"Ingrese el número entero {i} de 5: "))
                if num % 2 == 0:
                    hay_par = True
                break
            except ValueError:
                print("Entrada inválida.")
                
    if hay_par:
        print("Al menos uno de los números ingresados es par.")
    else:
        print("Ninguno de los números ingresados es par.")

def contador_temperaturas():
    print("\n--- Ejercicio 9: Contador de Temperaturas ---")
    menores_cero = 0
    mayores_treinta = 0
    
    while True:
        try:
            temp = float(input("Ingrese una temperatura (ingrese -100 para salir): "))
            if temp == -100:
                break
            if temp < 0:
                menores_cero += 1
            elif temp >= 30:
                mayores_treinta += 1
        except ValueError:
            print("Entrada inválida.")
            
    print(f"Resultados:\nTemperaturas menores a 0: {menores_cero}\nTemperaturas mayores o iguales a 30: {mayores_treinta}")

def simular_menu():
    print("\n--- Ejercicio 10: Menú de Opciones ---")
    while True:  
        print("\nMENÚ PRINCIPAL")
        print("1. Saludar")
        print("2. Mostrar créditos")
        print("3. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            print("¡Hola! Esperamos que tengas un gran día.")
        elif opcion == "2":
            print("Desarrollado para el TP3.")
        elif opcion == "3" or opcion.lower() == "salir":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def ejecutar_tp3():
    
    print("  TP3 - TRABAJO PRÁCTICO RESUELTO        ")
    
    calcular_promedio_notas()
    clasificar_edades()
    simular_compra()
    adivinar_numero_secreto()
    es_primo()
    validar_contrasena()
    promedio_positivos_negativos()
    determinar_pares()
    contador_temperaturas()
    simular_menu()

if __name__ == "__main__":
    ejecutar_tp3()
