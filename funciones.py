import random
import csv
import statistics

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"] 


def asignar_sueldos(trabajadores):
    sueldo_aleatorios = {}
    for trabajador in trabajadores:
        sueldo = random.randint(800000, 2500000)
        sueldo_aleatorios[trabajador] = sueldo
    return sueldo_aleatorios


def clasificar_sueldos(sueldo_aleatorios):
    menor_a_800 = {}
    entre_800k_2m = {}
    superior_2m = {}
    
    for trabajador, sueldo in sueldo_aleatorios.items():
        if sueldo < 800000:
            menor_a_800[trabajador] = sueldo
        elif 800000 < sueldo < 2000000:
            entre_800k_2m[trabajador] = sueldo
        elif sueldo >= 2000000:
            superior_2m[trabajador] = sueldo
    
    print("Sueldos menores a $800.000:", len(menor_a_800))
    for trabajador, sueldo in menor_a_800.items():
        print(trabajador, ": $", sueldo)
    
    print("Sueldos entre 800.000 y 2.000.000:", len(entre_800k_2m))
    for trabajador, sueldo in entre_800k_2m.items():
        print(trabajador, ": $", sueldo)
    
    print("Sueldos superiores a 2.000.000:", len(superior_2m))
    for trabajador, sueldo in superior_2m.items():
        print(trabajador, ": $", sueldo)



def calcular_estadisticas(sueldo_aleatorios):
    sueldos = list(sueldo_aleatorios.values())

    if not sueldos:
        print("No hay sueldos asignados")
        return None, None, None, None

    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    promedio = sum(sueldos) / len(sueldos)
    media_geometrica = statistics.geometric_mean(sueldos)
    return max_sueldo, min_sueldo, promedio, media_geometrica



def generar_reporte(sueldo_aleatorios):
    with open("reportes_sueldos.csv", "w", newline="") as archivo:
        reporte = csv.writer(archivo, delimiter=",")
        reporte.writerow(["Nombre Trabajador", "Sueldo"])
        for trabajador, sueldo in sueldo_aleatorios.items():
            reporte.writerow([trabajador, sueldo])
        print("Reporte generado con éxito")

