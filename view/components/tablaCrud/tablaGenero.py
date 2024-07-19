import customtkinter as ctk
from components.Button import Button
from hooks.destuirTodo import destuirTodo
from hooks.Peticiones.getGenero import getAllGeneros
from hooks.Peticiones.apdate.apdateGenero import apdateGenero
from hooks.Peticiones.delete.deleteGenero import deleteGenero
from hooks.Peticiones.insert.insertGenero import insertGenero
from components.VentaDeHelp import VentaDeHelp

def TablaGenero(main_frame, infoUser, ventana):
    # Limpiar contenido existente en el marco principal
    destuirTodo(ventana=main_frame)
    
    # Crear marco para las columnas fijas (id, nombre)
    fixed_columns_frame = ctk.CTkFrame(main_frame)
    fixed_columns_frame.grid(row=0, column=0, padx=20, pady=40, sticky="nsew")

    # Crear encabezados fijos para id y nombre
    fixed_headers = ["id", "nombre", "Editar", "Eliminar"]
    for col, header in enumerate(fixed_headers):
        label = ctk.CTkLabel(fixed_columns_frame, text=header.capitalize(), font=('Arial', 12, 'bold'))
        label.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")
    
    # Obtener información de los géneros
    generos = getAllGeneros()
    
    if not generos:
        print("No hay más datos para mostrar")
        return

    # Función para actualizar la ventana de edición de género
    def actualizar_Ventana(genero):
        ventanaActualizar = VentaDeHelp(ventana, infoUser)
        entry_nombre_actualizar = ctk.CTkEntry(ventanaActualizar, width=150)
        entry_nombre_actualizar.insert(0, genero["nombre"])
        entry_nombre_actualizar.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        actualizar_nombre_botones = ctk.CTkButton(ventanaActualizar, text="Actualizar", command=lambda: apdateGenero(id=genero["id"], nombre=entry_nombre_actualizar.get(), ventana=ventana, infoUser=infoUser, ventanaHelp=ventanaActualizar))
        actualizar_nombre_botones.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    # Insertar datos en la tabla fija (id, nombre y botones de acción)
    for row, genero in enumerate(generos, start=1):
        fixed_data = [genero["id"], genero["nombre"]]
        for col, dato in enumerate(fixed_data):
            cell = ctk.CTkLabel(fixed_columns_frame, text=str(dato), font=('Arial', 12))
            cell.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")
        
        # Botón Editar
        edit_button = ctk.CTkButton(fixed_columns_frame, text="Editar", command=lambda g=genero: actualizar_Ventana(g))
        edit_button.grid(row=row, column=len(fixed_data), padx=10, pady=5)
        
        # Botón Eliminar
        delete_button = ctk.CTkButton(fixed_columns_frame, text="Eliminar", command=lambda g=genero: deleteGenero(id=g["id"], main_frame=main_frame, infoUser=infoUser, ventana=ventana))
        delete_button.grid(row=row, column=len(fixed_data) + 1, padx=10, pady=5)
    
    # Crear marco para el formulario a la derecha
    form_frame = ctk.CTkFrame(main_frame)
    form_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
    form_frame.grid_rowconfigure(0, weight=1)
    form_frame.grid_columnconfigure(0, weight=0)  # Columna de la etiqueta
    form_frame.grid_columnconfigure(1, weight=0)  # Columna del entry

    # Etiquetas y campos de entrada en el formulario para agregar un nuevo género
    ctk.CTkLabel(form_frame, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="w")  # Alineado a la izquierda
    entry_nombre = ctk.CTkEntry(form_frame, width=150)  # Ancho fijo de 150
    entry_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="w")  # Alineado a la izquierda

    # Botón para agregar un nuevo género
    agregar_button = Button(form_frame, texto="Agregar", tamanio=20, eventoClick=lambda: insertGenero(nombre=entry_nombre.get(), ventana=ventana, infoUser=infoUser))
    agregar_button.grid(row=1, columnspan=2, pady=10, sticky="nsew")
    
    # Botón para limpiar el campo de entrada
    def limpiar_campos():
        entry_nombre.delete(0, ctk.END)
    
    limpiar_button = Button(form_frame, texto="Limpiar", tamanio=20, eventoClick=limpiar_campos)
    limpiar_button.grid(row=2, columnspan=2, pady=10, sticky="nsew")
