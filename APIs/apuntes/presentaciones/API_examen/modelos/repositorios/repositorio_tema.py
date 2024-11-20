from modelos.entidades.tema import Tema
import json

class RepositorioTema:
    __ruta_archivo="datos/temas.json"

    def __init__(self):
        self.__temas = self.__cargarTodos()

    def __cargarTodos(self):
        lista_diccionarios =[]
        lista_objetos=[]
        try:
            with open(RepositorioTema.__ruta_archivo,"r", encoding="UTF-8") as archivo:
                lista_diccionarios = json.load(archivo)
        except:
            print("error al cargar datos del archivo temas.json")
        for dicc in lista_diccionarios:
            lista_objetos.append(Tema.fromDiccionario(dicc))
        return lista_objetos

    def __guardarTodos(self):
        lista_dicc = []
        for tema in self.__temas:
            if isinstance(tema, Tema): #
                lista_dicc.append(tema.toDiccionario())
        
        with open(RepositorioTema.__ruta_archivo, "w", encoding="UTF-8") as arch:
            json.dump(lista_dicc, arch)

    # buscar todos
    def obtenerTodos(self):
        return self.__temas

    #VALIDACONES!!
    # buscar uno
    def obtenerTemaPorNumero(self, numero:int):
        for tema in self.__temas:
            if numero == tema.obtenerNumero():
                return tema
        return None
    
    # modificar
    def modificarPorNumero(self, numero:int, nombre:str="", enunciado:str=""):
        for tema in self.__temas:
            if numero == tema.obtenerNumero():
                if nombre != "":
                    tema.establecerNombre(nombre)
                if enunciado != "":
                    tema.establecerEnunciado(enunciado)
                self.__guardarTodos()
                return True
        return False

    #existe
    def existeNumero(self, numero:int)->bool:
        for tema in self.__temas:
            if numero == tema.obtenerNumero():
                return True
        return False
    
    # agregar
    def agregar(self, tema_nuevo:Tema)->bool:
        if not self.existeNumero(tema_nuevo.obtenerNumero()):
            self.__temas.append(tema_nuevo)
            self.__guardarTodos()
            return True
        return False


    # eliminar
    def eliminar(self, numero:int):
        for tema in self.__temas:
            if numero == tema.obtenerNumero():
                self.__temas.remove(tema)
                self.__guardarTodos()