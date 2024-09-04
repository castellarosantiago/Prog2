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
    # Código del Ejercicio 1
    # Solicitar los tres lados del triángulo
    lado1 = float(input("Ingresa el primer lado del triángulo: "))
    lado2 = float(input("Ingresa el segundo lado del triángulo: "))
    lado3 = float(input("Ingresa el tercer lado del triángulo: "))

    # Determinar el tipo de triángulo
    if lado1 == lado2 == lado3:
        print("El triángulo es Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es Isósceles")
    else:
        print("El triángulo es Escaleno")

def ejercicio2():
    print("Ejecutando Ejercicio 2...")
    # Código del Ejercicio 2
    ancho = float(input("Ingrese el ancho de la habitacion: "))
    largo = float(input("Ingrese el largo de la habitacion: "))
    alto = float(input("Ingrese el alto de la habitacion: "))

        # Área total de las paredes (dos paredes de ancho por alto y dos de largo por alto)
    area_paredes = (2 * ancho * alto) + (2 * largo * alto)
    
    # Área de la puerta (0,8 m * 2 m)
    area_puerta = 0.8 * 2
    
    # Área total a pintar
    area_a_pintar = area_paredes - area_puerta
    
    # Litros de pintura necesarios
    pintura_por_mano = area_a_pintar / 10
    pintura_total = input("Ingrese la cantidad de manos de pintura: ")
    pintura_total = pintura_por_mano * pintura_total
    print (f"La cantidad de pintura necesaria es: {pintura_total}")
    

def ejercicio4():
    print("Ejecutando Ejercicio 4...")
    # Código del Ejercicio 4
    num1 = input("ingrese el primer numero: ")
    num2 = input("ingrese el segundo numero: ")
    num3 = input("ingrese el tercer numero: ")
    
    if num1 > num2 and num1 > num3:
        print(f"{num1} es el numero mas grande")
    elif num2 > num1 & num2 > num3:
        print(f"{num2} es el numero mas grande")
    else:
        print(f"{num3} es el numero mas grande")

def ejercicio5():
    print("Ejecutando Ejercicio 5...")
    # Código del Ejercicio 5
    cadena = input("ingresa una palabra o frase...")
    espacios = cadena.count(' ')
    print(f"La cadena contiene {espacios} espacios.")

def ejercicio6():
    numero_secuencia = input("ingrese un numero" + leer_entero())
    
    secuencia = True
    while secuencia == True:
        for i in range(0, numero_secuencia+1):
            if i > 0:
                print(i, end=" ")
                secuencia = False
            else:
                print("Debe ingresar un numero mayor a 0")

def ejercicio7():
   print("Ejecutando Ejercicio 7...")
   #Codigo del Ejercicio 7
   numero_secuencia = input("ingrese un numero" + leer_entero())
    
   secuencia = True
   while secuencia == True:
        for i in range(0, numero_secuencia+1):
            if i > 0 and i % 2 == 0:
                print(i, end=" ")
                secuencia = False
            else:
                print("Debe ingresar un numero mayor a 0")    

def ejercicio8():
    print("Ejecutando Ejercicio 8...")
    # Código del Ejercicio 8
    cantidad = leer_entero(input("Ingrese la cantidad de valores que quiere registrar: "))
    
    ciclar = True
    aux = 0 
    numero = 0
    while ciclar == True:
        for i in range (0, cantidad + 1):
            numero = input("ingrese un numero entero")
            aux = numero + aux
    promedio = aux/cantidad
    print(f"La suma de los {cantidad} valores ingresados es: {aux}")
    print(f"Y el promedio de los {cantidad} valores ingresados es: {promedio}")

def ejercicio9():
    print("Ejecutando Ejercicio 9...")
    # Código del Ejercicio 9

    A = int(input("Ingresa el primer número entero positivo (A): "))
    B = int(input("Ingresa el segundo número entero positivo (B): "))
    X = int(input("Ingresa el número entero positivo (X) para encontrar sus múltiplos: "))

    if A > 0 and B > 0 and X > 0:
        print(f"Múltiplos de {X} entre {A} y {B} inclusive:")
        for i in range(A, B + 1):
            if i % X == 0:
                print(i, end=" ")
    else:
        print("Debes ingresar solo números enteros positivos.")

