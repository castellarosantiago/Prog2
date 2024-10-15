from abc import ABC, abstractmethod

class Producto():
    def __init__(self, nombre:str, id:int, precio:float, stock:int):        
        self.__nombre = nombre
        self.__id = id
        self.__precio = precio
        self.__stock = stock

    def sePuedeVender(self) -> bool:
        if self.__stock > 0:
            print("Este producto esta en stock, se puede vender")
            return True 
        else:
            print("Este producto no esta en stock, no se puede vender")
            return False

    def calcularDescuento(self):
        return 0

    def actualizarStock(self):
            cantidad = int(input("Ingrese la cantidad a actualizar: "))
            if self.__stock + cantidad < 0:
                print("No se puede actualizar el stock a un valor negativo.")
            else:
                self.__stock += cantidad  # Actualiza el stock sumando la cantidad proporcionada
                print(f"Stock actualizado, el stock actual es de {self.__stock} unidades.")


    
    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerPrecio(self):
        return self.__precio
    
    def obtenerStock(self):
        return self.__stock
        
class Categoria():
    def __init__(self, id:int, nombre:str):
        self.__id = id
        self.__nombre = nombre
        self.__productos = []
    def agregarProducto(self, producto):
        if producto not in self.__productos:
            self.__productos.append(producto)

    def eliminarProducto(self, producto):
        if producto in self.__productos:
            self.__productos.remove(producto)


class Inventario():
    def __init__(self):
        self.__productos = []

    def agregarProducto(self, producto):
        self.__productos.append(producto)

    def mostrarInventario(self):
        for Producto in self.__productos:
            print(f"{Producto.obtenerNombre()} - Stock: {Producto.obtenerStock()} - Precio: {Producto.obtenerPrecio()}")
 
    pass

class Persona(ABC):
    def __init__(self, nombre:str, direccion:str, email:str):
        self._nombre = nombre
        self._direccion = direccion
        self._email = email

class Cliente():
    def __init__(self, nombre:str, direccion:str, email:str, historialDeCompras:list):
        super().__init__(nombre, direccion, email)
        self.__historialDeCompras = historialDeCompras

    def obtenerHistorialDeCompras(self):
        return self.__historialDeCompras