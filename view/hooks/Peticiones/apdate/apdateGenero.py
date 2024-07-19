

def apdateGenero(id, nombre, ventana, infoUser, ventanaHelp):
    """
    Actualiza un género mediante una solicitud GET a la API local y refresca la tabla de películas en la interfaz gráfica.

    Args:
    - id: ID del género a actualizar.
    - nombre: Nuevo nombre para el género.
    - ventana: Objeto ventana donde se muestra la interfaz gráfica.
    - infoUser: Información del usuario actual.
    - ventanaHelp: Ventana de ayuda que se cierra después de la actualización.

    Returns:
    - dict: Respuesta JSON de la solicitud GET.
    """
    # Cerrar la ventana de ayuda
    import requests
    from TablaCrudPelicula import TablaCrudPelicula
    ventanaHelp.destroy()

    # Construir la URL para la solicitud GET
    url = f"http://localhost:8080/updateGenero?id={id}&nombre={nombre}"

    # Realizar la solicitud GET a la API local
    response = requests.get(url)

    # Refrescar la tabla de películas en la interfaz gráfica
    TablaCrudPelicula(ventana=ventana, infoUser=infoUser)

    # Devolver la respuesta JSON de la solicitud GET
    return response.json()
