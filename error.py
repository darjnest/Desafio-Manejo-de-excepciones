class DimensionError(Exception):
    """
    Excepción personalizada para manejar errores relacionados con dimensiones fuera del rango permitido.

    Atributos:
    - mensaje: El mensaje de error a mostrar.
    - dimension: La dimensión que causó el error (ancho o alto).
    - maximo: El valor máximo permitido para la dimensión.
    """

    def __init__(self, mensaje: str, dimension: str = None, maximo: int = None) -> None:
        """
        Constructor de la excepción DimensionError.

        Parámetros:
        - mensaje: El mensaje de error.
        - dimension: (Opcional) La dimensión que causó el error.
        - maximo: (Opcional) El valor máximo permitido para la dimensión.
        """
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

        def __str__(self) -> str:
            """
            Sobrecarga del método __str__ para personalizar el mensaje de la excepción.

            Retorna:
            - Un mensaje de error que incluye la dimensión y el valor máximo permitido si están disponibles.
            """
            if self.dimension and self.maximo:
                return f"{self.mensaje}. Dimension: {self.dimension}, Valor máximo permitido: {self.maximo}."
            elif self.dimension:
                return f"{self.mensaje}, Dimension: {self.dimension}."
            elif self.maximo:
                return f"{self.mensaje}, Valor maximo permitido: {self.maximo}."
            else:
                return super().__str__()
