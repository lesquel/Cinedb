import customtkinter as ctk
from tkinter import StringVar  # Importar StringVar para variables de texto
from hooks.destuirTodo import destuirTodo

def EditAdmin(ventana, infoUser, infoPelicula):
    """
    Función para crear la interfaz de edición de información de una película para administradores.

    Args:
    - ventana: La ventana principal de la aplicación.
    - infoUser: Información del usuario actual.
    - infoPelicula: Información de la película a editar.

    Returns:
    - frame: El marco principal que contiene la interfaz de edición de película.
    """
    # Importar componentes necesarios
    from components.Text import Text
    from components.Button import Button
    from components.Img import Img
    from components.Regresar import RegresarFunc
    from layout import Layout

    # Crear el marco principal
    frame = Layout(ventana)

    # Marco principal dentro del layout
    frame_main = ctk.CTkFrame(frame)
    frame_main.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")

    # Sub-marcos para diferentes secciones de edición
    frame_info = ctk.CTkFrame(frame_main)
    frame_info.grid(row=1, column=0, padx=40, pady=40, sticky="nsew")

    # Marco para nombre y descripción
    frame_name_desc = ctk.CTkFrame(frame_info)
    frame_name_desc.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Marco para duración, trailers y género
    frame_others = ctk.CTkFrame(frame_info)
    frame_others.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # Marco para el botón de guardar cambios
    frame_button = ctk.CTkFrame(frame_info)
    frame_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    # Variables de texto para editar
    nombre_var = StringVar(value=infoPelicula["nombre"])
    duracion_var = StringVar(value=infoPelicula["dura"])
    trailers_var = StringVar(value=infoPelicula["trailer"])
    
    # Texto actual para la descripción
    descripcion_text = infoPelicula["descri"]

    # Mostrar la imagen de la película
    Img(frame_main, infoPelicula["img"])

    # Etiquetas y campos de entrada para nombre y descripción
    label_nombre = ctk.CTkLabel(frame_name_desc, text="Nombre:", font=("Arial", 16), width=200, height=35)
    label_nombre.grid(row=0, column=0, padx=10, pady=10)
    entry_nombre = ctk.CTkEntry(frame_name_desc, textvariable=nombre_var, width=200, height=35)
    entry_nombre.grid(row=0, column=1, padx=10, pady=10)

    label_descripcion = ctk.CTkLabel(frame_name_desc, text="Descripción:", font=("Arial", 16), width=200, height=35)
    label_descripcion.grid(row=1, column=0, padx=10, pady=10)
    textbox_descripcion = ctk.CTkTextbox(frame_name_desc, width=400, height=100)
    textbox_descripcion.grid(row=1, column=1, padx=10, pady=10)
    textbox_descripcion.insert("1.0", descripcion_text)
    textbox_descripcion.configure(wrap='word')

    # Etiquetas y campos de entrada para duración y trailers
    label_duracion = ctk.CTkLabel(frame_others, text="Duración: (en horas)", font=("Arial", 16), width=200, height=35)
    label_duracion.grid(row=0, column=0, padx=10, pady=10)
    entry_duracion = ctk.CTkEntry(frame_others, textvariable=duracion_var, width=200, height=35)
    entry_duracion.grid(row=0, column=1, padx=10, pady=10)

    label_trailers = ctk.CTkLabel(frame_others, text="Trailers:", font=("Arial", 16), width=200, height=35)
    label_trailers.grid(row=1, column=0, padx=10, pady=10)
    entry_trailers = ctk.CTkEntry(frame_others, textvariable=trailers_var, width=200, height=35)
    entry_trailers.grid(row=1, column=1, padx=10, pady=10)

    # Componente personalizado para seleccionar género
    from components.GeneroEntry import GeneroEntry, obtener_id_genero
    genero_var, genero_menu, entries = GeneroEntry(parent=frame_others, campos=["", "", ""], entries={}, valorPordefecto=infoPelicula["genero"])

    def guardar_cambios():
        # Obtener los valores actualizados para la película
        new_info_pelicula = {
            "id": infoPelicula["id"],
            "nombre": nombre_var.get(),
            "descri": textbox_descripcion.get("1.0", "end-1c"),  # Obtener el texto de la caja de texto
            "dura": duracion_var.get(),
            "img": infoPelicula["img"],
            "trailers": trailers_var.get(),
            "genero_id": obtener_id_genero(genero_var.get())
        }
        
        # Llamar a la función de actualización de película
        from hooks.Peticiones.apdate.apdatePeli import apdatePeli
        apdatePeli(infoPelicula=new_info_pelicula, infoUser=infoUser, ventana=ventana)

    # Botón para guardar los cambios
    Button(frame_button, texto="Guardar", tamanio=16, row=0, column=0, eventoClick=guardar_cambios)

    # Función para regresar a la pantalla anterior
    from index import Index
    RegresarFunc(frame_actual=frame_main, funcion_retorno=lambda: Index(ventana=ventana, infoUser=infoUser))

    return frame
