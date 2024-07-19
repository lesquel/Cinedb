
def insertGenero(nombre, ventana, infoUser):
    """
    Inserta un nuevo género mediante una solicitud GET a una API local.

    Args:
    - nombre (str): Nombre del género que se va a agregar.
    - ventana: Objeto ventana donde se está realizando la inserción.
    - infoUser: Información del usuario actual.

    Returns:
    - dict: Respuesta JSON de la API sobre el resultado de la inserción del género.

    Note:
    - Esta función espera que la API responda adecuadamente a la solicitud GET para insertar el género.
    """
    import requests
    from TablaCrudPelicula import TablaCrudPelicula

    # Construir la URL para la solicitud GET
    url = f"http://localhost:8080/introGenero?nombre={nombre}"
    
    # Enviar la solicitud GET a la API
    response = requests.get(url)
    
    # Actualizar la tabla de géneros en la interfaz gráfica
    TablaCrudPelicula(ventana=ventana, infoUser=infoUser)
    
    # Retornar la respuesta JSON de la API
    return response.json()
