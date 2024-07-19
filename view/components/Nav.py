import customtkinter as ctk

def crear_boton(parent, texto, comando):
    """
    Crea un botón CTkButton con el texto y comando especificados y lo agrega al contenedor padre.

    Args:
        parent (CTkFrame): El contenedor donde se añadirá el botón.
        texto (str): El texto que se mostrará en el botón.
        comando (function): La función que se ejecutará al hacer clic en el botón.

    Returns:
        CTkButton: El botón creado.
    """
    boton = ctk.CTkButton(parent, text=texto, fg_color="#333333", corner_radius=10,
                          font=("Arial", 20), width=220, height=40, command=comando, hover_color="blue")
    boton.grid(padx=10, pady=5, sticky="ew")
    return boton

def Nav(frame, ventanas):
    """
    Crea un menú lateral dentro del marco dado.

    Args:
        frame (CTkFrame): El marco principal donde se añadirá el menú lateral.
        ventanas (list): Lista de diccionarios con información de las ventanas y usuarios.
    """
    from index import Index
    from Perfil import Perfil
    from login import login

    # Crear el marco para el menú lateral
    sidebar = ctk.CTkFrame(frame, width=220)
    sidebar.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

    # Añadir botones al menú lateral utilizando la función crear_boton
    crear_boton(sidebar, "Inicio", lambda: Index(ventana=ventanas[0]["ventana"], infoUser=ventanas[0]["infoUser"]))
    crear_boton(sidebar, "Perfil", lambda: Perfil(ventana=ventanas[0]["ventana"], infoUser=ventanas[0]["infoUser"]))
    crear_boton(sidebar, "Ajustes", lambda: print("Ajustes presionado"))
    crear_boton(sidebar, "Cerrar Sesión", lambda: login(ventanas[0]["ventana"]))

    return sidebar

def NavAdmin(frame, ventanas):
    """
    Crea un menú lateral dentro del marco dado, añadiendo una opción adicional para la administración.

    Args:
        frame (CTkFrame): El marco principal donde se añadirá el menú lateral.
        ventanas (list): Lista de diccionarios con información de las ventanas y usuarios.
    """
    from Administrar import Administrar

    # Crear el menú lateral utilizando la función Nav
    sidebar = Nav(frame=frame, ventanas=ventanas)

    # Añadir botón de administración al menú lateral
    crear_boton(sidebar, "Administrar", lambda: Administrar(ventana=ventanas[0]["ventana"], infoUser=ventanas[0]["infoUser"]))
