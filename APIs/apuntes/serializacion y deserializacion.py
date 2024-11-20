import json

class Persona:
    def __init__(self, dni:int, nombre:str, apellido:str) -> None:
        if not isinstance(dni, int):
            raise TypeError("el dni tiene q ser un numero entero")
        if not isinstance(nombre, str):
            raise TypeError("el nombre tiene q ser un nombre xd como le erras a esto")
        if not isinstance(apellido, str):
            raise ValueError("xd")
        
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
##serializacion
    def to_json(self):
        dicc_persona = {"dni": self.__dni, "nombre":self.__nombre, "apellido":self.__apellido}
        return json.dumps(dicc_persona, ensure_ascii=False)
##deserializacion
    @classmethod
    def from_json(cls, json_data):
        datos = json.loads(json_data)
        return cls(datos["dni"], datos["nombre"], datos["apellido"])