#4.Entrada de datos y estructuración. 
#Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture las materias y 
#créditos de su semestre preferido (inferior a 8vo) al final imprimir en el formato “{asignatura}” tiene “{créditos}” créditos. 
#Y la suma de todos los créditos del semestre.

# Crear un diccionario vacío para almacenar materias y créditos
materias = {}

# Capturar el número de materias
num_materias = int(input("Ingrese la cantidad de materias de su semestre: "))

# Pedir los datos de cada materia
for i in range(num_materias):
    asignatura = input(f"Ingrese el nombre de la materia {i + 1}: ")
    creditos = int(input(f"Ingrese los créditos de {asignatura}: "))
    materias[asignatura] = creditos

# Mostrar las materias con sus créditos
print("\nResumen del semestre:")
total_creditos = 0
for asignatura, creditos in materias.items():
    print(f'La materia "{asignatura}" tiene "{creditos}" créditos.')
    total_creditos += creditos

# Mostrar el total de créditos
print(f"\nTotal de créditos del semestre: {total_creditos}")