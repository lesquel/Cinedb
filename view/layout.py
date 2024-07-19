import customtkinter as ctk
from hooks.destuirTodo import destuirTodo

def Layout(ventana):
    """
    Configura y devuelve un marco de desplazamiento para una ventana dada.

    Args:
    - ventana: La ventana principal donde se colocará el marco de desplazamiento.

    Returns:
    - scroll_frame: El marco de desplazamiento configurado.
    """
    # Limpiar todo el contenido previo en la ventana
    destuirTodo(ventana)
    
    # Crear un marco de desplazamiento en lugar de un marco estándar
    scroll_frame = ctk.CTkScrollableFrame(ventana)
    scroll_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    
    # Configurar la expansión del marco de desplazamiento
    ventana.grid_rowconfigure(0, weight=1)  # Permitir que la fila 0 de la ventana se expanda verticalmente
    ventana.grid_columnconfigure(0, weight=1)  # Permitir que la columna 0 de la ventana se expanda horizontalmente
    
    return scroll_frame
