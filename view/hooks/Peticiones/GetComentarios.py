import requests

def GetComentarios(idPelicula):
    """
    Obtiene los comentarios asociados a una película específica.

    Args:
    - idPelicula (int): El ID de la película de la cual se desean obtener los comentarios.

    Returns:
    - dict: Un diccionario que contiene los datos de los comentarios obtenidos desde la API.

    """
    # Construir la URL para la solicitud GET
    url = f"http://localhost:8080/getComentario?idPelicula={idPelicula}"
    
    # Realizar la solicitud GET y obtener la respuesta
    response = requests.get(url)
    
    # Devolver los datos de los comentarios en formato JSON
    return response.json()
