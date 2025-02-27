#6 Razonamiento y prueba de código 
#Escribir un programa que reciba un numero entre 0 y 20 e imprimir el numero en letra,
#no utilizar condicionales, máximo 5 líneas de código.

def regresarLetra(num):
    numerosLetra = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve",
                    "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte"]
    print(numerosLetra[num])

# Ejemplo de cómo utilizarlo
regresarLetra(0)  # La salida es Cero
regresarLetra(5)  # La salida es Cinco
regresarLetra(20)  # La salida es Veinte