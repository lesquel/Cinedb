import requests
from customtkinter import CTkImage
from PIL import Image

def Img(url_or_path, size=75):
    """
    Función para cargar una imagen desde una URL o una ruta local, redimensionarla y 
    convertirla en un objeto CTkImage.

    Parámetros:
    - url_or_path (str): URL o ruta del archivo de la imagen.
    - size (int): Tamaño al que se redimensionará la imagen (por defecto 75).

    Retorna:
    - CTkImage: Imagen convertida a objeto CTkImage, redimensionada al tamaño especificado.
    """
    
    try:
        # Intentar abrir la imagen desde una URL
        response = requests.get(url_or_path, stream=True)
        image = Image.open(response.raw)
    except (requests.exceptions.MissingSchema, OSError):
        # Si falla, intentar abrirla como archivo local
        image = Image.open(url_or_path)
    
    # Redimensionar la imagen al tamaño especificado
    resized_image = image.resize((size, size))
    
    # Convertir la imagen PIL a un objeto CTkImage
    ctk_image = CTkImage(light_image=resized_image, dark_image=resized_image, size=(size, size))
    
    return ctk_image
