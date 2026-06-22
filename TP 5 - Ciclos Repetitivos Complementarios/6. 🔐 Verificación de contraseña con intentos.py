def verificar_contrasena():
    CONTRASENA_CORRECTA = "secure2026"
    intentos_maximos = 3
    intentos_realizados = 0
    
    print("--- Sistema de Autenticación ---")
    while intentos_realizados < intentos_maximos:
        intentos_restantes = intentos_maximos - intentos_realizados
        password_ingresada = input(f"Ingrese su contraseña (Intentos restantes: {intentos_restantes}): ")
        intentos_realizados += 1
        
        if password_ingresada == CONTRASENA_CORRECTA:
            print(" Acceso concedido. ¡Bienvenido!")
            return
        else:
            print(" Contraseña incorrecta.")
            
    print("\n🔒 Acceso bloqueado tras 3 intentos fallidos.")

if __name__ == "__main__":
    verificar_contrasena()