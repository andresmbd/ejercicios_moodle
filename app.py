import servicios, archivos

inventario = []
accion = ""

while accion != "0":
    accion = input("\nQue accion desea realizar:\n"
    "0- Salir\n" \
    "1- Agregar producto\n" \
    "2- Mostrar inventario\n" \
    "3- Calcular estadísticas\n" \
    "4- Buscar producto\n" \
    "5- Actualizar producto\n" \
    "6- Eliminar producto\n" \
    "7- Guardar CSV\n" \
    "8- Cargar CSV\n" \
    "-> ")
    

    
    if accion == "1": 
        inventario = servicios.agregar_producto(inventario)   

    elif accion == "2":
        servicios.mostrar_inventario(inventario)
        

    elif accion == "3":
        servicios.calcular_estadistica(inventario)

    elif accion == "4":
        servicios.buscar_producto(inventario)

    elif accion == "5":
        inventario = servicios.actualizar_producto(inventario)

    elif accion == "6":
        inventario = servicios.eliminar_producto(inventario)

    elif accion == "7":
        archivo =input("nombre del archivo a guardar más la extensión (.cvs): ").strip().lower()
        ruta = "./data/" + archivo
        archivos.guardar_csv(inventario, ruta)

    elif accion == "8":
        archivo = input("nombre del archivo: ").strip().lower()
        ruta = "./data/" + archivo

        nuevos_datos = archivos.cargar_csv(ruta)

        if len(nuevos_datos) > 0:
            opcion = input("1- Sobrescribir | 2- Fusionar: ")

            if opcion == "1":
                inventario = nuevos_datos

            elif opcion == "2":
                inventario = inventario + nuevos_datos

            else:
                print("Opción inválida")

    elif accion == "0":
        print("\nA la orden")

    else:
        print("\nOpción invalida elija un numero")


    

# El programa pide eleccion al usuario sobre el menu; 
# si hay un ValueError la iteracion continua hasta poner 
# el valor correcto para que se calcule precio total del producto y se 
# imprima junto con la informacion obtenida; se imprime lo que el usuario 
# vaya almacenando en el inventario; se calcula el total del acumulado de 
# precios y cantidades asi como se muestra las cantidades de productos; 
# el progrmaam sigue si una opcion es invalida o se detendra hasta que el 
# usuario elija "4" de salir.