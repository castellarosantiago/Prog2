from Apellido_Nombre_X import Producto, ProductoDeLujo, ProductoImportado, ProductoNacional

class Tester:
    def __init__(self):
        # Lista para guardar todos los productos que vayamos agregando
        self.productos = []

    def agregar_producto(self, producto: Producto):
        # Agregamos un producto a la lista de productos
        self.productos.append(producto)

    def mostrar_impuestos(self):
        # Recorremos todos los productos y mostramos su nombre y el impuesto calculado
        for producto in self.productos:
            print(producto)


# Pruebas con la clase Tester
if __name__ == "__main__":
    tester = Tester()

    # Creamos un producto nacional: Café con un precio de 100 y tasa de impuesto del 15%
    producto_nacional = ProductoNacional("Cafe", 100, 0.15)

    # Creamos un producto importado: Perfume con un precio de 200, tasa de impuesto del 20%, y arancel del 5%
    producto_importado = ProductoImportado("Perfume", 200, 0.20, 0.05)

    # Creamos un producto de lujo: Reloj con un precio de 500, tasa de impuesto del 10%, y un impuesto extra de lujo del 15%
    producto_de_lujo = ProductoDeLujo("Reloj", 500, 0.10, 0.15)

    # Agregamos cada producto a nuestra lista de pruebas
    tester.agregar_producto(producto_nacional)
    tester.agregar_producto(producto_importado)
    tester.agregar_producto(producto_de_lujo)

    # Mostramos los impuestos calculados para cada uno de los productos
    tester.mostrar_impuestos()
