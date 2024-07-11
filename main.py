import funciones as fn

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

while True:
    print("Menu")
    print("1. Asignar Sueldos aleatorios")
    print("2. Clasificar Sueldos")
    print("3. Calcular Estadísticas")
    print("4. Generar Reporte en csv")
    print("5. Salir")

    try:
        opc = int(input("Seleccione Opcion: "))

        if opc == 1:
            sueldo_aleatorios = fn.asignar_sueldos(trabajadores)
        elif opc == 2:
            fn.clasificar_sueldos(sueldo_aleatorios)
        elif opc == 3:
            max_sueldo, min_sueldo, promedio, media_geometrica = fn.calcular_estadisticas(sueldo_aleatorios)
            if promedio is not None:
                print("Sueldo máximo: ", max_sueldo)
                print("Sueldo mínimo: ", min_sueldo)
                print("Promedio de sueldos: ", promedio)
                print("Media geométrica de sueldos:", media_geometrica)
        elif opc == 4:
            fn.generar_reporte(sueldo_aleatorios)
        elif opc == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Seleccione una opción del 1 al 5.")
    
    except ValueError:
        print("Opción debe ser un número del 1 al 5.")
