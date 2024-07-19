

def deleteEstreno(id, ventana, infoUser, main_frame):
    """
    Elimina un estreno de la base de datos y actualiza la tabla de estrenos en la interfaz gráfica.

    Args:
    - id: ID del estreno que se va a eliminar.
    - ventana: Ventana principal de la aplicación.
    - infoUser: Información del usuario actual.
    - main_frame: Marco principal de la aplicación donde se muestra la tabla de estrenos.

    Returns:
    - dict or None: Respuesta JSON de la API si la eliminación fue exitosa, None si se canceló la operación.
    """
    # Mostrar un mensaje de confirmación para la eliminación
    import requests
    from tkinter import messagebox
    # from components.tablaCrud.tablaStreno import TablaEstreno
    confirmar = messagebox.askyesno("Eliminar Estreno", "¿Estás seguro de eliminar el estreno?")
    
    if not confirmar:
        return None
    
    # Realizar la solicitud GET para eliminar el estreno por su ID
    url = f"http://localhost:8080/deleteEstrenos?id={id}"
    response = requests.get(url)
    
    # Actualizar la tabla de estrenos después de la eliminación
    # TablaEstreno(infoUser=infoUser, ventana=ventana, main_frame=main_frame)
    from TablaCrudPelicula import TablaCrudPelicula
    TablaCrudPelicula(ventana=ventana, infoUser=infoUser)
    
    return response.json()
