# view/components/Comentarios.py
from hooks.destuirTodo import destuirTodo
from components.Text import Text
import customtkinter as ctk
from components.Button import Button
from hooks.Peticiones.GetComentarios import GetComentarios
from hooks.Peticiones.insert.insertComentario import insertComentario
from hooks.Peticiones.GetUser import GetUserId

def Comentarios(parent, idPelicula, idUsuario):
    """
    Función para mostrar comentarios de una película y permitir añadir nuevos comentarios.

    Parameters:
    - parent (ctk.CTkFrame): El contenedor donde se mostrarán los comentarios.
    - idPelicula (int/str): Identificador de la película.
    - idUsuario (int/str): Identificador del usuario actual.
    """
    destuirTodo(parent)
    
    comentarios = GetComentarios(idPelicula)

    # Crear el marco principal
    frame = ctk.CTkFrame(parent, corner_radius=10, border_width=2)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Crear el marco del formulario para añadir comentarios
    frameForm = ctk.CTkFrame(frame, corner_radius=10, border_width=2)
    frameForm.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    entry_comentario = ctk.CTkEntry(frameForm, placeholder_text="Escribe un comentario...", width=750, height=40)
    entry_comentario.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    Button(parent=frameForm, texto="Enviar", tamanio=16, row=1, column=0, eventoClick=lambda: insertComentario(idPelicula=idPelicula, comentario=entry_comentario.get(), parent=parent, idUsuario=idUsuario))

    # Crear el marco para mostrar todos los comentarios
    frameTodosLosComentarios = ctk.CTkFrame(parent, corner_radius=10, border_width=2)
    frameTodosLosComentarios.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    frameTodosLosComentarios.grid_rowconfigure(0, weight=1)
    frameTodosLosComentarios.grid_columnconfigure(0, weight=1)
    frameTodosLosComentarios.grid_columnconfigure(1, weight=1)

    Text(parent=frameTodosLosComentarios, texto="Comentarios", tamanio=20, row=0, column=0, padx=10, pady=10)

    fila = 0
    columna = 0
    if comentarios is None:
        return

    for i, comentario in enumerate(comentarios):
        # Crear el marco para cada comentario
        f = ctk.CTkFrame(frameTodosLosComentarios, border_width=2, corner_radius=10)
        f.grid(row=fila + 1, column=columna, padx=10, pady=10, sticky="nsew")
        f.grid_rowconfigure(0, weight=1)
        f.grid_columnconfigure(0, weight=1)

        # Mostrar el comentario
        Text(parent=f, texto=comentario["comentario"], tamanio=18, row=0, column=0, padx=10, pady=10)

        # Mostrar el nombre del usuario que escribió el comentario
        user = GetUserId(comentario["id_usuario"])
        Text(parent=f, texto=f"Escrito por: {user['name']}", tamanio=16, row=1, column=0, padx=10, pady=10)

        # Ajustar la fila y columna para la siguiente iteración
        if columna == 1:
            fila += 1
            columna = 0
        else:
            columna += 1
