

def Administrar(ventana, infoUser):
    """
    Función para crear la interfaz de administración con menús laterales y gráficos.

    Args:
    - ventana: La ventana principal de la aplicación.
    - infoUser: Información del usuario actual.

    Returns:
    - frame: El marco principal que contiene la interfaz de administración.
    """
    # Crear el marco principal
    import customtkinter as ctk
    from datos.UrlImgs import UrlIcos
    from layout import Layout
    from components.administrar.infoAdministrar import infoAdministrar
    from TablaCrudPelicula import TablaCrudPelicula
    from TablaCurdSalas import TablaCrudSalas
    from TablaCurdFunciones import TablaCrudFunciones
    from components.Graficos import Graficos
    from components.Nav import NavAdmin, Nav

    frame = Layout(ventana=ventana)

    # Crear marco para administrar películas, salas y funciones
    frameAdministrar = ctk.CTkFrame(frame)
    frameAdministrar.grid(row=0, column=1, padx=40, pady=40, sticky="nsew")
    frameAdministrar.grid_columnconfigure(1, weight=1)  # Aseguramos que la columna 1 se expanda

    # Añadir el menú lateral según el tipo de usuario
    if infoUser["admin"]:
        NavAdmin(frame, [{"ventana": ventana, "infoUser": infoUser}])
    else:
        Nav(frame, [{"ventana": ventana, "infoUser": infoUser}])

    # Crear título para la sección de administración
    ctk.CTkLabel(frameAdministrar, text="Administrar", font=("Arial", 24), corner_radius=20).grid(row=0, column=0, padx=10, pady=10)

    # Crear secciones para administrar películas, salas y funciones
    peliculas = infoAdministrar(frameAdministrar, infoFrame={"nombre": "Peliculas", "img": UrlIcos["funciones"], "row": 1, "column": 1}, VentanaAbrir=lambda: TablaCrudPelicula(ventana=ventana, infoUser=infoUser))
    salas = infoAdministrar(frameAdministrar, infoFrame={"nombre": "Salas", "img": UrlIcos["salas"], "row": 1, "column": 2}, VentanaAbrir=lambda: TablaCrudSalas(ventana=ventana, infoUser=infoUser))
    funciones = infoAdministrar(frameAdministrar, infoFrame={"nombre": "Funciones", "img": UrlIcos["movie"],  "row": 1, "column": 3}, VentanaAbrir=lambda: TablaCrudFunciones(ventana=ventana, infoUser=infoUser))

    # Crear marco para gráficos
    frameGraficos = ctk.CTkFrame(frame)
    frameGraficos.grid(row=1, column=1, padx=40, pady=40, sticky="nsew")

    # Título para la sección de gráficos
    ctk.CTkLabel(frameGraficos, text="Gráficos", font=("Arial", 24), corner_radius=20).grid(row=0, column=0, padx=10, pady=10)

    # Crear gráficos con datos predefinidos
    Graficos(frameGraficos, data=[10, 20, 15, 25, 30], labels=['Batman', 'Spiderman', 'Superman', 'Wonder Woman', 'Iron Man'], row=1, column=1, title="Peliculas mas vistas", x_label="Peliculas", y_label="Vistas")
    Graficos(frameGraficos, data=[10, 20, 15, 25], labels=['Sala 1', 'Sala 2', 'Sala 3', 'Sala 4'], row=2, column=1, title="Sala mas usada", x_label="Salas", y_label="Usos")
    Graficos(frameGraficos, data=[10, 20, 15, 25, 30], labels=['18', '20', '33', '24', '12'], row=3, column=1, title="Rango de Edad de Usuarios", x_label="Usuarios", y_label="Edad")

    return frame
