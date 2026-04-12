
def guardar_csv(inventario, ruta):
    if len(inventario) == 0:
        print("El inventario está vacío, no se puede guardar")
    else:
        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                archivo.write("nombre,precio,cantidad\n")

                for producto in inventario:
                    linea = producto["nombre"] + "," + str(producto["precio"]) + "," + str(producto["cantidad"]) + "\n"
                    archivo.write(linea)

            print("Inventario guardado en:", ruta)

        except:
            print("Error al guardar el archivo")



def cargar_csv(ruta):
    inventario = [] # Aquí se guardarán los productos válidos, una lista de {}
    errores = 0

    try: # Intenta ejecutar el código
         #Si algo falla va al except
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines() # guarda TODAS las líneas en la lista lineas[]

        if len(lineas) == 0: 
            print("Archivo vacío")
            return [] # Devuelve lista vacía y termina función

        encabezado = lineas[0].strip() # la primera linea se elimina espacios y saltos de línea \n
        if encabezado != "nombre,precio,cantidad": # Verifica que el archivo tenga el formato correcto
            print("Encabezado inválido")
            # si no:
            return [] 

        for linea in lineas[1:]: # por que el encabesado es lineas[0]
            partes = linea.strip().split(",")

            if len(partes) != 3:
                errores += 1
            else:
                nombre = partes[0]

                try:
                    precio = float(partes[1])
                    cantidad = int(partes[2])

                    if precio < 0 or cantidad < 0:
                        errores += 1
                    else:
                        producto = {
                            "nombre": nombre,
                            "precio": precio,
                            "cantidad": cantidad
                        }
                        inventario.append(producto)

                except:
                    errores += 1

        print("Productos cargados:", len(inventario))
        print("Filas inválidas omitidas:", errores)

        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado")
        return []
    except UnicodeDecodeError:
        print("Error de codificación en el archivo")
        return []
    except:
        print("Error al leer el archivo")
        return []