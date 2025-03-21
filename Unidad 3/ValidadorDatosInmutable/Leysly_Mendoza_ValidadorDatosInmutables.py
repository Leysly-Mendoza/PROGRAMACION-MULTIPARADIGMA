from typing import Tuple

# Función pura para validar el nombre del hechizo
def validar_nombre_hechizo(nombre: str) -> bool:
    return nombre.istitle() and nombre.replace(" ", "").isalpha()

# Función pura para validar el nivel de dificultad del Hechizo (debe estar entre 1 y 5)
def validar_nivel_dificultad(nivel: int) -> bool:
    return isinstance(nivel, int) and 1 <= nivel <= 5

# Función pura para validar el uso permitido del hechizo
def validar_uso(uso: str) -> bool:
    usos_validos = ("Defensa", "Ataque", "Otro")
    return uso in usos_validos

# Datos de prueba inmutables
hechizos = (
    ("Expelliarmus", 2, "Defensa"),
    ("Avada Kedavra", 5, "Ataque"),
    ("Lumos", 1, "Otro"),
    ("sectumsempra", 4, "Ataque"),  # Incorrecto, debe empezar en mayúscula.
    ("Accio", 3, "Movimiento")  # Incorrecto, uso no válido.
)

# Validación usando map() para aplicar funciones sin modificar la tupla original
resultados = list(map(lambda h: (
    validar_nombre_hechizo(h[0]), 
    validar_nivel_dificultad(h[1]), 
    validar_uso(h[2])
), hechizos))

# Mostrar los resultados
for hechizo, resultado in zip(hechizos, resultados):
    print(f"Hechizo: {hechizo[0]}, Nivel: {hechizo[1]}, Uso: {hechizo[2]} -> Validez: {resultado}")

# Filtrar solo los hechizos válidos usando filter()
hechizos_validos = tuple(filter(lambda h: all([
    validar_nombre_hechizo(h[0]), 
    validar_nivel_dificultad(h[1]), 
    validar_uso(h[2])
]), hechizos))

print("\nHechizos válidos:", hechizos_validos)
