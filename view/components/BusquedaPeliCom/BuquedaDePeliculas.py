import customtkinter as ctk
from components.Text import Text
from components.Button import Button
from components.Img import Img
from EditPeli_Admin import EditAdmin  # Assuming this imports an editing component
from Salas import Salas  # Assuming this imports a component for showing movie theaters

def BusquedaDePeliculas(parent, infoUser, busqueda, tipoDeBusqueda, peliculas, ventana):
    """
    Creates a display of movie information based on search results.

    Args:
    - parent (tkinter.Frame): The parent frame to contain the movie display.
    - infoUser (dict): Information about the current user.
    - busqueda (str): The search term used.
    - tipoDeBusqueda (str): The type of search performed.
    - peliculas (list): List of dictionaries containing movie information.
    - ventana: The main window or parent window object.

    Returns:
    - None
    """
    def Ventana(infoPelicula, idUsuario):
        """
        Opens a window to show theater details for the selected movie.

        Args:
        - infoPelicula (dict): Information about the selected movie.
        - idUsuario (int): The ID of the current user.

        Returns:
        - None
        """
        print(infoPelicula)  # Placeholder for future actions
        # Show the theater for the selected movie
        frame2 = Salas(ventana=ventana, infoPelicula=infoPelicula, idUsuario=idUsuario)

    def VentanaAdmin(infoPelicula, infoUser):
        """
        Opens a window for editing the selected movie (admin only).

        Args:
        - infoPelicula (dict): Information about the selected movie.
        - infoUser (dict): Information about the current user.

        Returns:
        - None
        """
        # Show the editing window for the selected movie
        frame2 = EditAdmin(ventana=ventana, infoUser=infoUser, infoPelicula=infoPelicula)

    # If there are no movies, do not display anything
    if not peliculas:
        return
    
    # Create a frame for displaying movies
    frame = ctk.CTkFrame(parent, corner_radius=20)
    frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    fila = 1
    columna = 0

    # Iterate over movies to create display widgets
    for pelicula in peliculas:
        # Create a frame for the movie
        marco_pelicula = ctk.CTkFrame(frame, corner_radius=10, border_width=2)
        marco_pelicula.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

        # Display the movie image
        Img(marco_pelicula, pelicula["img"])

        # Create a frame for the movie name
        marco_nombre = ctk.CTkFrame(marco_pelicula, fg_color="transparent") 
        marco_nombre.grid(row=1, column=0, pady=(0, 10))

        # Display the movie name and duration
        Text(marco_nombre, texto=pelicula["nombre"], tamanio=16).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        Text(marco_nombre, texto=f"Duración: {pelicula['dura']}H", tamanio=16).grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Button to view more details or edit the movie
        if infoUser["admin"]:
            # Button to edit the movie (admin only)
            Button(marco_pelicula, texto="Editar", tamanio=16, eventoClick=lambda infoPelicula=pelicula, infoUser=infoUser: VentanaAdmin(infoPelicula, infoUser)).grid(row=4, column=0, padx=10, pady=5)
        else:
            # Button to view the theater for the movie
            Button(marco_pelicula, texto="Ver", tamanio=16, eventoClick=lambda infoPelicula=pelicula, idUsuario=infoUser["id"]: Ventana(infoPelicula, idUsuario)).grid(row=4, column=0, padx=10, pady=5)
       
        # Update row and column positions
        columna += 1
        if columna >= 4:
            columna = 0
            fila += 1
