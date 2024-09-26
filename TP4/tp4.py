##metodos setters: son aquellos procedimientos que setean, establecen valores a atributos 
##metodos getters: procedimientos que acceden a las variables/atributos de clase, y devuelven su valor    

class Empleado:
    
    ##constructor
    def __init__(self, legajo:int, cantHoras:int, valorHora:float):
        #atributos de clase
        self.__legajo = legajo
        self.__cantHoras = cantHoras
        self.__valroHora = valorHora
   
    ##comandos - metodos setters
    def establecerHorasTrabajadas(self, cantidadHoras)->int:
         self.__cantHoras = cantidadHoras

    def establecerValorHora(self, valorHora)->float:
         self.__valroHora = valorHora
        
    ##consultas - metodos getters
    def obtenerLegajo(self)->int:
        return self.__legajo

    def obtenerValorHora(self) -> int:
        return self.__valroHora
    
    def obtenerHorasTrabajadas(self) -> int:
        return self.__cantHoras

    def obtenerSueldo(self)->float:
        return self.__cantHoras * self.__valroHora  


class Vinoteca:
    ##atributo de clase
    capacidadMaxima = 5000
    ##atributos de instancia 
    def __init__(self, cantJugos: int = 5000, cantBlancos: int = 5000, cantTintosJovenes: int = 5000, cantTintosAnejados: int = 5000):
        self.__cantJugos = cantJugos
        self.__cantBlancos = cantBlancos
        self.__cantTintosJovenes = cantTintosJovenes
        self.__cantTintosAnejados = cantTintosAnejados


    ##comandos
    def reponerJugos(self, cantJugos):
        if self.__cantJugos + cantJugos <= self.capacidadMaxima:
            self.__cantJugos += cantJugos
        pass

    def reponerVinosBlancos(self, cantBlancos):
        if self.__cantBlancos + cantBlancos <= self.capacidadMaxima:
            self.__cantBlancos += cantBlancos
        pass

    def reponerVinosTintoJoven(self, cantTintosJovenes):
        if self.__cantTintosJovenes + cantTintosJovenes <= self.capacidadMaxima:
            self.__cantTintosJovenes += cantTintosJovenes
        pass

    def reponerVinosTintoAnejado(self, cantTintosAnejados):
        if self.__cantTintosAnejados + cantTintosAnejados <= self.capacidadMaxima:
            self.__cantTintosAnejados += cantTintosAnejados
        pass

    def venderVinosBlancos(self, cantBlancos):
        
        pass

    def venderVinosTintoJoven(self, cantTintosJovenes):

        pass

    def venderVinosTintoAnejado(self, cantTintosAnejados):

        pass

    ##consutlas - metodos getters

    def obtenerCantJugos():

        pass
    def obtenerCantidadVinosBlancos():

        pass

    def obtenerCantitdadVinosTintosJovenes():

        pass

    def obtenerCantidadVinosTintosAnejados():

        pass