import random, math
import csv

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]


sueldos = {}

def asignar_sueldos ():
    global sueldos
    trabajadores (random.randint(300000, 2500000) for trabajadores in trabajadores)
    print ("sueldos asignados correctamente")


def clasificar_sueldos ():
    if not sueldos:
        print("primero debes asignar los sueldos")
        return
    
menores_800k = {k: v for k, v in sueldos.items() if v < 800000}
entre_800k_2m = {k: v for k, v in sueldos.items() if 800000<= v <= 2000000}
mayores_2m = {k: v for k, v in sueldos.items() if v > 2000000}

total_sueldos= sum (sueldos.values())

print ("clasificacion de sueldos:")
print (f"menores a $800.000: {len(menores_800k)} trabajadores")
print (f"entre $800.000 y $2.000.000: {len(entre_800k_2m)} trabajadores")
print (f"mayores de $2.000.000: {len(mayores_2m)} trabajadores") 
print (f"total de sueldos: ${total_sueldos,}")

def ver_estadisticas():
    if not sueldos:
        print ("primero debes asignar los sueldos")
        return
    
sueldo_max = max (sueldos.values())
sueldo_min = min (sueldos.values())
sueldo_promedio = sum (sueldos.values()) / len(sueldos)

print ("estadisticas de sueldos:")
print (f"sueldo mas alto: $ {sueldo_max:,}")
print (f"sueldo mas bajo: $ {sueldo_min: ,}")
print (f"sueldo promedio: $ {sueldo_promedio:,.2f}")

def calcular_media_geometrica():
    if not sueldos:
        print ("primero debes asignar los sueldos:")
        return
producto_sueldos = math.prod(sueldos.values())
media_geometrica = producto_sueldos ** (1/len (sueldos))

print ("media geometrica de los sueldos:")
print (f"{media_geometrica:,.2f}")

def generar_reporte ():
    if not sueldos:
        print ("primero debes asignar los sueldos")
        return
    
    with open ("reporte_sueldos.csv", "w", newline="")as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["trabajador",  "sueldo base", "descuento salud(7%)", "descuento afp (12%)", "sueldo liquido"])

for trabajador, sueldo in sueldos.items ():
    salud = sueldo * 0.07
    afp = sueldo * 0.12
    suedlo_liquido = sueldo - (salud + afp)
    csv.writer.writerow([trabajador, sueldo, salud, afp, suedlo_liquido])

print ("datos exportados correctamente a 'reportes_sueldos.csv")

def exportar_csv():
    if not sueldos:
        print ("primero debes asignar los sueldos")
        return
    
    with open ("reporte_sueldos.csv", "w", newline="")as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["trabajador", "sueldo", "descuento salud (7%)" , "descuento afp (12%)", "sueldo liquido"])

for trabajador, sueldo in sueldos.items():
        salud = sueldo * 0.07
        afp = sueldo * 0.12
        suedlo_liquido = sueldo - (salud + afp)
        csv.writer([trabajador, sueldo, salud, afp, suedlo_liquido])


