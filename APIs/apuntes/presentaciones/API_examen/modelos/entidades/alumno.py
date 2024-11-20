class Alumno():
    __ultimoid =0
    def __init__(self,legajo:int,apellido:str,nombre:str, id:int=None) -> None:
        if not isinstance(legajo, int):
            raise ValueError
        if legajo<1:
            raise ValueError
        if apellido=='' or apellido is None:
            raise ValueError
        if id != None:
            self.__id=id
        else:
            self.__id=Alumno.obtenerNuevoId()
        self.__legajo=legajo
        self.__apellido=apellido
        self.__nombre=nombre
    @classmethod
    def obtenerNuevoId(cls)->int:
        cls.__ultimoid=cls.__ultimoid+1
        return cls.__ultimoid
    @classmethod
    def obtenerUltimoID(cls)->int:
        return cls.__ultimoid
    @classmethod
    def establecerUltimoId(cls,id:int)->None:
        cls.__ultimoid=id   
    @classmethod
    def fromDiccionario(cls,dict:dict)->None:
        if "id" in dict:
            return cls(
                   dict['legajo'],
                   dict['apellido'],
                   dict['nombre'],
                   dict['id'])
        else:
            return cls(
                   dict['legajo'],
                   dict['apellido'],
                   dict['nombre'])
    
    def obtenerId(self)->int:
        return self.__id
    
    def obtenerLegajo(self):
        return self.__legajo
    
    def toDiccionario(self)->dict:
        return {
            "id":self.__id,
            "legajo": self.__legajo,
            "nombre": self.__nombre,
            "apellido":self.__apellido
        }
    
    def establecerApellido(self, apellido):
        self.__apellido = apellido

    def establecerNombre(self, nombre):
        self.__nombre = nombre