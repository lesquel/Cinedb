import requests
from tkinter import messagebox
from index import Index

def apdatePeli(infoPelicula, infoUser, ventana):
    """
    Actualiza la información de una película mediante una solicitud GET a la API local y muestra un mensaje de éxito.

    Args:
    - infoPelicula: Diccionario con la información de la película a actualizar, incluyendo ID, nombre, imagen, descripción, duración, trailers y ID de género.
    - infoUser: Información del usuario actual.
    - ventana: Objeto ventana donde se muestra la interfaz gráfica.

    Returns:
    - dict: Respuesta JSON de la solicitud GET.
    """
    # Construir la URL para la solicitud GET
    url = f"http://localhost:8080/updatePelicula?id={infoPelicula['id']}&nombre={infoPelicula['nombre']}&img={infoPelicula['img']}&descri={infoPelicula['descri']}&dura={infoPelicula['dura']}&trailers={infoPelicula['trailers']}&genero_id={infoPelicula['genero_id']}"

    # Realizar la solicitud GET a la API local
    response = requests.get(url)

    # Mostrar mensaje de éxito
    messagebox.showinfo("Actualizar", "La actualización se realizó con éxito")

    # Volver a la pantalla principal index, asumiendo que es la interfaz de inicio
    Index(ventana=ventana, infoUser=infoUser)

    # Devolver la respuesta JSON de la solicitud GET
    return response.json()
