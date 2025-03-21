# **Explicación del Proyecto Validador de Datos Inmutable**

## **Área de Aplicación y Justificación**
El área de aplicación elegida es la **validación de hechizos en el universo de Harry Potter**, asegurando que los hechizos cumplan ciertas reglas:  
- La primer letra del nombre del hechizo debe estar en mayúsculas.  
- El nivel de dificultad del hechizo debe ser un número entre 1 y 5.  
- El tipo de uso debe ser válido (ataque, defensa, otro).  

Se eligió este tema porque combina **fantasía y programación**, aplicando validaciones en un contexto original y entretenido. 
Aunque no tiene una aplicación práctica en la vida real, me ayudó a comprender mejor el tema y relacionarlo con algo que me apasiona.

----------

## **Inmutabilidad y Pureza de las Funciones**
- **Inmutabilidad**: Se usan **tuplas** para almacenar los datos, asegurando que no sean modificados después de su creación.  
- **Pureza**: Las funciones reciben datos y devuelven valores nuevos sin alterar el estado global ni generar efectos secundarios.  
- Se utilizan `map()` y `filter()` para aplicar validaciones sin modificar los datos originales.  

Este enfoque garantiza un código **predecible, modular y reutilizable**, siguiendo los principios de la **programación funcional**.

------
##### Leysly Yarismet Mendoza Flores. #21100248.