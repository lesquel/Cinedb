

def insertEstreno(idPelicula, ventana, infoUser, main_frame):
    """
    Inserta un nuevo estreno para una película mediante una solicitud GET a una API local.

    Args:
    - idPelicula (int): ID de la película para la cual se insertará el estreno.
    - ventana (tk.Tk): Ventana principal de la aplicación.
    - infoUser (dict): Información del usuario actual.
    - main_frame (tk.Frame): Marco principal de la interfaz gráfica donde se muestra la tabla de estrenos.

    Returns:
    - dict: Respuesta JSON de la API.

    """
    import requests
    from tkinter import messagebox
    # from components.tablaCrud.tablaStreno import TablaEstreno
    # Realizar la solicitud GET para insertar el estreno
    response = requests.get(f"http://localhost:8080/introEstrenos?idPelicula={idPelicula}")

    # Mostrar mensaje informativo de éxito
    messagebox.showinfo("Insertar Estreno", "El estreno se ha insertado correctamente")

    # Actualizar la tabla de estrenos en la interfaz gráfica
    # TablaEstreno(infoUser=infoUser, ventana=ventana, main_frame=main_frame)
    from TablaCrudPelicula import TablaCrudPelicula
    TablaCrudPelicula(ventana=ventana, infoUser=infoUser)

    # Retornar la respuesta JSON de la API
    return response.json()
