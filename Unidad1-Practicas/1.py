#1 Funciones con n parámetros 
#Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el producto total. 
def producto_total(*numeros):
    """Calcula el producto de varios números."""
    producto = 1
    for num in numeros:
        producto *= num
    return producto

# Ejemplo de uso
print("El producto total es:", producto_total(2, 3, 4))
