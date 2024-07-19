


def TablaFunciones(main_frame, infoUser, ventana):
    """
    Crea una tabla de funciones en un marco principal con opciones para ver, editar y eliminar funciones.

    Args:
    - main_frame (ctk.CTkFrame): Marco principal donde se colocará la tabla y el formulario.
    - infoUser (dict): Información del usuario actual.
    - ventana (tk.Tk): Ventana principal de la aplicación.

    Returns:
    - None
    """
    import customtkinter as ctk
    from components.Button import Button
    from components.GeneroEntry import obtener_id_genero
    from hooks.Peticiones.apdate.apdateFuncion import apdateFuncion
    from hooks.Peticiones.delete.deleteFuncion import deleteFuncion

    from hooks.Peticiones.insert.insertFuncion import insertFuncion
    # Limpiar contenido existente en el marco principal
    from hooks.destuirTodo import destuirTodo
    destuirTodo(ventana=main_frame)
    
    # Crear marco para las columnas fijas (id, fecha, idSala, idPeliculas, sillas)
    fixed_columns_frame = ctk.CTkFrame(main_frame)
    fixed_columns_frame.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")

    # Crear encabezados fijos para id, fecha, idSala, idPeliculas, sillas, Editar, Eliminar
    fixed_headers = ["id", "fecha", "idSala", "idPeliculas", "sillas", "Editar", "Eliminar"]
    for col, header in enumerate(fixed_headers):
        label = ctk.CTkLabel(fixed_columns_frame, text=header.capitalize(), font=('Arial', 12, 'bold'))
        label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")
    
    # Obtener información de las funciones (reemplazar con lógica real de obtención de datos)
    from hooks.Peticiones.GetFunciones import getAllFunciones
    funciones = getAllFunciones()
    
    if not funciones:
        print("No hay más datos para mostrar")
        return
    
    # Función para actualizar una función existente
    def actualizar_Ventana(funcion):
        """
        Abre una ventana para actualizar la información de una función.

        Args:
        - funcion (dict): Información de la función a actualizar.

        Returns:
        - None
        """
        from components.VentaDeHelp import VentaDeHelp
        ventanaActualizar = VentaDeHelp(ventana, infoUser)
        
        # Obtener datos para los selectores
        from hooks.Peticiones.GetSalas import GetAllSalas
        from hooks.Peticiones.GetPeli import GetPeliTodasAll
        salas = GetAllSalas()
        peliculas = GetPeliTodasAll()
        
        # Crear listas de nombres para los selectores de salas y películas
        sala_nombres = [f"{sala['nombre']} ({sala['id']})" for sala in salas]
        pelicula_nombres = [f"{pelicula['nombre']} ({pelicula['id']})" for pelicula in peliculas]

        # Etiquetas y campos de entrada en la ventana de actualización
        ctk.CTkLabel(ventanaActualizar, text="Fecha").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_fecha_actualizar = ctk.CTkEntry(ventanaActualizar, width=150)
        entry_fecha_actualizar.insert(0, funcion["fecha"])
        entry_fecha_actualizar.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        ctk.CTkLabel(ventanaActualizar, text="idSala").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_idSala_actualizar = ctk.CTkComboBox(ventanaActualizar, values=sala_nombres, width=150)
        entry_idSala_actualizar.set(f"{funcion['idSala']} ({funcion['idSala']})")  # Establecer valor inicial
        entry_idSala_actualizar.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ctk.CTkLabel(ventanaActualizar, text="idPeliculas").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        entry_idPeliculas_actualizar = ctk.CTkComboBox(ventanaActualizar, values=pelicula_nombres, width=150)
        entry_idPeliculas_actualizar.set(f"{funcion['idPeliculas']} ({funcion['idPeliculas']})")  # Establecer valor inicial
        entry_idPeliculas_actualizar.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Botón para actualizar la función
        ctk.CTkButton(ventanaActualizar, text="Actualizar", command=lambda: apdateFuncion(
            id=funcion["id"],
            fecha=entry_fecha_actualizar.get(),
            idSala=obtener_id_genero(entry_idSala_actualizar.get()),
            idPeliculas=obtener_id_genero(entry_idPeliculas_actualizar.get()),
            ventana=ventana,
            infoUser=infoUser,
            ventanaHelp=ventanaActualizar,
            main_frame=main_frame
        )).grid(row=4, column=0, padx=10, pady=5, sticky="w")

    # Función para ver las sillas disponibles para una función
    def ver_sillas(funcion):
        """
        Abre una ventana para visualizar las sillas disponibles para una función.

        Args:
        - funcion (dict): Información de la función.

        Returns:
        - None
        """
        from Sillas import Sillas
        from hooks.Peticiones.GetSalas import GetSalas
        sala = GetSalas(idSala=funcion["idSala"])
        from hooks.Peticiones.GetPeli import GetPeliId
        info = GetPeliId(idPelicula=funcion["idPeliculas"])
        Sillas(ventana=ventana, funcion_data=funcion, pelicula_info=info, id_usuario=infoUser["id"], funcion=funcion, sala=sala)
    
    # Insertar datos en la tabla fija (id, fecha, idSala, idPeliculas, sillas y botones de acción)
    for row, funcion in enumerate(funciones, start=1):
        fixed_data = [funcion["id"], funcion["fecha"], funcion["idSala"], funcion["idPeliculas"]]
        for col, dato in enumerate(fixed_data):
            cell = ctk.CTkLabel(fixed_columns_frame, text=str(dato), font=('Arial', 12))
            cell.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")
        
        # Botón para ver sillas
        ctk.CTkButton(fixed_columns_frame, text="Ver", command=lambda funcion=funcion: ver_sillas(funcion)).grid(row=row, column=len(fixed_data), padx=10, pady=5)
        
        # Botón Editar
        ctk.CTkButton(fixed_columns_frame, text="Editar", command=lambda funcion=funcion: actualizar_Ventana(funcion)).grid(row=row, column=len(fixed_data) + 1, padx=10, pady=5)
        
        # Botón Eliminar
        ctk.CTkButton(fixed_columns_frame, text="Eliminar", command=lambda funcion=funcion: deleteFuncion(id=funcion["id"], main_frame=main_frame, infoUser=infoUser, ventana=ventana)).grid(row=row, column=len(fixed_data) + 2, padx=10, pady=5)
    
    # Crear marco para el formulario a la derecha
    form_frame = ctk.CTkFrame(main_frame)
    form_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
    form_frame.grid_rowconfigure(0, weight=1)
    form_frame.grid_columnconfigure(0, weight=0)  # Columna de la etiqueta
    form_frame.grid_columnconfigure(1, weight=0)  # Columna del entry

    # Etiquetas y campos de entrada en el formulario para agregar una nueva función
    ctk.CTkLabel(form_frame, text="Fecha:").grid(row=0, column=0, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    entry_fecha = ctk.CTkEntry(form_frame, width=150)  # Ancho fijo de 150
    entry_fecha.grid(row=0, column=1, padx=10, pady=5, sticky="w")  # Alineado a la izquierda

    # Datos para los selectores
    from hooks.Peticiones.GetSalas import GetAllSalas
    from hooks.Peticiones.GetPeli import GetPeliTodasAll
    salas = GetAllSalas()
    peliculas = GetPeliTodasAll()
    # Listas de nombres para los selectores
    sala_nombres = [f"{sala['nombre']} ({sala['id']})" for sala in salas]
    pelicula_nombres = [f"{pelicula['nombre']} ({pelicula['id']})" for pelicula in peliculas]

    ctk.CTkLabel(form_frame, text="idSala:").grid(row=1, column=0, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    entry_idSala = ctk.CTkComboBox(form_frame, values=sala_nombres, width=150)  # Ancho fijo de 150
    entry_idSala.grid(row=1, column=1, padx=10, pady=5, sticky="w")  # Alineado a la izquierda

    ctk.CTkLabel(form_frame, text="idPeliculas:").grid(row=2, column=0, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    entry_idPeliculas = ctk.CTkComboBox(form_frame, values=pelicula_nombres, width=150)  # Ancho fijo de 150
    entry_idPeliculas.grid(row=2, column=1, padx=10, pady=5, sticky="w")  # Alineado a la izquierda

    # Botón para agregar una nueva función
    Button(form_frame, texto="Agregar", tamanio=20, eventoClick=lambda: insertFuncion(
        fecha=entry_fecha.get(),
        idSala=obtener_id_genero(entry_idSala.get()),  # Extrae solo el ID
        idPeliculas=obtener_id_genero(entry_idPeliculas.get()),  # Extrae solo el ID
        ventana=ventana,
        infoUser=infoUser,
        main_frame=main_frame
    )).grid(row=4, columnspan=2, pady=10, padx=10)
