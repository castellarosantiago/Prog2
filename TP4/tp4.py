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

class Automovil:
    ##atributos de instancia
    marca = ""
    modelo = ""
    velocidadMaxima = float
    velocidadActual = float

    ##constructor
    def __init__(self, marca:str, modelo:str, anno:int, velocidadMaxima:float, velocidadActual:float):
        self.__marca = marca
        self.__modelo = modelo
        self.__anno = anno
        self.__velocidadMaxima = velocidadMaxima
        self.__velocidadActual = velocidadActual

    ##comandos
    def establecerMarca(self, marca):
        self.__marca = marca

    def establecerModelo(self, modelo):
        self.__modelo = modelo

    def establecerVelocidadMaxima(self, velocidadMaxima):
        self.__velocidadMaxima = velocidadMaxima

    def establecerVelocidadActual(self, velocidadActual):
        self.__velocidadActual = velocidadActual

    def acelerar(self, velocidadActual, velocidadMaxima):
        if self.__velocidadActual <= self.__velocidadMaxima:
            velocidadActual += velocidadMaxima

    def desacelerar(self, velocidadActual):
        if self.__velocidadActual > 0:
            velocidadActual -= velocidadActual

    def frenarPorCompleto(self, velocidadActual):
        if self.__velocidadActual > 0:
            velocidadActual = 0


    ##consultas

    def obtenerMarca(self):
        return self.__marca

    def obternerModelo(self):
        return self.__modelo
    
    def obtenerAnno(self):
        return self.__anno
    
    def obtenerVelocidadMaxima(self):
        return self.__velocidadMaxima
    
    def obtenerVelocidadActual(self):
        return self.__velocidadActual
    
    def calcularMinutosParaLlegar(self, distanciaKM:float, tiempoParaLlegar:int):
        distanciaKM = 0
        tiempoParaLlegar = 0
        
        pass