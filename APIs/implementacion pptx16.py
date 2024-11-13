import json

class Direccion:

    #metodos de clase ---------------------------
    @classmethod
    def fromDiccionario(cls, data: dict) -> "Direccion":
        if not isinstance(data, dict):
            raise ValueError("")
        return Direccion(data)
    #constructor y metodos de instancia -----------------------
    def __init__(self, calle:str, numero:str) -> None:
        if not isinstance(calle, str):
            raise TypeError("xd")
        if not isinstance(numero, str):
            raise TypeError("xd")
        
        self.__calle = calle
        self.__numero = numero

    def obtenerCalle(self)->str:
        return self.__calle
    
    def obtenerNumero(self)->str:
        return self.__numero
    
    def esigualProf(self, otra:"Direccion")->bool:
        return self.__calle == otra.obtenerCalle() and self.__numero == otra.obtenerNumero()
    
    def toDiccionario(self):
        return {"calle":self.__calle, "numero":self.__numero}

class Persona:
    ##metodos de clase
    @classmethod
    def fromDiccionario(cls, data:dict)->"Persona":
        if not isinstance(data, dict):
            raise TypeError("loco, hace falta que te lo diga?")
        return cls(data["nombre"], data["apellido"], data["direccion"])
    
    ##constructor y metodos de instancia
    def __init__(self, nombre:str, apellido:str, direccion:Direccion):
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser un string válido")
        if not isinstance(apellido, str) or apellido == "" or apellido.isspace():
            raise ValueError("El apellido tambien flaco como le podes errar")
        if not isinstance(direccion, Direccion):
            raise ValueError("La dirección debe ser una instancia de la clase dirección")
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion

    def obtenerNombre(self)->str:
        return self.__nombre
    def obtenerApellido(self)->str:
        return self.__apellido
    def obtenerDireccion(self)->Direccion:
        return self.__direccion
    
    def esigualProf(self, otra:"Persona")->bool:
        return self.__nombre == otra.obtenerNombre() and self.__apellido == otra.obtenerApellido() and self.__direccion == otra.obtenerDireccion()
    
    def toDiccionario(self):
        return {"nombre:":self.__nombre, "apellido":self.__apellido, "direccion":self.__direccion.toDiccionario()}