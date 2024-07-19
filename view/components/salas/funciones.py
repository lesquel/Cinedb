import customtkinter as ctk
from Sillas import Sillas
from components.Text import Text
from components.Button import Button
from components.Comentarios import Comentarios
from hooks.Peticiones.GetSalas import GetSalas

def Funciones(parent, idUsuario, frame, ventana, funciones, info):
    """
    Display movie functions with options to view seat selection and comments.

    Args:
    - parent (tkinter.Frame): The parent frame to contain the movie function display.
    - idUsuario (int): The ID of the current user.
    - frame: The frame to destroy after selecting a function.
    - ventana: The main window or parent window object.
    - funciones (list): List of movie functions.
    - info (dict): Additional information about the movie.

    Returns:
    - None
    """
    # Function to navigate to seat selection window
    def Ventana(fun, info, funcion, sala):
        frame2 = Sillas(ventana, fun, info, idUsuario, funcion, sala)
    
    # Frame for movie functions
    frame1 = ctk.CTkFrame(parent)
    frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Function to iterate through movie functions and create frames
    def EjecutarFunciones():
        fila = 2
        columna = 0
        
        if not funciones:
            Text(parent=frame1, texto="No hay funciones", tamanio=20).grid(row=2, column=1, padx=10, pady=10)
            return
        
        for i, v in enumerate(funciones):
            if i % 3 == 0:
                fila += 1
                columna = 0
            
            # Create frame for each movie function
            f = ctk.CTkFrame(frame1, border_width=2, corner_radius=10)
            f.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")
            columna += 1

            # Get theater information
            sala = GetSalas(idSala=v["idSala"])

            # Display date and theater name
            Text(parent=f, texto=f"Fecha: {v['fecha']}", tamanio=16, row=0, column=0, padx=5, pady=5)
            Text(parent=f, texto=sala['nombre'], tamanio=16, row=1, column=0, padx=5, pady=5)

            # Button to view seat selection
            Button(parent=f, texto="Ver", tamanio=16, row=2, column=0, eventoClick=lambda fun=v, info=info, funcion=v, sala=sala: Ventana(fun, info, funcion, sala))

    EjecutarFunciones()

    # Frame for comments section
    frame2 = ctk.CTkFrame(parent)
    frame2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Display comments for the selected movie
    Comentarios(parent=frame2, idPelicula=info["id"], idUsuario=idUsuario)
