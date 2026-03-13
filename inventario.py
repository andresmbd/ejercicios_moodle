# Solicitar dato al usuario
nombre = input("Nombre del producto: ")

# Si el usuario ingresa un valor inválido de precio o cantidad, muestra un mensaje y vuelve a pedirlo. 
valor_precio = False
while valor_precio == False:
    try:
        precio = float(input("Precio del producto: ")) 
        valor_precio = True # Si funciona -> salir del ciclo

    except:
        print("Error. Ingresa el valor de numero correcto para el precio") # Si falla -> mostrar error y volver a preguntar
valor_cantidad = False

while valor_cantidad == False:
    try:
        cantidad = int(input("Cantidad de Producto: "))
        valor_cantidad = True

    except:
        print("Error. Ingresa el valor de numero correcsto para la cantidad")

# Calculo del producto e impresion del desgloze de la info del producto en la terminal
costo_total = precio * cantidad
print(f"Nombre del Producto: {nombre} | Precio: $ {precio:.2f} | Cantidad: {cantidad} | Total: $ {costo_total:.2f}")

# El programa pide informacion al usuario del nombre, precio, cantidad 
# del producto; si hay un ValueError la iteracion continua hasta poner 
# el valor correcto para que se calcule precio total del producto y se 
# imprima junto con la informacion obtenida