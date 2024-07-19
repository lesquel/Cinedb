import customtkinter as ctk
import threading
from layout import Layout
from components.index.pelicuas import Pelicuas
from components.index.estrenos import Estrenos
from BuscarPeli import BuscarPeli
from hooks.Peticiones.getGenero import getAllGeneros
from components.Nav import Nav, NavAdmin

def Index(ventana, infoUser):
    """
    Función para crear la pantalla principal de la aplicación.

    Args:
    - ventana: La ventana principal de la aplicación.
    - infoUser: Información del usuario actual.
    - ifAdmin: Booleano que indica si el usuario es administrador o no. Por defecto es False.

    Returns:
    - frame: El marco principal que contiene la pantalla principal de la aplicación.
    """
    # Crear el marco principal
    frame = Layout(ventana)

    # Crear el menú lateral según el tipo de usuario
    if infoUser["admin"]:
        NavAdmin(frame, [{"ventana": ventana, "infoUser": infoUser}])
    else:
        Nav(frame, [{"ventana": ventana, "infoUser": infoUser}])

    # Marco principal para el contenido
    frame_main = ctk.CTkFrame(frame)
    frame_main.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # Encabezado de la aplicación
    frame_header = ctk.CTkFrame(frame_main)
    frame_header.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    ctk.CTkLabel(frame_header, text="Intercine", font=("Arial", 24), corner_radius=20).grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # Formulario de búsqueda por nombre de película
    frame_form = ctk.CTkFrame(frame_header)
    frame_form.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    entry_buscar = ctk.CTkEntry(frame_form)
    entry_buscar.grid(row=0, column=0, padx=10, pady=10)

    def buscar_peliculas(termino):
        # Crear un nuevo hilo para la búsqueda
        threading.Thread(target=BuscarPeli, args=(ventana, infoUser, termino, "pelicula")).start()

    btn_buscar = ctk.CTkButton(frame_form, text="Buscar", command=lambda: buscar_peliculas(entry_buscar.get()))
    btn_buscar.grid(row=0, column=1, padx=10, pady=10)

    # Combo box para buscar por género
    generos = getAllGeneros()
    generos_combo = ctk.CTkComboBox(frame_form, values=[f"{g['nombre']} ({g['id']})" for g in generos], state="readonly")
    generos_combo.grid(row=0, column=2, padx=10, pady=10)

    def buscar_peliculas_genero(termino):
        from components.GeneroEntry import obtener_id_genero
        generoId = obtener_id_genero(seleccion=termino)
        threading.Thread(target=BuscarPeli, args=(ventana, infoUser, generoId, "genero")).start()

    btn_buscar_genero = ctk.CTkButton(frame_form, text="Buscar", command=lambda: buscar_peliculas_genero(generos_combo.get()))
    btn_buscar_genero.grid(row=0, column=3, padx=10, pady=10)

    # Frame para mostrar los estrenos
    frame_estrenos = ctk.CTkFrame(frame_main)
    frame_estrenos.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
    Estrenos(frame_estrenos, infoUser, ventana, page=1)

    # Frame scrollable para mostrar las películas principales
    frame_peliculas = ctk.CTkFrame(frame_main)
    frame_peliculas.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)
    Pelicuas(frame_peliculas, infoUser, ventana, page=1)

    return frame