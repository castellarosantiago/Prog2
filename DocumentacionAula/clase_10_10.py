from abc import ABC,abstractmethod
class Console:
    def __init__(self, marca:str, modelo:str, capacidad:float, cantJoystick:int, id:int):
        self._marca = marca
        self._modelo = modelo
        self._capacidad = capacidad
        self._cantJoystick = cantJoystick
        self._id = id
    def __str__(self) -> str:
        return  f"{self._marca} {self._modelo} con {self._cantJoystick} joysticks"
    def obtenerMarca(self):
        return self._marca
    def obtenerModelo(self):
        return self._modelo
    def obtenerCapacidad(self):
        return self._capacidad
    def obtenerCantJoystick(self):
        return self._cantJoystick
    def obtenerId(self):
        return self._id

class Videojuego(ABC):
    def __init__(self, nombre:str, genero:str, descripcion:str, añolanzamiento:int ,multijugador: bool, plataforma:str, id:int):
        self._nombre = nombre
        self._genero = genero
        self._descripcion = descripcion
        self._multijugador = multijugador
        self._añoLanzamiento = añolanzamiento
        self._plataforma = plataforma
        self._id = id
    def obtenerNombre(self):
        return self._nombre
    def obtenerGenero(self):
        return self._genero
    def obtenerDescripcion(self):
        return self._descripcion
    def obtenerMultijugador(self):
        return self._multijugador
    def obtenerAñoLanzamiento(self):
        return self._añoLanzamiento
    def obtenerPlataforma(self):
        return self._plataforma
    def __str__(self) -> str:
        return "{ " + self._nombre + ", " + self._descripcion
    @abstractmethod
    def sePuedeVender() -> bool: 
        pass        

class VideojuegoFisico(Videojuego):
    def __init__(self, nombre: str, genero: str, descripcion: str, añolanzamiento: int, multijugador: bool, plataforma: str, id: int,precio:float ,stock:int):
        super().__init__(nombre, genero, descripcion, añolanzamiento, multijugador, plataforma, id)
        self.__precio = precio
        self.__stock = stock
    def obtenerPrecio(self):
        return self.__precio
    def obtenerStock(self):
        return self.__stock
    def sePuedeVender(self) -> bool:
        return self.__stock>0
    def __str__(self) -> str:
        return super().__str__() +" stock " + str(self.__stock)

class VideojuegoDigital(Videojuego):
    def __init__(self, nombre: str, genero: str, descripcion: str, añolanzamiento: int, multijugador: bool, plataforma: str, id: int,tamaño:float,distribuidora:str):
        super().__init__(nombre, genero, descripcion, añolanzamiento, multijugador, plataforma, id)
        self.__tamaño = tamaño
        self.__distribuidora = distribuidora
    def obtenerTamaño(self):
        return self.__tamaño
    def obtenerDistribuidora(self):
        return self.__distribuidora
    def sePuedeVender(self) -> bool:
        return True
    
class TiendaDeVideojuegos():
    def __init__(self):
        self.__videojuegos = [Videojuego]
        self.__consolas =[Console]
    def agregarVideojuego(self,videojuego:Videojuego):
        self.__videojuegos.append(videojuego)
    def agregarConsola(self,consola:Console):
        self.__consolas.append(consola)
    def __str__(self) -> str:
        for videojuego in self.__videojuegos:
            print(videojuego)
        return ""

class Item():
    def __init__(self, juego:Videojuego, cantidad:int, id:int):
        self.__juego = juego
        self.__cantidad = cantidad
        self.__id = id
    def precioTotal(self):
        return self.__juego.obtenerPrecio() * self.__cantidad
    
class Compra():
    def __init__(self,formaPago:str,fecha:str):
        
        self.__formaPago = formaPago
        self.__fecha = fecha
        self.__items=[]
    def agregarItem(self,item:Item):
        self.__items.append(item)
    def preciototal(self):
        preciototal=0
        for item in self.__items:
            preciototal += item.precioTotal()
        return preciototal
        
        
class Cliente:
    def __init__(self, nombre:str, direccion:str, email:str):
        
        self.__nombre = nombre
        self.__direccion = direccion
        self.__email = email
        self.__historial_compras = []
        
    def comprar(self, compras:Compra):
        self.__historial_compras.append(compras)    
    def obtenerHistorialCompras(self):
        return self.__historial_compras
    def obtenerNombre(self):
        return self.__nombre
    def obtenerDirecion(self):
        return self.__direccion
    def obtenerEmail(self):
        return self.__email

miconsola= Console("sony","Playstation 5",500,2,1)
miviedejuegofisico= VideojuegoFisico("god of war","figthing","Es el god of war",2023,False,"sony",1,70,100)
miviedejuegodigital = VideojuegoDigital("god of war","figthing","Es el god of war",2023,False,"sony",1,18875,"Steam")
mitienda= TiendaDeVideojuegos()
mitienda.agregarVideojuego(miviedejuegodigital)
mitienda.agregarVideojuego(miviedejuegofisico)
miclient= Cliente("juan","calle falsa 123","emailfalso@gmail.com")
micompra= Compra("Efectivo","2022-12-25")
micompra.agregarItem(Item(miviedejuegofisico,2,1))

print (mitienda)
print (micompra.preciototal())
#TypeError: Can't instantiate abstract class Videojuego with abstract method sePuedeVender