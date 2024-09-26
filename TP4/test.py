from tp4 import Empleado

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


if __name__ == "__main__":
    testEj2()
    alternateTestEj2()