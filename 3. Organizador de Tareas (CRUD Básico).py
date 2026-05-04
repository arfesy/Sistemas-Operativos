tareas = {}

def gestionar_tareas():
    while True:
        accion = input("\n[A]gregar, [U]pdate, [E]liminar, [V]er, [S]alir: ").upper()
        
        if accion == "A":
            nombre = input("Tarea: ")
            tareas[nombre] = "Pendiente"
        elif accion == "U":
            nombre = input("Nombre de la tarea a actualizar: ")
            if nombre in tareas:
                nuevo_estado = input("Nuevo estado (Pendiente/En progreso/Completada): ")
                tareas[nombre] = nuevo_estado
        elif accion == "V":
            for t, e in tareas.items():
                print(f"- {t}: {e}")
        elif accion == "S":
            break

gestionar_tareas()