def ejercicio10():
    ancho = int(input("Ingresa la medida del ancho del rectángulo: "))
    alto = int(input("Ingresa la medida del alto del rectángulo: "))

    # Verificación de que ambos lados sean positivos y que el lado más largo no exceda 40
    if ancho > 0 and alto > 0 and max(ancho, alto) <= 40:
        for i in range(alto):
            print('*' * ancho)
    else:
        print("Error: ambos lados deben ser positivos y el lado más largo no debe exceder 40.")
        

def ejercicio11():
    suma = 0
    cantidad = 0

    while True:
        numero = int(input("Ingresa un número entero positivo (o un número negativo para finalizar): "))
        
        if numero < 0:
            break

        suma += numero
        cantidad += 1

    if cantidad > 0:
        promedio = suma / cantidad
        print(f"El promedio es {promedio:.2f} con un total de {cantidad} ingresos.")
    else:
        print("No se ingresaron números positivos.")

def ejercicio12():
    numeros = []
    
    while True:
        numero = int(input("Ingresa un número entero positivo (o 0 para finalizar): "))
        
        if numero == 0:
            break
        
        if numero > 0:
            numeros.append(numero)
        else:
            print("Solo se permiten números enteros positivos.")

    if numeros == sorted(numeros):
        print("La secuencia está ordenada de menor a mayor.")
    else:
        print("La secuencia no está ordenada de menor a mayor.")

def ejercicio13():
    caracter = input("Ingresa un carácter: ")
    N = int(input("Ingresa la cantidad de repeticiones: "))

    if len(caracter) == 1 and N > 0:
        print(caracter * N)
    else:
        print("Error: Debes ingresar un solo carácter y un número natural mayor a 0.")

def ejercicio14():
    texto = input("Ingresa un texto: ").lower()
    vocales = "aeiou"
    contador = 0

    for caracter in texto:
        if caracter in vocales:
            contador += 1

    print(f"El texto contiene {contador} vocales.")

def ejercicio15():
    oracion = input("Ingresa una oración: ")
    
    # a. Número total de caracteres en la oración
    total_caracteres = len(oracion)
    
    # b. Cantidad total de letras (consonantes y vocales, sin signos de puntuación)
    total_letras = sum(1 for c in oracion if c.isalpha())
    
    # c. Cantidad de palabras separadas por uno o más espacios
    palabras = oracion.split()
    total_palabras = len(palabras)
    
    # Resultados
    print(f"El número total de caracteres en la oración es: {total_caracteres}")
    print(f"La cantidad total de letras (consonantes y vocales) es: {total_letras}")
    print(f"La cantidad total de palabras es: {total_palabras}")

def ejercicio16():
    texto = input("Ingresa un texto: ")
    
    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Encontrar la palabra más larga
    palabra_larga = max(palabras, key=len)
    
    # Mostrar el resultado
    print(f"La palabra más larga es '{palabra_larga}' y tiene {len(palabra_larga)} letras.")
    
# ------------------------------------MENU--------------------------------------------------------
def menu():
    while True:
        print("\nMenú de Ejercicios:")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("7. Ejercicio 7")
        print("8. Ejercicio 8")
        print("9. Ejercicio 9")
        print("10. Ejercicio 10")
        print("11. Ejercicio 11")
        print("12. Ejercicio 12")
        print("13. Ejercicio 13")
        print("14. Ejercicio 14")
        print("15. Ejercicio 15")
        print("16. Ejercicio 16")
        print("0. Salir")

        opcion = leer_entero("Selecciona una opción (0-16): ")

        if opcion == 1:
            ejercicio1()
        elif opcion == 2:
            ejercicio2()
        elif opcion == 4:
            ejercicio4 ()
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
        elif opcion == 11:
            ejercicio11()
        elif opcion == 12:
            ejercicio12()
        elif opcion == 13:
            ejercicio13()
        elif opcion == 14:
            ejercicio14()
        elif opcion == 15:
            ejercicio15()
        elif opcion == 16:
            ejercicio16()
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige un número entre 0 y 9.")

if __name__ == "__main__":
    menu()
