from modelos.entidades.alumno import Alumno
import json

class RepositorioAlumno:
    __ruta_archivo = "datos/alumnos.json"

    def __init__(self):
        self.__alumnos = self.__cargarTodos()

    def __cargarTodos(self):
        #tomar del archivo el json
        #convertir en lista o diccionario
        #crear los objetos y cargarlos en la lista interna
        lista_objetos = []
        try:
            with open(RepositorioAlumno.__ruta_archivo, 'r', encoding="UTF-8") as archivo:
                dicc = json.load(archivo)
            Alumno.establecerUltimoId(dicc["ultimoID"])
            for alumno in dicc["alumnos"]:
                lista_objetos.append(Alumno.fromDiccionario(alumno))
        except Exception as e:
            print("error cargando los datos de alumnos.\n"+ str(e))
        
        return lista_objetos
    
    def __guardarTodos(self):
        lista_dicc = []
        for alumno in self.__alumnos:
            lista_dicc.append(alumno.toDiccionario())
        
        diccDatos = {
            "ultimoID":Alumno.obtenerUltimoID(),
            "alumnos": lista_dicc
        }

        try:
            with open(RepositorioAlumno.__ruta_archivo, "w", encoding="UTF-8") as archivo:
                json.dump(diccDatos, archivo, indent=4)
        except Exception as e:
            print("error guardando los datos de alumnos.\n"+ str(e))
        
    #pedirle objetos
    #todos
    def obtenerTodos(self):
        return self.__alumnos
    
    #VALIDACIONES!!
    #uno en particular por una clave
    def obtenerAlumnoPorLegajo(self, legajo:int)->Alumno:
        #buscar en cada alumno si su legajo coincide, si coincide lo retorno
        for alumno in self.__alumnos:
            if legajo == alumno.obtenerLegajo():
                return alumno
        return None
    
    def existeAlumnoPorLegajo(self, legajo:int)->bool:
        for alumno in self.__alumnos:
            if legajo == alumno.obtenerLegajo():
                return True
        return False
    
    #eliminar
    def eliminarPorLegajo(self, legajo:int):
        for alumno in self.__alumnos:
            if legajo == alumno.obtenerLegajo():
                self.__alumnos.remove(alumno)
                self.__guardarTodos()

    #modificar
    def modificarPorLegajo(self, legajo:int, apellido:str, nombre:str):
        for alumno in self.__alumnos:
            if legajo == alumno.obtenerLegajo():
                alumno.establecerApellido(apellido)
                alumno.establecerNombre(nombre)
                self.__guardarTodos()
                break
    #agregar
    def agregar(self, alumno:Alumno):
        if not self.existeAlumnoPorLegajo(alumno.obtenerLegajo()):
            self.__alumnos.append(alumno)
            self.__guardarTodos()