# Desafio-Manejo-de-excepciones

# Proyecto de Manejo de Excepciones - Galería de Fotos

Este proyecto es parte de un desafío que consiste en validar las dimensiones de una foto en una aplicación de galería. Se implementa una excepción personalizada para asegurar que las dimensiones de la foto (ancho y alto) estén dentro de un rango permitido.

## Descripción

El proyecto incluye dos archivos principales:

1. **`error.py`**: Define la excepción personalizada `DimensionError`, que se utiliza para manejar errores cuando las dimensiones de la foto están fuera de los límites permitidos.

2. **`foto.py`**: Contiene la clase `Foto`, que representa una foto con atributos de ancho, alto y ruta. Los métodos `setter` para los atributos de ancho y alto validan los valores y lanzan la excepción `DimensionError` si los valores están fuera del rango permitido.

3. **`main.py`**: Es el archivo principal que solicita al usuario las dimensiones de la foto, intenta crear una instancia de `Foto` y permite probar la validación de las dimensiones.

## Ejecución

Para ejecutar el programa:

1. Clona el repositorio y navega al directorio del proyecto.

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_DIRECTORIO>
   Ejecuta el archivo main.py para probar la funcionalidad.
   python main.py
   Ingresa las dimensiones de la foto cuando se te solicite y observa cómo se manejan las excepciones si se ingresan valores fuera del rango permitido.
   Ejemplo de Uso
   ```

Ingresa el ancho de la foto: 1200
Ingresa el alto de la foto: 800
Foto creada con éxito: Ancho=1200, Alto=800, Ruta=ruta/a/la/imagen.jpg
Ingresa un nuevo ancho para la foto: 3000
El ancho está fuera del rango permitido. Dimension: ancho, Valor máximo permitido: 2500.
Ingresa un nuevo alto para la foto: 0
El alto está fuera del rango permitido. Dimension: alto, Valor máximo permitido: 2500.
Requerimientos

Python 3.x
Autor

Carlos Silva Diaz
