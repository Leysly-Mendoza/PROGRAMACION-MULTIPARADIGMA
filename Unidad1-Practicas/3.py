#3.Entrada de datos y manipulación. 
#Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de manera inversa letra por letra .

# Solicitar al usuario su nombre completo
nombre = input("Ingrese su nombre completo: ")

# Recorrer el nombre en orden inverso y mostrarlo letra por letra
print("Nombre invertido letra por letra:")
for letra in reversed(nombre):
    print(letra)
