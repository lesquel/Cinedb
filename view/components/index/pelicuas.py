import customtkinter as ctk
from components.Text import Text
from components.Button import Button
from components.Img import Img
from hooks.Peticiones.GetPeli import GetAllPeli
from EditPeli_Admin import EditAdmin
from Salas import Salas

def Pelicuas(parent, infoUser, ventana, page=1):
    """
    Display all movies with options for admin and users.

    Args:
    - parent (tkinter.Frame): The parent frame to contain the movie display.
    - infoUser (dict): Information about the current user.
    - ventana: The main window or parent window object.
    - page (int): The page number of movies to fetch (default is 1).

    Returns:
    - None
    """
    from hooks.destuirTodo import destuirTodo
    destuirTodo(ventana=parent)

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

    # Get movies for the current page
    peliculas = GetAllPeli(page=page, limit=8)

    # If no movies, display a message
    if not peliculas:
        ctk.CTkLabel(parent, text="No hay películas", font=("Arial", 24), corner_radius=20).grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        return

    # Add title to the framePeliculas
    ctk.CTkLabel(parent, text="Todas las películas", font=("Arial", 24), corner_radius=20).grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # Create a frame for movies
    frame = ctk.CTkFrame(parent, corner_radius=20)
    frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    fila = 1
    columna = 0

    # Iterate over movies to create display widgets
    for pelicula in peliculas:
        # Create a frame for the movie
        marco_pelicula = ctk.CTkFrame(frame, corner_radius=10, border_width=2)
        marco_pelicula.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

        # Display the image of the movie
        Img(marco_pelicula, pelicula["img"])

        # Create a frame for the name of the movie
        marco_nombre = ctk.CTkFrame(marco_pelicula, fg_color="transparent") 
        marco_nombre.grid(row=1, column=0, pady=(0, 10))

        # Display the name and duration of the movie
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

    # Create pagination buttons if more pages are available
    paginacion_frame = ctk.CTkFrame(parent)
    paginacion_frame.grid(row=fila+1, column=0, pady=10, sticky="nsew")

    # Check if there are more movies on the next page
    hay_mas_peliculas = GetAllPeli(page=page+1, limit=4)

    # Previous Button
    if page > 1:
        btn_anterior = Button(paginacion_frame, texto="Anterior", tamanio=16, eventoClick=lambda: Pelicuas(parent, infoUser, ventana, page=page-1))
        btn_anterior.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Next Button
    if hay_mas_peliculas:
        btn_siguiente = Button(paginacion_frame, texto="Siguiente", tamanio=16, eventoClick=lambda: Pelicuas(parent, infoUser, ventana, page=page+1))
        btn_siguiente.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
