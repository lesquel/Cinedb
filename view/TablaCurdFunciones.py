import customtkinter as ctk
from layout import Layout
from components.Regresar import RegresarFunc
from Administrar import Administrar
from components.tablaCrud.tablaFunciones import TablaFunciones

def TablaCrudFunciones(ventana, infoUser):
    """
    Crea una interfaz de tabla CRUD para gestionar funciones de cine.

    Args:
    - ventana: Objeto ventana donde se colocará la interfaz.
    - infoUser: Información del usuario actual.

    Returns:
    - main_frame: Marco principal que contiene la interfaz de tabla CRUD para funciones.
    """

    # Crear el marco principal utilizando Layout
    main_frame = Layout(ventana)

    # Configuración del grid para expansión
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)

    # Botón para regresar a la pantalla anterior
    RegresarFunc(main_frame, lambda: Administrar(ventana=ventana, infoUser=infoUser))

    # Frame para la tabla CRUD de Funciones
    frameFunciones = ctk.CTkFrame(main_frame)
    frameFunciones.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")
    frameFunciones.grid_columnconfigure(0, weight=1)
    frameFunciones.grid_columnconfigure(1, weight=1)
    TablaFunciones(main_frame=frameFunciones, infoUser=infoUser, ventana=ventana)

    return main_frame
