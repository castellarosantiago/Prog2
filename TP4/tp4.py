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
        

    def reponerVinosBlancos(self, cantBlancos):
        if self.__cantBlancos + cantBlancos <= self.capacidadMaxima:
            self.__cantBlancos += cantBlancos
        

    def reponerVinosTintoJovenes(self, cantTintosJovenes):
        if self.__cantTintosJovenes + cantTintosJovenes <= self.capacidadMaxima:
            self.__cantTintosJovenes += cantTintosJovenes
        

    def reponerVinosTintoAnejados(self, cantTintosAnejados):
        if self.__cantTintosAnejados + cantTintosAnejados <= self.capacidadMaxima:
            self.__cantTintosAnejados += cantTintosAnejados
        

    def venderJugos(self, cantJugos):

        if cantJugos <= self.__cantJugos:
            self.__cantJugos -= cantJugos

    def venderVinosBlancos(self, cantBlancos):
        if cantBlancos <= self.__cantBlancos:
            self.__cantBlancos -= cantBlancos
        

    def venderVinosTintoJoven(self, cantTintosJovenes):
        if cantTintosJovenes <= self.__cantTintosJovenes:
            self.__cantTintosJovenes -= cantTintosJovenes
        

    def venderVinosTintoAnejado(self, cantTintosAnejados):
        if cantTintosAnejados <= self.__cantTintosAnejados:
            self.__cantTintosAnejados -= cantTintosAnejados
        

    ##consutlas - metodos getters

    def obtenerCantJugos(self):
        return self.__cantJugos
        
    def obtenerCantidadVinosBlancos(self):
        return self.__cantBlancos

        

    def obtenerCantitdadVinosTintosJovenes(self):
        return self.__cantTintosJovenes

        

    def obtenerCantidadVinosTintosAnejados(self):
        return self.__cantTintosAnejados

        