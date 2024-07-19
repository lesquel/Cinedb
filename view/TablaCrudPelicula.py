import customtkinter as ctk
from layout import Layout
from components.Regresar import RegresarFunc

from components.tablaCrud.tablaPelicula import TablaPelicula
from components.tablaCrud.tablaGenero import TablaGenero
from components.tablaCrud.tablaStreno import TablaEstreno

def TablaCrudPelicula(ventana, infoUser):
    """
    Crea una interfaz de tabla CRUD para gestionar películas, géneros y estrenos.

    Args:
    - ventana: Objeto ventana donde se colocará la interfaz.
    - infoUser: Información del usuario actual.

    Returns:
    - main_frame: Marco principal que contiene la interfaz de tabla CRUD.
    """

    # Crear el marco principal utilizando Layout
    from Administrar import Administrar
    main_frame = Layout(ventana)

    # Configuración del grid para expansión
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)

    # Botón para regresar a la pantalla anterior
    RegresarFunc(main_frame, lambda: Administrar(ventana=ventana, infoUser=infoUser))

    frame_Main_pelicula = ctk.CTkFrame(main_frame)
    frame_Main_pelicula.grid(row=0, column=0, columnspan=2, padx=20, pady=40, sticky="nsew")
    title_Main_pelicula = ctk.CTkLabel(frame_Main_pelicula, text="Películas", font=("Arial", 24), corner_radius=20)
    title_Main_pelicula.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    # Frame para la tabla CRUD de Películas
    framePelicula = ctk.CTkFrame(frame_Main_pelicula)
    framePelicula.grid(row=1, column=0, columnspan=2, padx=20, pady=40, sticky="nsew")
    framePelicula.grid_columnconfigure(0, weight=1)
    framePelicula.grid_columnconfigure(1, weight=1)
    TablaPelicula(main_frame=framePelicula, infoUser=infoUser, ventana=ventana)

    frame_Main_genero = ctk.CTkFrame(main_frame)
    frame_Main_genero.grid(row=1, column=0, columnspan=2, padx=20, pady=40, sticky="nsew")
    title_Main_genero = ctk.CTkLabel(frame_Main_genero, text="Géneros", font=("Arial", 24), corner_radius=20)
    title_Main_genero.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    # Frame para la tabla CRUD de Géneros
    frameGenero = ctk.CTkFrame(frame_Main_genero)
    frameGenero.grid(row=1, column=0, columnspan=2, padx=20, pady=40, sticky="nsew")
    TablaGenero(main_frame=frameGenero, infoUser=infoUser, ventana=ventana)

    frame_Main_estreno = ctk.CTkFrame(main_frame)
    frame_Main_estreno.grid(row=2, column=0, columnspan=2, padx=20, pady=40, sticky="nsew")
    title_Main_estreno = ctk.CTkLabel(frame_Main_estreno, text="Estrenos", font=("Arial", 24), corner_radius=20)
    title_Main_estreno.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    # Frame para la tabla CRUD de Estrenos
    frameEstreno = ctk.CTkFrame(frame_Main_estreno)
    frameEstreno.grid(row=1, column=0, padx=20, pady=40, sticky="nsew")
    TablaEstreno(main_frame=frameEstreno, infoUser=infoUser, ventana=ventana)

    return main_frame
