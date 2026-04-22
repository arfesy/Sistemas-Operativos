seg_totales = int(input("Ingrese cantidad de segundos: "))

horas = seg_totales // 3600
minutos = (seg_totales % 3600) // 60
segundos = seg_totales % 60

print(f"{horas}h : {minutos}m : {segundos}s")