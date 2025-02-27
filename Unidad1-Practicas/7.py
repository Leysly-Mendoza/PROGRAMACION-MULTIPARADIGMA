#7 Formateo y conversiones 
#Escribir un programa que muestre un menú con 2 opciones la primera opción
#“1.- Imprimir YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la 
#fecha del día de hoy en el formato seleccionado.
from datetime import datetime

def obtenerFecha(op):
    hoy = datetime.today()
    if op == "1":
        return hoy.strftime("%Y/%m/%d")
    elif op == "2":
        return hoy.strftime("%m/%d/%Y")
    else:
        return "Opción inválida"

print("Teclee una opción:")
print("1.- Imprimir YYYY/MM/DD")
print("2.- Imprimir MM/DD/YYYY")

op = input("Teclee 1 o 2: ") 

print("Fecha:", obtenerFecha(op)) # Obtener e imprimir la fecha en el formato seleccionado