from components.Text import Text
from components.Button import Button
from components.Img import Img
import customtkinter as ctk
from Salas import Salas

def Pelicuas(parent, infoUser, frame, ventana, ifAdmin=False):
    """
    Display movies with options to view details or edit (admin only).

    Args:
    - parent (tkinter.Frame): The parent frame to contain the movie display.
    - infoUser (dict): Information about the current user.
    - frame: The frame to destroy after showing movie details.
    - ventana: The main window or parent window object.
    - ifAdmin (bool): Flag indicating if the current user is an admin (default is False).

    Returns:
    - None
    """
    def Ventana(infoPelicula, idUsuario):
        """
        Show theater details for the selected movie.

        Args:
        - infoPelicula (dict): Information about the selected movie.
        - idUsuario (int): The ID of the current user.

        Returns:
        - None
        """
        frame2 = Salas(ventana=ventana, infoPelicula=infoPelicula, idUsuario=idUsuario)
        frame.destroy()  # Destroy current frame after showing details
        frame2.grid(row=0, column=0, sticky="nsew")

    # Simulated movie data - replace with actual data retrieval
    from hooks.Peticiones.GetPeli import GetAllPeli
    peliculas = GetAllPeli(page=1, limit=4)

    fila = 1
    columna = 0

    # Iterate over movies to create display widgets
    for pelicula in peliculas:
        # Create a frame for the movie
        marco_pelicula = ctk.CTkFrame(parent, corner_radius=10, border_width=2)
        marco_pelicula.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

        # Display the image of the movie
        Img(marco_pelicula, pelicula["img"])

        # Create a frame for the name of the movie
        marco_nombre = ctk.CTkFrame(marco_pelicula)
        marco_nombre.grid(pady=(0, 10))

        # Display the name and duration of the movie
        Text(marco_nombre, texto=pelicula["nombre"], tamanio=16, row=0, column=0, padx=10, pady=10).grid(sticky="w")
        Text(marco_nombre, texto=f"Duración: {pelicula['dura']}H", tamanio=16, row=1, column=0, padx=10, pady=10).grid(sticky="w")

        # Button to view more details or edit the movie (admin only)
        if ifAdmin:
            Button(marco_pelicula, texto="Editar", tamanio=16, row=2, column=0, eventoClick=lambda infoPelicula=pelicula, idUsuario=infoUser["id"]: Ventana(infoPelicula, idUsuario))
        else:
            Button(marco_pelicula, texto="Ver", tamanio=16, row=2, column=0, eventoClick=lambda infoPelicula=pelicula, idUsuario=infoUser["id"]: Ventana(infoPelicula, idUsuario))

        # Update row and column positions
        columna += 1
        if columna >= 4:
            columna = 0
            fila += 1
