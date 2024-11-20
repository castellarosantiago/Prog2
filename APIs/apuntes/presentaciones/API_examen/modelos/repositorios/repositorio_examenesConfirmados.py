from modelos.entidades.temaalumno import TemaAlumno
from modelos.entidades.alumno import Alumno
from modelos.entidades.tema import Tema
import json
import os

class RepositorioExamenesConfirmados:
    __ruta_archivo = "datos/examenesConfirmados.json"

    def __init__(self):
        self.__examenes = self.__cargarTodos()

    def __cargarTodos(self):
        lista_diccionarios =[]
        lista_objetos=[]
        if os.path.exists(RepositorioExamenesConfirmados.__ruta_archivo):
            try:
                with open(RepositorioExamenesConfirmados.__ruta_archivo,"r", encoding="UTF-8") as archivo:
                    lista_diccionarios = json.load(archivo)
            except:
                print("error al cargar datos del archivo temas.json")
            for dicc in lista_diccionarios:
                lista_objetos.append(TemaAlumno.fromDiccionario(dicc))
        
        return lista_objetos



    def __guardarTodos(self):
        lista_dicc = []
        for examen in self.__examenes:
            if isinstance(examen, TemaAlumno): #
                lista_dicc.append(examen.toDiccionario())
        
        with open(RepositorioExamenesConfirmados.__ruta_archivo, "w", encoding="UTF-8") as arch:
            json.dump(lista_dicc, arch)

    # buscar todos
    def obtenerTodos(self):
        return self.__examenes
    
    def agregar(self, examen_confirmado:TemaAlumno):
        self.__examenes.append(examen_confirmado)
        self.__guardarTodos()
        return True