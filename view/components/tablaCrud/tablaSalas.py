import customtkinter as ctk
from components.Button import Button
from hooks.Peticiones.apdate.apdateSala import apdateSala
from hooks.Peticiones.delete.deleteSala import deleteSala

def TablaSala(main_frame, infoUser, ventana):
    """
    Función para mostrar una tabla de salas con opciones de editar, eliminar, agregar y visualizar las sillas de una sala.

    Parameters:
    - main_frame (ctk.CTkFrame): Marco principal donde se mostrará la tabla.
    - infoUser (dict): Información del usuario actual.
    - ventana (Tk.Tk): Ventana principal de la aplicación.

    Returns:
    - None
    """
    # Importar función para limpiar el contenido anterior del marco principal
    from hooks.destuirTodo import destuirTodo
    destuirTodo(ventana=main_frame)
    
    # Crear marco para las columnas fijas (id, nombre, fillas, columnas)
    fixed_columns_frame = ctk.CTkFrame(main_frame)
    fixed_columns_frame.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")

    # Crear marco para la vista previa de sillas
    frame_de_SillasPreview = ctk.CTkFrame(main_frame)
    frame_de_SillasPreview.grid(row=1, column=0, padx=20, pady=40, sticky="nsew")
    frame_de_SillasPreview.grid_columnconfigure(0, weight=1)
    frame_de_SillasPreview.grid_columnconfigure(1, weight=1)    

    # Crear encabezados fijos para id, nombre, fillas, columnas, editar y eliminar
    fixed_headers = ["id", "nombre", "fillas", "columnas", "Editar", "Eliminar"]
    for col, header in enumerate(fixed_headers):
        label = ctk.CTkLabel(fixed_columns_frame, text=header.capitalize(), font=('Arial', 12, 'bold'))
        label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")
    
    # Obtener las salas para mostrar en la tabla
    from hooks.Peticiones.GetSalas import GetAllSalas
    salas = GetAllSalas()
    
    # Manejar caso cuando no hay salas para mostrar
    if not salas:
        print("No hay más datos para mostrar")
        return
    
    # Función para actualizar la ventana de edición de una sala
    def actualizar_Ventana(sala):
        from components.VentaDeHelp import VentaDeHelp
        ventanaActualizar = VentaDeHelp(ventana, infoUser)
        
        # Crear campos de entrada prellenados con los datos de la sala seleccionada
        entry_nombre_actualizar = ctk.CTkEntry(ventanaActualizar, width=150)
        entry_nombre_actualizar.insert(0, sala["nombre"])
        entry_nombre_actualizar.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        entry_fillas_actualizar = ctk.CTkEntry(ventanaActualizar, width=150)
        entry_fillas_actualizar.insert(0, sala["fillas"])
        entry_fillas_actualizar.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        entry_columnas_actualizar = ctk.CTkEntry(ventanaActualizar, width=150)
        entry_columnas_actualizar.insert(0, sala["columnas"])
        entry_columnas_actualizar.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        # Botón para actualizar la sala
        actualizar_sala_botones = ctk.CTkButton(ventanaActualizar, text="Actualizar", command=lambda: apdateSala(id=sala["id"], nombre=entry_nombre_actualizar.get(), filas=entry_fillas_actualizar.get(), columnas=entry_columnas_actualizar.get(), ventana=ventana, infoUser=infoUser, ventanaHelp=ventanaActualizar, main_frame=main_frame))
        actualizar_sala_botones.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    
    # Insertar datos en la tabla fija (id, nombre, fillas, columnas y botones de acción)
    for row, sala in enumerate(salas, start=1):
        fixed_data = [sala["id"], sala["nombre"], sala["fillas"], sala["columnas"]]
        for col, dato in enumerate(fixed_data):
            cell = ctk.CTkLabel(fixed_columns_frame, text=str(dato), font=('Arial', 12))
            cell.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")
        
        # Botón Editar
        edit_button = ctk.CTkButton(fixed_columns_frame, text="Editar", command=lambda sala=sala: actualizar_Ventana(sala))
        edit_button.grid(row=row, column=len(fixed_data), padx=10, pady=5)
        
        # Botón Eliminar
        delete_button = ctk.CTkButton(fixed_columns_frame, text="Eliminar", command=lambda sala=sala: deleteSala(id=sala["id"], main_frame=main_frame, infoUser=infoUser, ventana=ventana))
        delete_button.grid(row=row, column=len(fixed_data) + 1, padx=10, pady=5)
    
    # Crear marco para el formulario a la derecha
    form_frame = ctk.CTkFrame(main_frame)
    form_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
    form_frame.grid_rowconfigure(0, weight=1)
    form_frame.grid_columnconfigure(0, weight=0)  # Columna de la etiqueta
    form_frame.grid_columnconfigure(1, weight=0)  # Columna del entry

    # Etiquetas y campos de entrada en el formulario para agregar una nueva sala
    ctk.CTkLabel(form_frame, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    entry_nombre = ctk.CTkEntry(form_frame, width=150)  # Ancho fijo de 150
    entry_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    
    ctk.CTkLabel(form_frame, text="Fillas:").grid(row=1, column=0, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    entry_fillas = ctk.CTkEntry(form_frame, width=150)  # Ancho fijo de 150
    entry_fillas.grid(row=1, column=1, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    
    ctk.CTkLabel(form_frame, text="Columnas:").grid(row=2, column=0, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    entry_columnas = ctk.CTkEntry(form_frame, width=150)  # Ancho fijo de 150
    entry_columnas.grid(row=2, column=1, padx=10, pady=5, sticky="w")  # Alineado a la izquierda

    # Botón para agregar una nueva sala
    from hooks.Peticiones.insert.insertSala import insertSala
    agregar_button = Button(form_frame, texto="Agregar", tamanio=20, eventoClick=lambda: insertSala(nombre=entry_nombre.get(), filas=int(entry_fillas.get()), columnas=entry_columnas.get(), ventana=ventana, infoUser=infoUser, main_frame=main_frame))
    agregar_button.grid(row=3, columnspan=2, pady=10, sticky="nsew")
    
    # Botón para limpiar los campos de entrada
    def limpiar_campos():
        entry_nombre.delete(0, ctk.END)
        entry_fillas.delete(0, ctk.END)
        entry_columnas.delete(0, ctk.END)
    
    limpiar_button = Button(form_frame, texto="Limpiar", tamanio=20, eventoClick=limpiar_campos)
    limpiar_button.grid(row=4, columnspan=2, pady=10, sticky="nsew")

    # Función para ver las sillas de una sala
    def Ver_Sillas(frame_de_SillasPreview, sala, ventana, infoUser):
        from components.AllSIllas import AllSIllas
        from hooks.Peticiones.insert.insertFuncion import cerateSillas
        
        # Crear y mostrar la matriz de sillas de la sala seleccionada
        sillas = cerateSillas(filas=int(entry_fillas.get()), columnas=int(entry_columnas.get()))
        AllSIllas(matriz=sillas, frame=frame_de_SillasPreview, idUsuario=infoUser["id"])

    # Botón para ver las sillas de una sala
    verSillas = ctk.CTkButton(form_frame, text="Ver", command=lambda: Ver_Sillas(frame_de_SillasPreview, sala=sala, ventana=ventana, infoUser=infoUser))
    verSillas.grid(row=5, columnspan=2, pady=10, sticky="nsew")
