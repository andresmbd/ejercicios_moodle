
inventario = []
accion = ""

nombre = "" # nombre del producto
precio = 0 # precio del producto
cantidad = 0 # cantidad del producto
fin_inven = len(inventario) 

def agregar_producto(nombre_producto:str,precio:float,cantidad:int,lista:list):
    nombre_producto = input("Nombre del producto: ")
    # Si el usuario ingresa un valor inválido de precio o cantidad, muestra un mensaje y vuelve a pedirlo. 
    valor_precio = False
    while valor_precio == False:
        try:
            precio = float(input("Precio del producto: $ ")) 
            valor_precio = True # Si funciona -> salir del ciclo
        except:
            print("Error. Ingresa el valor de numero correcto para el precio") # Si falla -> mostrar error y volver a preguntar

    valor_cantidad = False
    while valor_cantidad == False:
        try:
            cantidad = int(input("Cantidad de Producto: "))
            valor_cantidad = True
        except:
            print("Error. Ingresa el valor de numero correcto para la cantidad")

    producto = {"nombre":nombre_producto,
                "precio":precio,
                "cantidad":cantidad}
    lista.append(producto)

def mostrar_inventario(lista:list):
    if len(lista) == 0:
        print("\nEl inventario esta vacio")
    else:
        for i in lista:
            print("Nombre:", i["nombre"],"| Precio: $", i["precio"],"| Cantidad:", i["cantidad"])

def calcular_estadistica(lista:list):
    total = 0
    cantidad_productos = len(lista)
    for i in lista:
        total += (i["precio"] * i["cantidad"])
    print("\nCantidad total de productos:", cantidad_productos,"| Valor total del inventario: $", total)

while accion != "4":
    accion = input("\nQue accion desea realizar:\n" \
    "1- Agregar producto\n" \
    "2- Mostrar inventario\n" \
    "3- Calcular estadísticas\n" \
    "4- Salir\n" \
    "-> ").lower()
    

    
    if accion == "1": 
        agregar_producto(nombre, precio, cantidad, inventario)   

    elif accion == "2":
        mostrar_inventario(inventario)
        

    elif accion == "3":
        calcular_estadistica(inventario)

    elif accion == "4":
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