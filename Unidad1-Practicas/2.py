#2 Manejo y manipulación de elementos de una lista 
#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3,
#y muestre por pantalla la lista resultante. 

# Crear la lista con el abecedario
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Eliminar las letras en posiciones múltiples de 3 (en índices 2, 5, 8, 11, 14, ...)
i = len(abecedario) - 1
while i >= 0:
    if (i + 1) % 3 == 0:  # Si la posición es múltiplo de 3
        abecedario.pop(i)  # Eliminar la letra en esa posición
    i -= 1  # Retroceder al siguiente índice

# Mostrar la lista resultante
print(abecedario)
