from abc import ABC, abstractmethod
from datetime import date, datetime, now

class Empleado(ABC):
    def __init__(self, DNI:str, nombre:str, apellido:str, anioIngreso:int, fechaNac:date):
        self._DNI = DNI
        self._nombre = nombre
        self._apellido = apellido
        self._anioIngreso = anioIngreso
        self._fechaNac = fechaNac
    @abstractmethod
    def obtenerSueldo():
        pass

class Empresa():
    def __init__(self) -> None:
        self.__listaEmpleados = []
    def obtenerSueldoTotal(self) -> float:
        total = 0
        for empleado in self.__listaEmpleados:
            total += empleado.obtenerSueldo()
        return total
    def agregarEmpleado(self, empleado:Empleado) -> None:
        self.__listaEmpleados.append(empleado)

    def empleadoMasClientesCaptados(self, empleado:Empleado) -> Empleado:
        cantMayor = -1
        empleadoMayor = None
        for empleado in self.__listaEmpleados:
            if isinstance(empleado, EmpleadoSueldoVariable):
                if empleado.obtenerClientesCaptados() > cantMayor:
                    cantMayor = empleado.obtenerClientesCaptados()
                    empleadoMayor = empleado



class EmpleadoSueldoFijo(Empleado):
    def __init__(self, sueldoBasico:float, DNI:str, nombre:str, apellido:str, anioIngreso:int, fechaNac:date)->None:
        super().__init__(self, DNI, nombre, apellido, anioIngreso, fechaNac)
        self.__sueldoBasico = sueldoBasico
    def obtenerSueldo(self) -> float:
        ##que mal que te veo parcial de mañana
        return self.__sueldoBasico * self.__calcularMontoAntiguedad
    def __calcularMontoAntiguedad(self):
        antiguedad = now().year - self._anioIngreso
        porcentajeantiguedad = 1
        if antiguedad > 2 and antiguedad <5:
            porcentajeantiguedad = 1.05
        else:
            if antiguedad>=5:
                porcentajeantiguedad = 1.10
        return porcentajeantiguedad
    


    pass