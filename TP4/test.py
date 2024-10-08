from tp4 import Empleado, Vinoteca

##clases tester del ejercicio 2
def testEj2():

    ##pedir al usuario ingresar los datos de un empleado

    legajo = int(input("Ingrese el legajo del empleado: "))
    cant_horas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
    valor_hora = float(input("Ingrese el valor de la hora: "))

    ##creo un objeto de tipo Empleado usando el constructor
    empleado = Empleado(legajo,cant_horas, valor_hora)

    ##Uso los metodos para establecer las horas trabajadas y el valor de la hora

    empleado.establecerHorasTrabajadas(cant_horas)
    empleado.establecerValorHora(valor_hora)

    print(f"Legajo N°{empleado.obtenerLegajo()}")
    print(f"Sueldo calculado: {empleado.obtenerSueldo()}")

def alternateTestEj2():
    ##ingreso de los datos del empleado
    legajo = int(input("Ingrese el lejajo del epmleado: "))
    cant_horas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
    valor_hora = float(input("Ingrese el valor de la hora:"))

    #se utiliza el constructor solo con el atributo legajo, para despues modificar los otros atributos
    empleado = Empleado(legajo, 0, 0)

    #se utilizan los metodos setters para modificar los atributos necesarios

    empleado.establecerHorasTrabajadas(cant_horas)
    empleado.establecerValorHora(valor_hora)

    ##se muestra el resultado con los metodos getters

    print(f"Legajo N°{empleado.obtenerLegajo()}")
    print(f"Sueldo calculado: {empleado.obtenerSueldo()}")

##clases tester del ejercicio 3
def testEj3():
    vinoteca = Vinoteca()
    while True:
        print("Vinoteca Menu:")
        print("1. Ver cantidad de Jugos")
        print("2. Ver cantidad de Vinos Blancos")
        print("3. Ver cantidad de Vinos Tintos Jóvenes")
        print("4. Ver cantidad de Vinos Tintos Añejados")
        print("5. Vender Jugos")
        print("6. Vender Vinos Blancos")
        print("7. Vender Vinos Tintos Jóvenes")
        print("8. Vender Vinos Tintos Añejados")
        print("9. Reponer Jugos")
        print("10. Reponer Vinos Blancos")
        print("11. Reponer Vinos Tintos Jóvenes")
        print("12. Reponer Vinos Tintos Añejados")
        print("13. Salir")

        option = int(input("Ingrese una opción: "))

        if option == 1:
            print(f"La cantidad de Jugos actual es de {vinoteca.obtenerCantJugos()}")
        elif option == 2:
            print(f"La cantidad de Vinos Blancos actual es de {vinoteca.obtenerCantidadVinosBlancos()}")
        elif option == 3:
            print(f"La cantidad de Vinos Tintos Jóvenes actual es de {vinoteca.obtenerCantitdadVinosTintosJovenes()}")
        elif option == 4:
            print(f"La cantidad de Vinos Tintos Añejados actual es de {vinoteca.obtenerCantidadVinosTintosAnejados()}")
        elif option == 5:
            cantidad = int(input("Ingrese la cantidad de Jugos a vender: "))
            vinoteca.venderJugos(cantidad)
            print(f"Venta realizada con éxito, cantidad de Jugos disponible: {vinoteca.obtenerCantJugos()}")
        elif option == 6:
            cantidad = int(input("Ingrese la cantidad de Vinos Blancos a vender: "))
            vinoteca.venderVinosBlancos(cantidad)
            print(f"Venta realizada con éxito, cantidad de Vinos Blancos disponible: {vinoteca.obtenerCantidadVinosBlancos()}")
        elif option == 7:
            cantidad = int(input("Ingrese la cantidad de Vinos Tintos Jóvenes a vender: "))
            vinoteca.venderVinosTintosJovenes(cantidad)
            print(f"Venta realizada con éxito, cantidad de Vinos Tintos Jóvenes disponible: {vinoteca.obtenerCantitdadVinosTintosJovenes()}")
        elif option == 8:
            cantidad = int(input("Ingrese la cantidad de Vinos Tintos Añejados a vender: "))
            vinoteca.venderVinosTintosAnejados(cantidad)
            print(f"Venta realizada con éxito, cantidad de Vinos Tintos Añejados disponible: {vinoteca.obtenerCantidadVinosTintosAnejados()}")
        elif option == 9:
            cantidad = int(input("Ingrese la cantidad de Jugos a reponer: "))
            vinoteca.reponerJugos(cantidad)
            print(f"Reposición realizada con éxito, cantidad de Jugos disponible: {vinoteca.obtenerCantJugos()}")
        elif option == 10:
            cantidad = int(input("Ingrese la cantidad de Vinos Blancos a reponer: "))
            vinoteca.reponerVinosBlancos(cantidad)
            print(f"Reposición realizada con éxito, cantidad de Vinos Blancos disponible: {vinoteca.obtenerCantidadVinosBlancos()}")
        elif option == 11:
            cantidad = int(input("Ingrese la cantidad de Vinos Tintos Jóvenes a reponer: "))
            vinoteca.reponerVinosTintoJovenes(cantidad)
            print(f"Reposición realizada con éxito, cantidad de vinos Tintos Jóvenes disponible: {vinoteca.obtenerCantitdadVinosTintosJovenes()}")
        elif option == 12:
            cantidad = int(input("Ingrese la cantidad de Vinos Tintos Añejados a reponer: "))
            vinoteca.reponerVinosTintoAnejados(cantidad)
            print(f"Reposición realizada con éxito, cantidad de Vinos Tintos Añejados disponible: {vinoteca.obtenerCantidadVinosTintosAnejados()}")
        elif option == 13:
            print("Saliendo del menú...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def testEj4():
    pass#TODO

if __name__ == "__main__":
    #testEj2()
    #alternateTestEj2()
    #testEj3()
    pass