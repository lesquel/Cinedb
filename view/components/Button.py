import customtkinter as ctk

def Button(parent, texto, tamanio, row=0, column=0, columnspan=1, eventoClick=None):
    """
    Crea un botón estilizado con customtkinter.

    Args:
        parent (widget): El contenedor padre para el botón.
        texto (str): El texto que se mostrará en el botón.
        tamanio (int): El tamaño de la fuente del texto del botón.
        row (int): La fila en la cuadrícula del contenedor.
        column (int): La columna en la cuadrícula del contenedor.
        columnspan (int): El número de columnas que el botón abarcará.
        bg (str): El color de fondo del botón.
        eventoClick (func): La función que se ejecutará cuando se haga clic en el botón.
    """
    button = ctk.CTkButton(
        parent,
        text=texto,
        command=eventoClick,
        font=("Arial", tamanio),
        corner_radius=10,  # Añadir esquinas redondeadas para un diseño más moderno
        text_color="#ffffff",
        fg_color="blue"  # Establecer el color del texto
    )
    button.grid(row=row, column=column, columnspan=columnspan, padx=20, pady=10)
    return button
