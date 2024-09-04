from foto import Foto
from error import DimensionError

"""
Este programa permite al usuario ingresar las dimensiones de una foto (ancho y alto) y 
verifica si estas dimensiones son válidas según las reglas establecidas.
"""


def solicitar_medidas():
    """
    Función que solicita al usuario las medidas de ancho y alto de una foto.

    Retorna:
    - ancho: El valor ingresado por el usuario para el ancho.
    - alto: El valor ingresado por el usuario para el alto.
    """
    ancho = int(input("Ingresa el ancho de la foto: "))
    alto = int(input("Ingresa el alto de la foto: "))
    return ancho, alto


def main():
    """
    Función principal que ejecuta el programa.
    Permite al usuario ingresar las dimensiones de una foto e intenta crear una instancia de Foto.
    Si las dimensiones no son válidas, se captura y muestra un mensaje de error.
    """
    try:
        ancho, alto = solicitar_medidas()
        ruta = "ruta/a/la/imagen.jpg"  # Puedes cambiar la ruta según sea necesario
        foto = Foto(ancho, alto, ruta)
        print(
            f"Foto creada con éxito: Ancho={foto.ancho}, Alto={foto.alto}, Ruta={foto.ruta}"
        )

        # Solicitar nuevas dimensiones para probar los setters
        nuevo_ancho = int(input("Ingresa un nuevo ancho para la foto: "))
        foto.ancho = nuevo_ancho  # Esto lanzará una excepción si el ancho es inválido

        nuevo_alto = int(input("Ingresa un nuevo alto para la foto: "))
        foto.alto = nuevo_alto  # Esto lanzará una excepción si el alto es inválido

    except DimensionError as e:
        print(e)


if __name__ == "__main__":
    main()
