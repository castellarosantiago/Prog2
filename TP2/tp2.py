def leer_entero(mensaje):
    repetir = True
    while repetir:
        try:
            valor = int(input(mensaje))
            repetir = False
        except:
            print("Error, debes ingresar un número entero")
    return valor

def ejercicio1():
    print("Ejecutando Ejercicio 1...")
    def reverso(cadena):
        return cadena[::-1]

    def es_palindromo(cadena):
        cadena = cadena.lower()
        cadena = ''.join(filter(str.isalnum, cadena))
        return cadena == reverso(cadena)
    
    texto = input("Ingresa una cadena de texto: ")
    if es_palindromo(texto):
        print(f'"{texto}" es un palíndromo.')
    else:
        print(f'"{texto}" no es un palíndromo.')
def ejercicio2():
    print("Ejecutando Ejercicio 2...")
    def EsBisiesto(anio):
        return (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0))
    
    def es_fecha_valida(dia, mes, anio):
        # Verificar año bisiesto
        bisiesto = EsBisiesto(anio)
        
        # Número de días por mes
        dias_por_mes = {
            1: 31, 2: 29 if bisiesto else 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        
        # Verificar si el mes y el día son válidos
        if mes in dias_por_mes and 1 <= dia <= dias_por_mes[mes]:
            return True
        else:
            return False
    
    def leer_entero(mensaje):
        repetir = True
        while repetir:
            try:
                valor = int(input(mensaje))
                repetir = False
            except:
                print("Error, debes ingresar un número entero")
        return valor

    dia = leer_entero("Ingrese el día: ")
    mes = leer_entero("Ingrese el mes: ")
    anio = leer_entero("Ingrese el año: ")
    
    if es_fecha_valida(dia, mes, anio):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")
def ejercicio3():
    print("Ejecutando Ejercicio 3...")
    def leer_entero(mensaje):
        repetir = True
        while repetir:
            try:
                valor = int(input(mensaje))
                repetir = False
            except:
                print("Error, debes ingresar un número entero")
        return valor

    # Leer la cantidad de notas a cargar
    cantidad_notas = leer_entero("Ingrese la cantidad de notas que desea cargar: ")

    # Inicializar la lista para las notas
    notas = []

    # Cargar las notas en la lista
    for i in range(cantidad_notas):
        nota = leer_entero(f"Ingrese la nota {i + 1}: ")
        notas.append(nota)

    # Buscar la nota más alta y su índice
    nota_maxima = max(notas)
    indice_maxima = notas.index(nota_maxima)

    # Mostrar el resultado
    print(f"La nota más alta es {nota_maxima} y se encuentra en el índice {indice_maxima}.")
def ejercicio4():
    print("Ejecutando Ejercicio 4...")
    def leer_entero(mensaje):
        repetir = True
        while repetir:
            try:
                valor = int(input(mensaje))
                repetir = False
            except:
                print("Error, debes ingresar un número entero")
        return valor
    
    # Leer y validar el número ingresado
    numero = leer_entero("Ingrese un número: ")
    
    # Crear una lista con los dígitos del número
    digitos = [int(d) for d in str(numero)]
    
    # Encontrar el dígito mayor y su índice
    digito_maximo = max(digitos)
    indice_maximo = digitos.index(digito_maximo)
    
    # Mostrar el índice del dígito mayor
    print(f"El dígito mayor es {digito_maximo} y se encuentra en el índice {indice_maximo}.")    
def ejercicio5():
    print("Ejecutando Ejercicio 5...")
    def leer_entero(mensaje):
        repetir = True
        while repetir:
            try:
                valor = int(input(mensaje))
                repetir = False
            except:
                print("Error, debes ingresar un número entero")
        return valor
    
    def leer_cadena(mensaje):
        return input(mensaje).strip()

    # Leer la cantidad de alumnos
    cantidad_alumnos = leer_entero("Ingrese la cantidad de alumnos: ")

    # Inicializar la lista de alumnos y notas
    alumnos_notas = []

    # Leer los datos de cada alumno
    for _ in range(cantidad_alumnos):
        nombre = leer_cadena("Ingrese el nombre del alumno: ")
        nota = leer_entero(f"Ingrese la nota de {nombre}: ")
        alumnos_notas.append((nombre, nota))

    # Mostrar el resultado
    print("\nALUMNOS          PARCIAL  RESULTADO")
    for nombre, nota in alumnos_notas:
        resultado = "Aprobado" if nota >= 40 else "Desaprobado"
        print(f"{nombre:<15} {nota:<8} {resultado}")
def ejercicio6():
    print("Ejecutando Ejercicio 6...")
    def leer_distancias(archivo):
        try:
            with open(archivo, 'r') as file:
                distancias = [float(line.strip()) for line in file]
            return distancias
        except FileNotFoundError:
            print("Error: El archivo no se encuentra.")
            return []
        except ValueError:
            print("Error: El archivo contiene datos no válidos.")
            return []
    
    def calcular_promedio(distancias):
        if not distancias:
            return 0
        return sum(distancias) / len(distancias)
    
    def mostrar_resultados(distancias, promedio):
        mayores_que_promedio = [d for d in distancias if d > promedio]
        
        print(f"La distancia promedio de los viajes es {promedio:.2f} y los viajes con distancia mayor son: ", end="")
        print(", ".join(f"{d:.2f}" for d in mayores_que_promedio) if mayores_que_promedio else "Ninguno")

    # Leer distancias desde el archivo
    distancias = leer_distancias('distancias.txt')

    if distancias:
        # Calcular el promedio de las distancias
        promedio = calcular_promedio(distancias)
        
        # Mostrar los resultados
        mostrar_resultados(distancias, promedio)
def ejercicio7():
    print("Ejecutando Ejercicio 7...")
    def leer_productos(archivo):
        productos = {}
        try:
            with open(archivo, 'r') as file:
                for line in file:
                    codigo, nombre, precio = line.strip().split(';')
                    productos[codigo] = {'nombre': nombre, 'precio': float(precio)}
        except FileNotFoundError:
            print("Error: El archivo no se encuentra.")
        except ValueError:
            print("Error: El archivo contiene datos no válidos.")
        return productos

    def buscar_precio(productos, codigo_buscar):
        producto = productos.get(codigo_buscar)
        if producto:
            return producto['nombre'], producto['precio']
        else:
            return None, None

    # Leer productos desde el archivo
    productos = leer_productos('productos.txt')

    if productos:
        # Solicitar código del producto
        codigo_buscar = input("Ingrese el código del producto: ")

        # Buscar el precio del producto
        nombre, precio = buscar_precio(productos, codigo_buscar)
        
        if nombre:
            print(f"El precio del producto '{nombre}' con código {codigo_buscar} es {precio:.2f}.")
        else:
            print("El código del producto no se encuentra.")
def ejercicio8():
    print("Ejecutando Ejercicio 8...")
    def leer_productos(archivo):
        productos = {}
        try:
            with open(archivo, 'r') as file:
                for line in file:
                    codigo, nombre, precio = line.strip().split(';')
                    productos[codigo] = {'nombre': nombre, 'precio': float(precio)}
        except FileNotFoundError:
            print("Error: El archivo no se encuentra.")
        except ValueError:
            print("Error: El archivo contiene datos no válidos.")
        return productos

    def leer_stock(archivo):
        stock = {}
        try:
            with open(archivo, 'r') as file:
                for line in file:
                    codigo, stock_minimo, stock_real = line.strip().split(';')
                    stock[codigo] = {'stock_minimo': int(stock_minimo), 'stock_real': int(stock_real)}
        except FileNotFoundError:
            print("Error: El archivo no se encuentra.")
        except ValueError:
            print("Error: El archivo contiene datos no válidos.")
        return stock

    def generar_compras(productos, stock, archivo_salida):
        with open(archivo_salida, 'w') as file:
            for codigo, datos_stock in stock.items():
                if codigo in productos:
                    datos_producto = productos[codigo]
                    stock_minimo = datos_stock['stock_minimo']
                    stock_real = datos_stock['stock_real']
                    if stock_real < stock_minimo:
                        nombre = datos_producto['nombre']
                        precio = datos_producto['precio']
                        file.write(f"{codigo};{nombre};{stock_minimo};{stock_real};{precio}\n")

    # Leer datos de productos y stock
    productos = leer_productos('productos.txt')
    stock = leer_stock('stock.txt')

    # Generar el archivo de compras
    generar_compras(productos, stock, 'compras.txt')

    print("El archivo 'compras.txt' ha sido generado con los productos cuyo stock está por debajo del mínimo.")
def ejercicio9():
    print("Ejecutando Ejercicio 9...")
    def leer_notas(archivo):
        notas = {}
        try:
            with open(archivo, 'r') as file:
                for line in file:
                    datos = line.strip().split(';')
                    legajo = datos[0]
                    notas[legajo] = list(map(float, datos[1:]))
        except FileNotFoundError:
            print("Error: El archivo de notas no se encuentra.")
        except ValueError:
            print("Error: El archivo de notas contiene datos no válidos.")
        return notas

    def leer_alumnos(archivo):
        alumnos = {}
        try:
            with open(archivo, 'r') as file:
                for line in file:
                    datos = line.strip().split(';')
                    legajo = datos[0]
                    apellido = datos[1]
                    nombre = datos[2]
                    alumnos[legajo] = {'apellido': apellido, 'nombre': nombre}
        except FileNotFoundError:
            print("Error: El archivo de alumnos no se encuentra.")
        except ValueError:
            print("Error: El archivo de alumnos contiene datos no válidos.")
        return alumnos

    def generar_promocion(notas, alumnos, archivo_salida):
        promocionados = []
        
        for legajo, notas_alumno in notas.items():
            promedio = sum(notas_alumno) / len(notas_alumno)
            if promedio > 7:
                if legajo in alumnos:
                    alumno = alumnos[legajo]
                    apellido = alumno['apellido']
                    nombre = alumno['nombre']
                    promocionados.append((apellido, nombre))
        
        # Ordenar por apellido y nombre
        promocionados.sort()
        
        # Escribir en el archivo de salida
        with open(archivo_salida, 'w') as file:
            for apellido, nombre in promocionados:
                file.write(f"{apellido};{nombre}\n")

    # Leer datos de notas y alumnos
    notas = leer_notas('alumnos.txt')
    alumnos = leer_alumnos('alumnos_alumnos.txt')

    # Generar el archivo de promoción
    generar_promocion(notas, alumnos, 'promocion.txt')

    print("El archivo 'promocion.txt' ha sido generado con los alumnos que promocionan.")
    
def menu():
    while True:
        print("\nMenú de Ejercicios:")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("7. Ejercicio 7")
        print("8. Ejercicio 8")
        print("9. Ejercicio 9")
        print("0. Salir")

        opcion = leer_entero("Selecciona una opción (0-9): ")

        if opcion == 1:
            ejercicio1()
        elif opcion == 2:
            ejercicio2()
        elif opcion == 3:
            ejercicio3()
        elif opcion == 4:
            ejercicio4()
        elif opcion == 5:
            ejercicio5()
        elif opcion == 6:
            ejercicio6()
        elif opcion == 7:
            ejercicio7()
        elif opcion == 8:
            ejercicio8()
        elif opcion == 9:
            ejercicio9()
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige un número entre 0 y 9.")

if __name__ == "__main__":
    menu()
