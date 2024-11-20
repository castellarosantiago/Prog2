from modelos.entidades.temaalumno import TemaAlumno
from modelos.entidades.alumno import Alumno
from modelos.entidades.tema import Tema
import json
import os

class RepositorioExamenes:
    __ruta_archivo = "datos/examenesDisponibles.json"

    def __init__(self):
        self.__examenes = self.__cargarTodos()

    def __cargarTodos(self):
        lista_diccionarios =[]
        lista_objetos=[]
        if os.path.exists(RepositorioExamenes.__ruta_archivo):
            try:
                with open(RepositorioExamenes.__ruta_archivo,"r", encoding="UTF-8") as archivo:
                    lista_diccionarios = json.load(archivo)
            except:
                print("error al cargar datos del archivo temas.json")
            for dicc in lista_diccionarios:
                lista_objetos.append(TemaAlumno.fromDiccionario(dicc))
        else:
            #mezcla aleatoria
            import random
            from modelos.repositorios.repositorios import obtenerRepoAlumnos, obtenerRepoTemas
            repo_temas = obtenerRepoTemas()
            repo_alumnos = obtenerRepoAlumnos()
            for alumno in repo_alumnos.obtenerTodos():
                #tema_aleatorio = repo_temas.obtenerTemaPorNumero(random.randint(1,5))
                tema_aleatorio = random.choice(repo_temas.obtenerTodos())
                examen = TemaAlumno(alumno, tema_aleatorio)
                lista_objetos.append(examen)
            self.__guardarCreacionExamenes(lista_objetos)
        return lista_objetos
    
    def __guardarCreacionExamenes(self, lista_obj:list):
        lista_dicc = []
        for examen in lista_obj:
            if isinstance(examen, TemaAlumno): #
                lista_dicc.append(examen.toDiccionario())
        
        with open(RepositorioExamenes.__ruta_archivo, "w", encoding="UTF-8") as arch:
            json.dump(lista_dicc, arch)

    def __guardarTodos(self):
        lista_dicc = []
        for examen in self.__examenes:
            if isinstance(examen, TemaAlumno): #
                lista_dicc.append(examen.toDiccionario())
        
        with open(RepositorioExamenes.__ruta_archivo, "w", encoding="UTF-8") as arch:
            json.dump(lista_dicc, arch)

    # buscar todos
    def obtenerTodos(self):
        return self.__examenes

    #VALIDACONES!!
    # buscar uno
    def obtenerExamenPorIDAlumno(self, id:int):
        for examen in self.__examenes:
            if id == examen.obtenerAlumno().obtenerId():
                return examen
        return None
    

    