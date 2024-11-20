class Alumno:
    def __init__(self, legajo, id_interno, nombre, apellido):
        self.legajo = legajo
        self.id_interno = id_interno
        self.nombre = nombre
        self.apellido = apellido

class Tema:
    def __init__(self, numero, nombre, enunciado):
        self.numero = numero
        self.nombre = nombre
        self.enunciado = enunciado