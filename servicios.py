def agregar_producto(lista:list):
    # Validacion si se ingresa algun int 
    valor_str = False
    while valor_str == False: # Mientras lo que se ingrese sea un str
        nombre_producto = input("Nombre del producto: ").strip().lower()
        if nombre_producto.isalpha(): # si todos los caracteres son str
            valor_str = True
        elif nombre_producto.replace(" ", "").isalpha(): # si hay un espacio en el nombre como platano verde
            valor_str = True
        else:
            print("Error. Ingresa el nombre correcto del producto")

    # Si el usuario ingresa un valor inválido de precio o cantidad, muestra un mensaje y vuelve a pedirlo. 
    valor_precio = False
    while valor_precio == False:
        try:
            precio = float(input("Precio del producto: $ ")) 
            if precio < 0: # si se ingresa un valor negativo
                print("\nEl precio no puede ser negativo\n")
            else:
                valor_precio = True # Si funciona -> salir del ciclo
        except:
            print("\nError. Ingresa el valor de numero correcto para el precio\n") # Si falla -> mostrar error y volver a preguntar

    valor_cantidad = False
    while valor_cantidad == False:
        try:
            cantidad = int(input("Cantidad de Producto: "))
            if cantidad < 0: # si se ingresa un valor negativo
                print("\nLa cantidad no puede ser negativa\n")
            else:
                valor_cantidad = True
        except:
            print("\nError. Ingresa el valor de numero correcto para la cantidad\n")

    producto = {"nombre":nombre_producto,
                "precio":precio,
                "cantidad":cantidad}
    lista.append(producto)

    return lista

def mostrar_inventario(lista:list):
    if len(lista) == 0:
        print("\nEl inventario esta vacio")
    else:
        for i in lista:
            print("Nombre:", i["nombre"],"| Precio: $", i["precio"],"| Cantidad:", i["cantidad"])


def buscar_producto(lista:list):
    busqueda_prod = input("Nombre del producto: ").strip().lower()
    resultado = None

    if len(lista) == 0:
        print("\nEl inventario esta vacio")
    else:
        for dict in lista:
            if dict["nombre"] == busqueda_prod:
                resultado = dict
    
    if resultado:
            print(resultado)
    else:
        print("No encontrado")

def actualizar_producto(lista:list):
    busqueda_prod = input("Nombre del producto a cambiar: ").strip().lower()
    encontrado = False # variable para identificar si el prod es encontrado o no
    if len(lista) == 0:
        print("\nEl inventario esta vacio\n")
    else:
        for producto in lista:

            if producto["nombre"] == busqueda_prod:

                valor_str = False
                while valor_str == False:
                    nuevo_nombre = input("Nuevo nombre (Enter para dejar igual): ").strip().lower()
                    if nuevo_nombre == "":
                        valor_str = True
                
                    elif nuevo_nombre.replace(" ", "").isalpha(): # si hay un espacio en el nombre como platano verde
                        producto["nombre"] = nuevo_nombre
                        valor_str = True
                    else:
                        print("Error. Ingresa el nombre correcto del producto")


                valor_precio = False
                while valor_precio == False:
                    nuevo_precio = input("Nuevo precio (Enter para dejar igual): $ ")
                    if nuevo_precio == "":
                        valor_precio = True  

                    else:
                        try:
                            precio_num = float(nuevo_precio)
                            if precio_num < 0: # si se ingresa un valor negativo
                                print("\nEl precio no puede ser negativo\n")
                            
                            else:
                                producto["precio"] = precio_num
                                valor_precio = True
                        except:
                            print("\nError. Ingresa el valor de numero correcto para el precio\n")
                    
                valor_cantidad = False
                while valor_cantidad == False:
                    nuevo_cantidad = input("Nueva cantidad  (Enter para dejar igual): ")
                    if nuevo_cantidad == "":
                        valor_cantidad = True

                    else:
                        try:
                            cantidad_num = int(nuevo_cantidad)
                            if cantidad_num < 0: # si se ingresa un valor negativo
                                print("\nLa cantidad no puede ser negativa\n")
                            
                            else:
                                producto["cantidad"] = cantidad_num
                                valor_cantidad = True
                        except:
                            print("\nError. Ingresa el valor de numero correcto para la cantidad\n")

                encontrado = True

    if encontrado:
        print("Producto actualizado")
    else:
        print("Producto no encontrado")

    return lista

def eliminar_producto(lista:list):
    busqueda_prod = input("Nombre del producto a eliminar: ").strip().lower()
    encontrado = False

    for producto in lista:
        if producto["nombre"] == busqueda_prod:
            lista.remove(producto)
            encontrado = True
    if encontrado:
        print("Producto eliminado")
    else:
        print("Producto no encontrado")

    return lista


def calcular_estadistica(lista:list):
    total = 0
    cantidad_productos = len(lista)
    for i in lista:
        total += (i["precio"] * i["cantidad"])
    print("\nCantidad total de productos:", cantidad_productos,"| Valor total del inventario: $", total)