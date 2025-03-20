# 🛒 Simulador de Tienda Online 🛒
Simulador de tienda online desarrollado en Python, que incluye funcionalidades de gestión de productos, carritos de compra y clientes. Además, cuenta con pruebas unitarias para asegurar el correcto funcionamiento del sistema.

## 📦 **Clases y Funcionalidad** 📦

### **1. Producto**
- Representa un producto físico.
- **Atributos:** `nombre`, `precio`, `stock`
- **Métodos:**
  - `calcular_costo()`: Devuelve el precio del producto.
  - `disponible()`: Verifica si hay stock disponible.
  - `__str__()`: Muestra la información del producto.

---

### **2. ProductoDigital (Hereda de Producto)**
- Representa un producto digital con un descuento del 10%.
- **Atributos:** `nombre`, `precio`, `stock=-1`
- **Métodos:**
  - `calcular_costo()`: Aplica un 10% de descuento al precio.
  - `disponible()`: Siempre devuelve `True`.
  - `__str__()`: Muestra la información con el precio actualizado.

---

### **3. Cliente**
- Representa un cliente que realiza compras.
- **Atributos:** `nombre`, `email`
- **Métodos:**
  - `__str__()`: Muestra los datos del cliente.

---

### **4. Carrito**
- Simula un carrito de compras.
- **Atributos:** `productos` (lista de productos)
- **Métodos:**
  - `agregar_producto(producto)`: Agrega productos al carrito si hay stock disponible.
  - `calcular_total()`: Calcula el total del carrito.
  - `__str__()`: Muestra los productos agregados o un mensaje de carrito vacío.

---

### **5. Tienda**
- Administra los productos y las compras.
- **Atributos:** `catalogo` (lista de productos)
- **Métodos:**
  - `agregar_al_catalogo(producto)`: Agrega un producto al catálogo.
  - `buscar_producto(nombre)`: Busca un producto por su nombre.
  - `realizar_compra(cliente, carrito)`: Procesa la compra.

---

## 🧪 **Pruebas Unitarias** 🧪

Las pruebas se realizaron con el módulo `unittest`.
Se implementaron dos pruebas principales para la clase `Carrito`:
1. **Carrito Vacío:** Verifica que el total sea **0** cuando no hay productos.
2. **Carrito con Productos:** Calcula el total correctamente al agregar productos físicos y digitales.

Para ejecutar las pruebas:
```bash
python Leysly_Mendoza_SimuladorTienda.py
```

---

## 🚀 **Cómo Ejecutar el Proyecto** 🚀

1. Ejecuta el programa:
```bash
python Leysly_Mendoza_SimuladorTienda.py
```
2. Para ejecutar las pruebas unitarias:
```bash
python -m unittest Leysly_Mendoza_SimuladorTienda.py
python -m unittest pruebas.py
```

---

¡Gracias! 😊

