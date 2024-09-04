def leerentero(mensaje):
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
    def cuadrados(lista_numeros):
        return [x**2 for x in lista_numeros]

    # Ejemplo de uso:
    numeros = [1, 2, 3, 4, 5]
    resultado = cuadrados(numeros)
    print("Cuadrados:", resultado)

def ejercicio2():
    print("Ejecutando Ejercicio 2...")
    def filtrar_nombres(nombres, longitud_minima):
        return [nombre for nombre in nombres if len(nombre) >= longitud_minima]

    # Ejemplo de uso:
    nombres = ["Ana", "Roberto", "Luis", "Alejandra", "Marta"]
    longitud_minima = 5
    resultado = filtrar_nombres(nombres, longitud_minima)
    print("Nombres filtrados:", resultado)

def ejercicio3():
    print("Ejecutando Ejercicio 3...")
    def leer_lineas(archivo):
        with open(archivo, 'r') as file:
            return [linea.strip() for linea in file]

    # Ejemplo de uso:
    archivo = 'datos.txt'
    lineas = leer_lineas(archivo)
    print("Líneas del archivo:", lineas)

def ejercicio4():
    print("Ejecutando Ejercicio 4...")
    def filtrar_palabras(diccionario, letra):
        return [palabra for palabra in diccionario if palabra.startswith(letra)]

    # Ejemplo de uso:
    diccionario = {
        "apple": "a fruit",
        "banana": "a fruit",
        "avocado": "a fruit",
        "carrot": "a vegetable",
        "apricot": "a fruit"
    }
    letra = "a"
    resultado = filtrar_palabras(diccionario, letra)
    print("Palabras que comienzan con '{}':".format(letra), resultado)
    
def ejercicio5():
    print("Ejecutando Ejercicio 5...")
    def es_primo(num):
        if num < 2:
            return False
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

    def numeros_primos(rango_inicio, rango_fin):
        return [num for num in range(rango_inicio, rango_fin + 1) if es_primo(num)]

    # Ejemplo de uso:
    inicio = 10
    fin = 50
    primos = numeros_primos(inicio, fin)
    print("Números primos en el rango de {} a {}:".format(inicio, fin), primos)

def ejercicio6():
    print("Ejecutando Ejercicio 6...")
    def filtrar_personas_por_edad(diccionario, edad_minima):
        return [nombre for nombre, edad in diccionario.items() if edad > edad_minima]

    # Ejemplo de uso:
    personas = {
        "Ana": 23,
        "Luis": 30,
        "Carlos": 17,
        "Marta": 25,
        "Sofía": 20
    }
    
    edad_minima = int(input("Ingresa la edad mínima: "))
    resultado = filtrar_personas_por_edad(personas, edad_minima)
    print("Personas mayores de {} años:".format(edad_minima), resultado)

def ejercicio7():
    print("Ejecutando Ejercicio 7...")
    def contar_vocales(palabra):
        return sum(1 for letra in palabra.lower() if letra in 'aeiou')

    while True:
        palabra = input("Ingresa una palabra (o 'salir' para terminar): ").strip()
        if palabra.lower() == "salir":
            print("Terminando el programa...")
            break
        cantidad_vocales = contar_vocales(palabra)
        print(f"La cantidad de vocales en '{palabra}' es: {cantidad_vocales}")

def ejercicio8():
    print("Ejecutando Ejercicio 8...")
    def eliminar_duplicados(lista):
        return [elemento for elemento in set(lista)]

    # Ejemplo de uso:
    lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5, 5, 5]
    lista_unica = eliminar_duplicados(lista_con_duplicados)
    print("Lista sin duplicados:", lista_unica)

def ejercicio9():
    print("Ejecutando Ejercicio 9...")
    def separar_pares_impares(lista):
        pares = [num for num in lista if num % 2 == 0]
        impares = [num for num in lista if num % 2 != 0]
        return pares, impares

    # Ejemplo de uso:
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares, impares = separar_pares_impares(lista_numeros)
    print("Números pares:", pares)
    print("Números impares:", impares)

def ejercicio10():
    print("Ejecutando Ejercicio 10...")
    estudiantes = [
        {"nombre_apellido": "Pepe", "legajo": 101, "nota_parcial1": 75, "nota_parcial2": 80, "nota_final": 85},
        {"nombre_apellido": "María", "legajo": 102, "nota_parcial1": 65, "nota_parcial2": 70, "nota_final": 90},
        {"nombre_apellido": "Pedro", "legajo": 103, "nota_parcial1": 55, "nota_parcial2": 65, "nota_final": 60},
        {"nombre_apellido": "Ana", "legajo": 104, "nota_parcial1": 90, "nota_parcial2": 85, "nota_final": 95}
    ]

    # a. Lista con los nombres de todos los estudiantes
    nombres = [estudiante["nombre_apellido"] for estudiante in estudiantes]
    print("Nombres:", nombres)

    # b. Lista con los nombres de estudiantes con calificación superior a 70 en todos los exámenes
    superiores_70 = [estudiante["nombre_apellido"] for estudiante in estudiantes 
                      if (estudiante["nota_parcial1"] > 70 and 
                          estudiante["nota_parcial2"] > 70 and 
                          estudiante["nota_final"] > 70)]
    print("Estudiantes con calificaciones superiores a 70 en todos los exámenes:", superiores_70)

    # c. Lista con los nombres de estudiantes con calificación inferior a 60 en al menos un examen
    inferiores_60 = [estudiante["nombre_apellido"] for estudiante in estudiantes 
                      if (estudiante["nota_parcial1"] < 60 or 
                          estudiante["nota_parcial2"] < 60 or 
                          estudiante["nota_final"] < 60)]
    print("Estudiantes con calificación inferior a 60 en al menos un examen:", inferiores_60)

#--------------------------------------------MENU------------------------------------------------
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

        opcion = leerentero("Selecciona una opción (0-10): ")

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
        elif opcion == 10:
            ejercicio10()
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige un número entre 0 y 9.")

if __name__ == "__main__":
    menu()