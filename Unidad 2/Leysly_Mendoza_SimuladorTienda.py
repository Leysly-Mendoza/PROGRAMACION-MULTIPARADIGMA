import unittest

#Clase Producto
"""
Producto es la clase base de Producto que engloba tanto productos físicos y digitales. 
"""
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.stock = stock
    
    @property
    def precio(self):
        return self.__precio
    
    def disponible(self):
        return self.stock > 0
    
    def calcular_costo(self):
        return self.precio
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"

#Clase Producto Digital
"""
Producto Digital representa un producto digital sin stock físico y hereda de la clase Producto. 
"""
class ProductoDigital(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio, stock=-1)  
    
    def calcular_costo(self):
        return self.precio * 0.9 #10% de descuento
    
    def disponible(self):
        return True  # Siempre disponible
    
    def __str__(self):
        return f"{self.nombre} (Digital) - ${self.calcular_costo()}"

#Clase Cliente
"""
Representa a un cliente de la tienda.
"""
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        
    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"

#Clase Carrito
"""
Simula un carrito de compras donde se agregan productos.
"""
class Carrito:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        if producto.disponible():
            self.productos.append(producto)
            if producto.stock > 0:
                producto.stock -= 1
            print(f"{producto.nombre} agregado al carrito.")
        else:
            print(f"No hay stock disponible para {producto.nombre}.")

    def calcular_total(self):
        return sum(p.calcular_costo() for p in self.productos)
    
    def __str__(self):
        return "\n".join(str(p) for p in self.productos) or "Carrito vacío"

#Clase Tienda 
"""
Representa la tienda, donde se pueden agregar prudctos al catalogo, buscar productos y realizar compras.
"""
class Tienda:
    def __init__(self):
        self.catalogo = []
    
    def agregar_al_catalogo(self, producto):
        self.catalogo.append(producto)
        print(f"{producto.nombre} agregado al catálogo.")
    
    def buscar_producto(self, nombre):
        for producto in self.catalogo:
            if producto.nombre == nombre:
                return producto
        return None
    
    def realizar_compra(self, cliente, carrito):
        if not carrito.productos:
            return "Compra cancelada: carrito vacío."
        total = carrito.calcular_total()
        return f"Compra realizada por {cliente.nombre}:\n{carrito}\nTotal: ${total}"

# Pruebas unitarias de la clase Carrito con el módulo unittest. 
class PruebasCarrito(unittest.TestCase):
    def test_carrito_vacio(self):
        carrito = Carrito()
        self.assertEqual(carrito.calcular_total(), 0)
    
    def test_calcular_total(self):
        carrito = Carrito()
        libro = Producto("Harry Potter y el caliz de fuego", 399, 5)
        digital = ProductoDigital("Curso en linea", 99)
        digital2 = ProductoDigital("Harry Potter y el caliz de fuego", 299)
        carrito.agregar_producto(libro)
        carrito.agregar_producto(digital)
        carrito.agregar_producto(digital2)
        self.assertEqual(carrito.calcular_total(), 399 + (99 + 299) * 0.9)  # 797

if __name__ == '__main__':
    unittest.main()