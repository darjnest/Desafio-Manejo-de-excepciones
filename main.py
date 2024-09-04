from foto import Foto
from error import DimensionError

try:
    foto = Foto(1200, 800, "100000.jpg")
    foto.ancho = 3000  # Esto lanzará una excepción DimensionError
except DimensionError as e:
    print(e)

    try:
        foto.alto = 0  # Esto también lanzará una excepción DimensionError
    except DimensionError as e:
        print(e)
