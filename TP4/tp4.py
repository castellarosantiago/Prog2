class Empleado:

    def __init__(self, legajo:int, cantHoras:int=0, valorHora:float=0):
        #atributos de clase
        self.__legajo = legajo
        self.__cantHoras = cantHoras
        self.__valroHora = valorHora

    def establecerHorasTrabajadas()->int:
        pass #TODO

    def establecerValorHora()->float:
        pass #TODO

    def obtenerSueldo()->float:
        pass #TODO