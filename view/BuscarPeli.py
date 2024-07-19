
def BuscarPeli(ventana, infoUser, busqueda, tipoDeBusqueda):
    """
    Función para crear la pantalla de búsqueda de películas según criterios.

    Args:
    - ventana: La ventana principal de la aplicación.
    - infoUser: Información del usuario actual.
    - busqueda: Término de búsqueda (nombre de película o ID de género).
    - tipoDeBusqueda: Tipo de búsqueda ("pelicula" o "genero").

    Returns:
    - frame: El marco principal que contiene la interfaz de búsqueda de películas.
    """
    from components.GeneroEntry import obtener_id_genero
    import customtkinter as ctk
    from layout import Layout
    from hooks.Peticiones.getGenero import getAllGeneros
    from hooks.Peticiones.GetPeli import GetPeliByGenero, GetPeliByNombre
    from components.Regresar import RegresarFunc
    from components.BusquedaPeliCom.BuquedaDePeliculas import BusquedaDePeliculas

    # Crear el marco principal
    from index import Index
    from components.Nav import NavAdmin, Nav
    frame = Layout(ventana)

    # Determinar el menú lateral según el tipo de usuario
    if infoUser["admin"]:
        NavAdmin(frame, [{"ventana": ventana, "infoUser": infoUser}])
    else:
        Nav(frame, [{"ventana": ventana, "infoUser": infoUser}])

    # Crear marco para el contenido principal
    frameMain = ctk.CTkFrame(frame)
    frameMain.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # Encabezado con logo y botón de regresar
    frameHeader = ctk.CTkFrame(frameMain)
    frameHeader.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    ctk.CTkLabel(frameHeader, text="Intercine", font=("Arial", 24), corner_radius=20).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    RegresarFunc(frameHeader, lambda: Index(ventana, infoUser))

    # Formulario de búsqueda
    frameForm = ctk.CTkFrame(frameHeader)
    frameForm.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    entry_buscar = ctk.CTkEntry(frameForm)
    entry_buscar.grid(row=0, column=0, padx=10, pady=10)

    def buscar_peliculas(termino):
        if tipoDeBusqueda == "pelicula":
            BuscarPeli(ventana=ventana, infoUser=infoUser, busqueda=termino, tipoDeBusqueda="pelicula")
        elif tipoDeBusqueda == "genero":
            BuscarPeli(ventana=ventana, infoUser=infoUser, busqueda=termino, tipoDeBusqueda="genero")

    btn_buscar = ctk.CTkButton(frameForm, text="Buscar", command=lambda: buscar_peliculas(entry_buscar.get()))
    btn_buscar.grid(row=0, column=1, padx=10, pady=10)

    # ComboBox para seleccionar géneros
    generos = getAllGeneros()
    generosEntry = ctk.CTkComboBox(frameForm, values=[f"{g['nombre']} ({g['id']})" for g in generos], state="readonly")
    generosEntry.grid(row=0, column=2, padx=10, pady=10)

    def buscar_peliculasGenero(termino):
        generoId = obtener_id_genero(seleccion=termino)
        BuscarPeli(ventana=ventana, infoUser=infoUser, busqueda=generoId, tipoDeBusqueda="genero")

    btn_Entry_buscar = ctk.CTkButton(frameForm, text="Buscar", command=lambda: buscar_peliculasGenero(generosEntry.get()))
    btn_Entry_buscar.grid(row=0, column=3, padx=10, pady=10)

    # Etiqueta de información de búsqueda
    ctk.CTkLabel(frameForm, text=f"Busqueda: ({busqueda})", font=("Arial", 24), corner_radius=20).grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Marco scrollable para el contenido principal de películas
    framePeliculas = ctk.CTkFrame(frameMain)
    framePeliculas.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    # Función para validar si hay resultados de búsqueda
    def validacion_busqueda(busqueda, infoPelicula):
        if infoPelicula is None:
            ctk.CTkLabel(framePeliculas, text="No hay resultados", font=("Arial", 24), corner_radius=20).grid(row=1, column=0, columnspan=3, padx=10, pady=10)
            return False
        return True

    # Obtener y mostrar resultados de búsqueda según el tipo de búsqueda
    if tipoDeBusqueda == "genero":
        peliculas = GetPeliByGenero(idGenero=busqueda)
        if not validacion_busqueda(busqueda=entry_buscar.get(), infoPelicula=peliculas):
            return frame
        BusquedaDePeliculas(parent=framePeliculas, infoUser=infoUser, busqueda=busqueda, tipoDeBusqueda=tipoDeBusqueda, peliculas=peliculas, ventana=ventana)
        return frame

    if tipoDeBusqueda == "pelicula":
        if busqueda == "":
            ctk.CTkLabel(framePeliculas, text="No hay película a buscar", font=("Arial", 24), corner_radius=20).grid(row=1, column=0, columnspan=3, padx=10, pady=10)
            return frame
        peliculas = GetPeliByNombre(nombre=busqueda)
        if not validacion_busqueda(busqueda=entry_buscar.get(), infoPelicula=peliculas):
            return frame
        BusquedaDePeliculas(parent=framePeliculas, infoUser=infoUser, busqueda=busqueda, tipoDeBusqueda=tipoDeBusqueda, peliculas=peliculas, ventana=ventana)
        return frame

    return frame
