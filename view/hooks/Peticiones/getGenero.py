import requests

def getGenero(idGenero):
    """
    Obtiene información detallada de un género específico por su ID.

    Args:
    - idGenero (int): El ID del género del cual se desea obtener la información.

    Returns:
    - dict: Un diccionario con los datos del género obtenidos desde la API.
            Si no se encuentra el género, devuelve un diccionario vacío.
    """
    # Realizar la solicitud GET para obtener un género por su ID
    response = requests.get(f"http://localhost:8080/getGenero?id={idGenero}")
    
    # Convertir la respuesta JSON en un diccionario de Python
    genero = response.json()
    
    return genero

def getAllGeneros():
    """
    Obtiene todos los géneros disponibles en la base de datos.

    Returns:
    - list: Una lista de diccionarios que contienen los datos de todos los géneros obtenidos desde la API.
    """
    # Realizar la solicitud GET para obtener todos los géneros
    response = requests.get(f"http://localhost:8080/getAllGenero")
    
    # Convertir la respuesta JSON en una lista de diccionarios de Python
    generos = response.json()
    
    return generos
