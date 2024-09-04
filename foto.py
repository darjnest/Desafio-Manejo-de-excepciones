from error import DimensionError


class Foto:
    """
    Clase que representa una foto con dimensiones y una ruta de almacenamiento.

    Atributos de clase:
    - MAX: El valor máximo permitido para las dimensiones de la foto (ancho y alto).
    """

    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        """
        Constructor de la clase Foto.

        Parámetros:
        - ancho: El ancho inicial de la foto.
        - alto: El alto inicial de la foto.
        - ruta: La ruta donde se almacena la foto.
        """
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        """
        Getter para el atributo 'ancho'.

        Retorna:
        - El ancho de la foto.
        """
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        """
        Setter para el atributo 'ancho'. Valida que el nuevo ancho esté dentro del rango permitido.

        Parámetros:
        - ancho: El nuevo valor para el ancho de la foto.

        Lanza:
        - DimensionError: Si el ancho está fuera del rango permitido (menor a 1 o mayor a MAX).
        """
        if ancho < 1 or ancho > self.MAX:
            raise DimensionError(
                "El ancho está fuera del rango permitido", "ancho", self.MAX
            )
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        """
        Getter para el atributo 'alto'.

        Retorna:
        - El alto de la foto.
        """
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        """
        Setter para el atributo 'alto'. Valida que el nuevo alto esté dentro del rango permitido.

        Parámetros:
        - alto: El nuevo valor para el alto de la foto.

        Lanza:
        - DimensionError: Si el alto está fuera del rango permitido (menor a 1 o mayor a MAX).
        """

        if alto < 1 or alto > self.MAX:
            raise DimensionError(
                "El alto está fuera del rango permitido", "alto", self.MAX
            )
        self.__alto = alto
