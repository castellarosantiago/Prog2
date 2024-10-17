from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre: str, precio: float, tasaImpuesto: float) -> None:
        self._nombre = nombre
        self._precio = precio
        self._tasaImpuesto = tasaImpuesto

    @abstractmethod
    def calcularImpuesto(self) -> float:
        pass

    def obtenerNombre(self) -> str:
        return self._nombre

    def obtenerPrecio(self) -> float:
        return self._precio
    def obtenerTasaImpuesto(self) -> float:
        return self._tasaImpuesto

class ProductoNacional(Producto):
    def __init__(self, nombre: str, precio: float, tasaImpuesto: float):
        super().__init__(nombre, precio, tasaImpuesto)

    def calcularImpuesto(self) -> float:
        return self._precio * self._tasaImpuesto

    def __str__(self) -> str:
        return f"{self.obtenerNombre()} (Nacional): Impuesto = $ {self.calcularImpuesto()}"


class ProductoImportado(Producto):
    def __init__(self, nombre: str, precio: float, tasaImpuesto: float, tasaArancel: float):
        super().__init__(nombre, precio, tasaImpuesto)
        self.__tasaArancel = tasaArancel

    def calcularImpuesto(self) -> float:
        impuesto = self._precio * self._tasaImpuesto  
        arancel = self._precio * self.__tasaArancel
        return impuesto + arancel

    def __str__(self) -> str:
        return f"{self.obtenerNombre()} (Importado): Impuesto = $ {self.calcularImpuesto()}"


class ProductoDeLujo(Producto):
    def __init__(self, nombre: str, precio: float, tasaImpuesto: float, tasaImpuestoDeLujo: float) -> None:
        super().__init__(nombre, precio, tasaImpuesto)
        self.__tasaImpuestoDeLujo = tasaImpuestoDeLujo

    def calcularImpuesto(self) -> float:
        impuesto = self._precio * self._tasaImpuesto
        impuestoDeLujo = self._precio * self.__tasaImpuestoDeLujo
        return impuesto + impuestoDeLujo

    def __str__(self) -> str:
        return f"{self.obtenerNombre()} (De Lujo): Impuesto = $ {self.calcularImpuesto()}"

