import customtkinter as ctk

def Text(parent, texto, tamanio, row=0, column=0, pady=10, padx=20):
    """
    Crea y coloca un CTkLabel con el texto y tamaño especificados en la cuadrícula de su marco padre.

    Args:
        parent (CTkFrame): El marco padre donde se añadirá el label.
        texto (str): El texto a mostrar en el label.
        tamanio (int): El tamaño de la fuente del texto.
        row (int, optional): La fila de la cuadrícula donde se colocará el label. Por defecto es 0.
        column (int, optional): La columna de la cuadrícula donde se colocará el label. Por defecto es 0.
        pady (int, optional): El padding vertical del label. Por defecto es 10.
        padx (int, optional): El padding horizontal del label. Por defecto es 20.

    Returns:
        CTkLabel: El label creado y colocado en la cuadrícula.
    """
    # Creación de un CTkLabel con estilo moderno
    label = ctk.CTkLabel(parent, 
                         text=texto, 
                         font=("Arial", tamanio), 
                         pady=pady, 
                         padx=padx,
                         bg_color="transparent")

    # Configuración de la posición del label en la cuadrícula
    label.grid(row=row, column=column, sticky="w", padx=padx, pady=pady)

    return label
