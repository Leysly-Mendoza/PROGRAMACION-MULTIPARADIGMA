#5 Manejo de información 
#Escribir una función que reciba n parámetros de llave valor e imprima la información en formato “{llave}”: “{Valor}”

def manejarInformacion(**kwargs):
    for llave, valor in kwargs.items():
        print(f'"{llave}": "{valor}"')

# Ejemplo de cómo utilizarlo:
manejarInformacion(nombre="Emilio", edad=21, numControl="21100540", especialidad="Desarollo")