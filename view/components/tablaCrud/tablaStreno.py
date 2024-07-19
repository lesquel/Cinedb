import customtkinter as ctk
from components.Button import Button
from hooks.Peticiones.GetPeli import GetPeliId, GetPeliTodasAll
from hooks.Peticiones.GetSliderAndEstreno import GetEstrenoAll
from hooks.Peticiones.delete.deleteSliderAndEstreno import deleteEstreno
from hooks.destuirTodo import destuirTodo
from hooks.Peticiones.insert.insertSliderAndEstreno import insertEstreno
from components.GeneroEntry import obtener_id_genero

def TablaEstreno(main_frame, infoUser, ventana):
    """
    Función para mostrar una tabla de estrenos con opción de eliminar y agregar nuevos estrenos.

    Parameters:
    - main_frame (ctk.CTkFrame): Marco principal donde se mostrará la tabla.
    - infoUser (dict): Información del usuario actual.
    - ventana (Tk.Tk): Ventana principal de la aplicación.

    Returns:
    - None
    """
    # Limpiar contenido anterior del marco principal
    destuirTodo(ventana=main_frame)
    
    # Crear marco para las columnas fijas (id, Película, Eliminar)
    fixed_columns_frame = ctk.CTkFrame(main_frame)
    fixed_columns_frame.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")

    # Función para imprimir los datos de los estrenos
    def PrintarDatos():
        estrenos = GetEstrenoAll()
        if not estrenos:
            print("No hay datos de estrenos para mostrar")
            return
        
        # Crear encabezados fijos para id, Película y Eliminar
        fixed_headers = ["id", "Pelicula", "Eliminar"]
        for col, header in enumerate(fixed_headers):
            label = ctk.CTkLabel(fixed_columns_frame, text=header.capitalize(), font=('Arial', 12, 'bold'))
            label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")
        
        # Mostrar datos de los estrenos en la tabla
        for row, estreno in enumerate(estrenos, start=1):
            pelicula = GetPeliId(estreno["id_pelicula"])
            fixed_data = [estreno["id"], pelicula["nombre"]]
            for col, dato in enumerate(fixed_data):
                cell = ctk.CTkLabel(fixed_columns_frame, text=str(dato), font=('Arial', 12))
                cell.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")
            
            # Botón Eliminar para cada estreno
            delete_button = ctk.CTkButton(fixed_columns_frame, text="Eliminar", command=lambda e=estreno: eliminar_estreno(e))
            delete_button.grid(row=row, column=len(fixed_data), padx=10, pady=5)
    
    # Función para eliminar un estreno
    def eliminar_estreno(estreno):
        deleteEstreno(id=estreno["id"], main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    
    # Crear marco para el formulario a la derecha
    form_frame = ctk.CTkFrame(main_frame)
    form_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
    form_frame.grid_rowconfigure(0, weight=1)
    form_frame.grid_columnconfigure(0, weight=0)  # Columna de la etiqueta
    form_frame.grid_columnconfigure(1, weight=0)  # Columna del entry

    # Etiqueta y campo de entrada en el formulario para agregar un nuevo estreno
    ctk.CTkLabel(form_frame, text="ID Película:").grid(row=0, column=0, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    
    # Obtener todas las películas disponibles para mostrar en el ComboBox
    peliculas = GetPeliTodasAll()
    entry_id_pelicula = ctk.CTkComboBox(form_frame, values=[f"{pelicula['nombre']} ({pelicula['id']})" for pelicula in peliculas], width=150)  # Ancho fijo de 150
    entry_id_pelicula.grid(row=0, column=1, padx=10, pady=5, sticky="w")  # Alineado a la izquierda

    # Función para agregar un nuevo estreno
    def agregar_estreno():
        insertEstreno(idPelicula=obtener_id_genero(entry_id_pelicula.get()), ventana=ventana, infoUser=infoUser, main_frame=main_frame)
    
    # Botón para agregar un nuevo estreno
    agregar_button = Button(form_frame, texto="Agregar", tamanio=20, eventoClick=lambda: agregar_estreno())
    agregar_button.grid(row=1, columnspan=2, pady=10, sticky="nsew")
    
    # Mostrar los datos actuales de los estrenos al iniciar la tabla
    PrintarDatos()
