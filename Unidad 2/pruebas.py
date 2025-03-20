import unittest
from Leysly_Mendoza_SimuladorTienda import Producto, ProductoDigital, Cliente, Carrito, Tienda

class TestTienda(unittest.TestCase):
    
    def setUp(self):
        self.tienda = Tienda()
        self.camisa = Producto("Camisa", 99, 10)
        self.camaraDigital = ProductoDigital("Camara", 500)
        self.pantalon = Producto("Pantalon", 250, 2)
        
        self.tienda.agregar_al_catalogo(self.camisa)
        self.tienda.agregar_al_catalogo(self.camaraDigital)
        self.tienda.agregar_al_catalogo(self.pantalon)

        self.cliente = Cliente("Leysly", "Leysly@gmail.com")
        self.carrito = Carrito()

    def test_agregar_al_catalogo(self):
        self.assertEqual(len(self.tienda.catalogo), 3)
        self.assertEqual(self.tienda.catalogo[0].nombre, "Camisa")
        self.assertEqual(self.tienda.catalogo[1].nombre, "Camara")
        self.assertEqual(self.tienda.catalogo[2].nombre, "Pantalon")
    
    def test_buscar_producto_existente(self):
        producto = self.tienda.buscar_producto("Camisa")
        self.assertIsNotNone(producto)
        self.assertEqual(producto.nombre, "Camisa")
    
    def test_buscar_producto_no_existente(self):
        producto = self.tienda.buscar_producto("Zapato")
        self.assertIsNone(producto)

    def test_realizar_compra_carrito_vacio(self):
        resultado = self.tienda.realizar_compra(self.cliente, self.carrito)
        self.assertEqual(resultado, "Compra cancelada: carrito vacío.")

    def test_realizar_compra_con_productos(self):
        self.carrito.agregar_producto(self.tienda.buscar_producto("Camisa"))
        self.carrito.agregar_producto(self.tienda.buscar_producto("Camara"))
        resultado = self.tienda.realizar_compra(self.cliente, self.carrito)
        self.assertIn("Compra realizada por Leysly", resultado)
        self.assertIn("Total: $549.0", resultado)

    def test_validar_stock(self):
        self.carrito.agregar_producto(self.tienda.buscar_producto("Pantalon"))
        self.carrito.agregar_producto(self.tienda.buscar_producto("Pantalon"))
        self.carrito.agregar_producto(self.tienda.buscar_producto("Pantalon"))  #No hay stock disponible para Pantalon.
        self.assertEqual(len(self.carrito.productos), 2)

if __name__ == '__main__':
    unittest.main()

"""
Pruebas Unitarias:
 - setUp(): Configura el entorno de prueba creando una instancia de la tienda (Tienda).
 - Agrega tres productos (uno físico con stock, uno digital y otro físico con poco stock).
 - Crea un cliente (Cliente) y un carrito de compras (Carrito).

test_agregar_al_catalogo(): Verifica que los productos se agreguen correctamente al catálogo.
 - Comprueba que la cantidad de productos sea 3 y que sus nombres sean los esperados.

test_buscar_producto_existente()
 - Busca un producto por nombre (Camisa) y verifica que se encuentre correctamente.
 - Comprueba que el producto devuelto no sea None.

test_buscar_producto_no_existente()
 - Intenta buscar un producto que no existe (Zapato) y verifica que retorne None.

 test_realizar_compra_carrito_vacio()
 - Intenta realizar una compra con un carrito vacío.
 - Verifica que el mensaje de cancelación de compra sea el correcto.

test_realizar_compra_con_productos()
 - Agrega productos al carrito (Camisa y Camara) y realiza una compra.
 - Comprueba que el mensaje incluya el nombre del cliente y el total correcto ($549.0).

test_validar_stock()
 - Agrega productos al carrito verificando el control de stock (Pantalon con solo 2 unidades).
 - Intenta agregar una tercera unidad, pero verifica que no se agregue por falta de stock.
 - Comprueba que solo haya 2 productos en el carrito.

"""