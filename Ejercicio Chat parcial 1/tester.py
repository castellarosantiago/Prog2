from tienda import Producto, Categoria, Inventario, Cliente

class Tester:
    def __init__(self):
        # Crear un producto
        self.producto1 = Producto("Laptop", 1, 1000.00, 10)

    def run_tests(self):
        print("=== Pruebas de Producto ===")
        print(f"Nombre: {self.producto1.obtenerNombre()}, Precio: {self.producto1.obtenerPrecio()}, Stock: {self.producto1.obtenerStock()}")
        
        # Llamar al método actualizarStock, que solicitará al usuario la cantidad
        self.producto1.actualizarStock()

        # Mostrar el stock actualizado
        print(f"Stock después de la actualización: {self.producto1.obtenerStock()}")

# Ejecutar el Tester
if __name__ == "__main__":
    tester = Tester()
    tester.run_tests()

