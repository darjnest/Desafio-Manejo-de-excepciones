class DimensionError(Exception):
    def __init__(self, mensaje: str, dimension: str = None, maximo: int = None) -> None:
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

        def __str__(self) -> str:
            if self.dimension and self.maximo:
                return f"{self.mensaje}. Dimension: {self.dimension}, Valor máximo permitido: {self.maximo}."
            elif self.dimension:
                return f"{self.mensaje}, Dimension: {self.dimension}."
            elif self.maximo:
                return f"{self.mensaje}, Valor maximo permitido: {self.maximo}."
            else:
                return super().__str__()
