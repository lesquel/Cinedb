

def deleteGenero(id, main_frame, infoUser, ventana):
    """
    Elimina un género de la base de datos y actualiza la tabla de géneros en la interfaz gráfica.

    Args:
    - id: ID del género que se va a eliminar.
    - main_frame: Marco principal de la aplicación donde se muestra la tabla de géneros.
    - infoUser: Información del usuario actual.
    - ventana: Ventana principal de la aplicación.

    Returns:
    - JSON: Respuesta de la solicitud HTTP DELETE.

    Notes:
    - Realiza una solicitud HTTP DELETE para eliminar el género por su ID.
    - Después de la eliminación, actualiza la tabla de géneros en la interfaz gráfica llamando a TablaGenero.
    """
    import requests
    from components.tablaCrud.tablaGenero import TablaGenero
    # Realizar la solicitud DELETE para eliminar el género por su ID
    url = f"http://localhost:8080/deleteGenero?id={id}"
    response = requests.delete(url)
    
    # Actualizar la tabla de géneros en la interfaz gráfica
    TablaGenero(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    
    return response.json()
