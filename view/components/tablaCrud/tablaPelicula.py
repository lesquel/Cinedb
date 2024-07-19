import customtkinter as ctk
from components.Button import Button
from hooks.destuirTodo import destuirTodo
from hooks.Peticiones.GetPeli import GetAllPeli
from EditPeli_Admin import EditAdmin
from hooks.Peticiones.delete.deletePeli import eliminar_pelicula
from hooks.Peticiones.insert.insertPelicula import insertPelicula
from components.GeneroEntry import GeneroEntry
from components.AbrirImg import ImgAbrir

# Variable para rastrear la página actual
current_page = 1

def TablaPelicula(main_frame, infoUser, ventana, page=1):
    """
    Función para mostrar una tabla de películas con opciones de editar, eliminar, agregar y paginación.

    Parameters:
    - main_frame (ctk.CTkFrame): Marco principal donde se mostrará la tabla.
    - infoUser (dict): Información del usuario actual.
    - ventana (Tk.Tk): Ventana principal de la aplicación.
    - page (int): Página actual de la paginación (por defecto es 1).

    Returns:
    - None
    """
    # Limpiar el contenido anterior del marco principal
    destuirTodo(ventana=main_frame)
    
    # Establecer la página actual
    global current_page
    current_page = page

    # Configurar el grid para expandir las columnas
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=0)  # Columna fija para los datos principales
    main_frame.grid_columnconfigure(1, weight=1)  # Columna expandible para los detalles de la película
    main_frame.grid_columnconfigure(2, weight=0)  # Columna fija para el formulario de ingreso

    # Crear marco para las columnas fijas (id, nombre, img + botones de acción)
    fixed_columns_frame = ctk.CTkFrame(main_frame)
    fixed_columns_frame.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")

    # Crear encabezados fijos para id, nombre, img, editar y eliminar
    fixed_headers = ["id", "nombre", "Editar", "Eliminar"]
    for col, header in enumerate(fixed_headers):
        label = ctk.CTkLabel(fixed_columns_frame, text=header.capitalize(), font=('Arial', 12, 'bold'))
        label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")
    
    # Crear marco scrollable para las demás columnas (img, genero, duracion, trailer, descripcion)
    scrollable_frame = ctk.CTkScrollableFrame(main_frame, orientation="horizontal", width=500)
    scrollable_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    # Crear encabezados scrollable para las columnas restantes
    scrollable_headers = ["img", "genero", "duracion", "trailer", "descripcion"]
    for col, header in enumerate(scrollable_headers):
        label = ctk.CTkLabel(scrollable_frame, text=header.capitalize(), font=('Arial', 12, 'bold'))
        label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")
    
    # Obtener películas para mostrar en la tabla
    peliculas = GetAllPeli(page=page, limit=8)
    
    # Manejar caso cuando no hay películas para mostrar
    if not peliculas:
        print("No hay más datos para mostrar")
        return
    
    # Función para abrir la ventana de edición de una película
    def editar_pelicula(pelicula):
        EditAdmin(ventana=ventana, infoUser=infoUser, infoPelicula=pelicula)
        # Aquí se puede añadir lógica adicional para editar la película

    # Insertar datos en la tabla fija (id, nombre, img y botones de acción)
    for row, pelicula in enumerate(peliculas, start=1):
        fixed_data = [pelicula["id"], pelicula["nombre"]]
        for col, dato in enumerate(fixed_data):
            cell = ctk.CTkLabel(fixed_columns_frame, text=str(dato), font=('Arial', 12))
            cell.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")
        
        # Botón Editar
        edit_button = ctk.CTkButton(fixed_columns_frame, text="Editar", command=lambda p=pelicula: editar_pelicula(p))
        edit_button.grid(row=row, column=len(fixed_data), padx=10, pady=5)
        
        # Botón Eliminar
        delete_button = ctk.CTkButton(fixed_columns_frame, text="Eliminar", command=lambda p=pelicula: eliminar_pelicula(p, main_frame=main_frame, ventana=ventana, infoUser=infoUser))
        delete_button.grid(row=row, column=len(fixed_data) + 1, padx=10, pady=5)
    
    # Insertar datos en la tabla scrollable para las demás columnas
    for row, pelicula in enumerate(peliculas, start=1):
        scrollable_data = [pelicula["img"], pelicula["genero"], pelicula["dura"], pelicula["trailer"], pelicula["descri"]]
        for col, dato in enumerate(scrollable_data):
            cell = ctk.CTkLabel(scrollable_frame, text=str(dato), font=('Arial', 12))
            cell.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")
    
    # Crear marco para el formulario a la derecha
    form_frame = ctk.CTkFrame(main_frame)
    form_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
    form_frame.grid_rowconfigure(0, weight=1)
    form_frame.grid_columnconfigure(0, weight=1)

    # Etiquetas y campos de entrada en el formulario basados en los campos proporcionados
    campos_formulario = ["nombre", "duracion", "trailer", "descripcion", "img"]
    entries = {}  # Diccionario para almacenar las referencias de los campos de entrada
    
    for idx, campo in enumerate(campos_formulario):
        ctk.CTkLabel(form_frame, text=f"{campo.capitalize()}:").grid(row=idx, column=0, padx=10, pady=5, sticky="nsew")
        entry = ctk.CTkEntry(form_frame)
        entry.grid(row=idx, column=1, padx=10, pady=5, sticky="nsew")
        entries[campo] = entry  # Almacena la referencia del campo de entrada

    # Componente personalizado para seleccionar género
    genero_var, genero_menu, entries = GeneroEntry(parent=form_frame, campos=campos_formulario, entries=entries)

    # Componente personalizado para abrir imagen
    label_imagen = ImgAbrir(frame=form_frame, img_entry=entries["img"], row=len(campos_formulario)+1, column=1)
    
    # Botón para agregar datos al formulario
    agregar_button = Button(form_frame, texto="Agregar", tamanio=20, eventoClick=lambda: insertPelicula(entries=entries, label_imagen=label_imagen, main_frame=main_frame, ventana=ventana, infoUser=infoUser))
    agregar_button.grid(row=len(campos_formulario)+2, columnspan=2, pady=10, sticky="nsew")
    
    # Botón para limpiar todo el formulario
    def limpiar_todo():
        TablaPelicula(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    
    limpiar_todo_button = Button(form_frame, texto="Limpiar todo", tamanio=20, eventoClick=limpiar_todo)
    limpiar_todo_button.grid(row=len(campos_formulario)+3, columnspan=2, pady=10, sticky="nsew")

    # Agregar botones de paginación al final
    paginacion_frame = ctk.CTkFrame(main_frame)
    paginacion_frame.grid(row=1, column=0, columnspan=3, pady=20, sticky="nsew")
    paginacion_frame.grid_columnconfigure(0, weight=1)

    # Funciones para controlar la paginación
    def pagina_anterior():
        global current_page
        if current_page > 1:
            current_page -= 1
            TablaPelicula(main_frame, infoUser, ventana, current_page)

    def pagina_siguiente():
        global current_page
        current_page += 1
        peliculas_nuevas = GetAllPeli(page=current_page, limit=8)
        if peliculas_nuevas:
            TablaPelicula(main_frame, infoUser, ventana, current_page)
        else:
            current_page -= 1  # Si no hay más datos, no incrementamos la página
    
    # Botones de paginación
    anterior_button = Button(paginacion_frame, texto="Anterior", tamanio=15, eventoClick=pagina_anterior)
    anterior_button.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

    siguiente_button = Button(paginacion_frame, texto="Siguiente", tamanio=15, eventoClick=pagina_siguiente)
    siguiente_button.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
