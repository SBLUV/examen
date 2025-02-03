def menu ():

    opcion= [
    1: "asignar_sueldos",
    2: "clasificar_sueldos",
    3: "ver_estadisticas",
    4: "calcular_media_geometrica",
    5: "generar_reporte",
    6: "exportar_csv",
    7: "salir"
]

    while True:
        print ("menu principal")
        print ("1.asignar_sueldos")
        print ("2.clasificar_sueldos")
        print ("3.ver_estadisticas")
        print ("4.calcular_media_geometrica")
        print ("5.generar_reporte")
        print ("6.exportar_csv")
        print ("7.salir")

        opcion = input ("seleccione una opcion:")

        if opcion == 1:
            print ("asignar sueldos")
        elif opcion == 2:
            print ("clasificar sueldos")
        elif opcion == 3:
            print ("ver estadisticas")
        elif opcion == 4:
            print ("calcular media geometrica")
        elif opcion == 5:
            print ("generar reporte")
        elif opcion == 6:
            print ("exportar csv")
        elif opcion == 7:
            print+ ("saliendo..")
            break

    menu()