import secrets
import string

def generar_password():
    longitud = int(input("Longitud de la contraseña: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    print(f"Tu nueva contraseña segura es: {password}")

generar_password()