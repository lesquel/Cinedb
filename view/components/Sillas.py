import customtkinter as ctk
def Sillas(parent, row, column, tamanio, bg_color="#888888", imagen_url=None):
    from components.ImgLocal import Img
    """
    Creates a button styled as a seat using customtkinter with a modern design.
    
    Args:
        parent (widget): The parent container for the button.
        row (int): The row in the grid of the container.
        column (int): The column in the grid of the container.
        tamanio (int): The font size of the button text.
        bg_color (str): The background color of the button.
        imagen_url (str): The URL or local path of the image to display on the button.

    Returns:
        btn (CTkButton): The created button.
    """
    img = Img(imagen_url, 50) if imagen_url else None
    
    btn = ctk.CTkButton(parent, 
                        image=img,
                        font=("Arial", tamanio),
                        text="",
                        border_width=3,
                        fg_color="transparent",
                        border_color=bg_color,
                        text_color="#000000",
                        height=100,  # Button width
                        corner_radius=10,  # Rounded corners for a smoother design
                        command=lambda: print("Button pressed"))  # Example function
    
    # Position the button in the grid
    btn.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")  # Add padding for spacing
    
    # Configurar el grid del parent para que la celda del botón pueda expandirse
    parent.grid_columnconfigure(column, weight=1)   
    parent.grid_rowconfigure(row, weight=1)

    return [btn, row, column]
