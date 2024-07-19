import customtkinter as ctk
from layout import Layout
from components.AllSIllas import AllSIllas
from hooks.Reserva import Reservar
from hooks.Recomendado import Recomendado
from components.Regresar import RegresarFunc

def Sillas(ventana, funcion_data, pelicula_info, id_usuario, funcion, sala):
    """
    Crea una interfaz para mostrar las sillas de una sala de cine con opciones de reserva y recomendación de asientos.

    Args:
    - ventana: Objeto ventana donde se colocará la interfaz.
    - funcion_data: Datos de la función de cine, incluyendo información de sillas.
    - pelicula_info: Información de la película relacionada con la función.
    - id_usuario: ID del usuario actual.
    - funcion: Información de la función de cine.
    - sala: Información de la sala de cine.

    Returns:
    - frame_principal: Marco principal que contiene toda la interfaz de sillas y opciones.
    """

    from Salas import Salas
    # Crear el contenedor principal
    frame_principal = Layout(ventana=ventana)

    # Crear frame1 y frame2 para organizar los componentes
    frame1 = ctk.CTkFrame(frame_principal, width=600)
    frame2 = ctk.CTkFrame(frame_principal)

    # Configuración de disposición y expansión de frames
    frame2.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)
    frame2.grid_columnconfigure(0, weight=1)
    frame2.grid_rowconfigure(0, weight=1)

    frame1.grid(row=0, column=1, sticky="nsew", padx=40, pady=40)

    # Cargar la matriz de sillas desde los datos de la función
    matriz_sillas = funcion_data["sillas"]

    # Función para ejecutar el algoritmo de recomendación de asientos
    def ejecutar_recomendacion(id_usuario=id_usuario):
        nonlocal matriz_sillas
        matriz_sillas = Recomendado(matriz=matriz_sillas)
        AllSIllas(matriz=matriz_sillas, frame=frame2, idUsuario=id_usuario)

    # Etiqueta para la pantalla en frame2
    pantalla_label = ctk.CTkLabel(frame2, text="Pantalla", font=("Arial", 14), bg_color="#222222", text_color="#ffffff")
    pantalla_label.grid(row=len(matriz_sillas) + 1, column=0, columnspan=6, padx=10, pady=10, sticky="ew")

    # Leyenda de tipos de sillas y sus colores
    leyenda_sillas = [
        ["L", "Libre", "#8888ff"],          # Libre
        ["O", "Ocupado", "#ff8888"],        # Ocupado
        ["S", "Sección|Reservado", "#888888"],  # Sección o reservado
        ["R", "Recomendado", "#88ff88"],    # Recomendado
        ["M", "Mis Sillas", "#ffff00"]      # Mis sillas
    ]

    # Configuración de la leyenda de sillas en frame1 usando grid
    for i, (codigo, descripcion, color) in enumerate(leyenda_sillas):
        label = ctk.CTkLabel(frame1, text=f"{codigo}={descripcion}", font=("Arial", 14), bg_color=color)
        label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

    # Mostrar todas las sillas en frame2 al cargar la interfaz
    AllSIllas(matriz=matriz_sillas, frame=frame2, idUsuario=id_usuario)

    # Botón para ejecutar la recomendación de mejor asiento en frame1
    mejor_asiento_boton = ctk.CTkButton(frame1, text="Recomendar Mejor Asiento", command=lambda: ejecutar_recomendacion(id_usuario=id_usuario))
    mejor_asiento_boton.grid(row=len(leyenda_sillas) + 1, column=0, sticky="ew", padx=10, pady=5)

    # Frame para el botón de reserva de sillas
    frame_reserva = ctk.CTkFrame(frame1, width=600, height=600)
    frame_reserva.grid(row=len(leyenda_sillas) + 2, column=0, sticky="nsew", padx=40, pady=40)

    # Botón para cargar información y proceder con la reserva de sillas
    reservar_boton = ctk.CTkButton(frame_reserva, text="Cargar Información para Reserva", command=lambda: Reservar(frame=frame_reserva, info=pelicula_info, id=funcion["id"], sillas=matriz_sillas, idUsuario=id_usuario, funcion=funcion, sala=sala))
    reservar_boton.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

    # Botón para regresar a la página de detalles de la película
    RegresarFunc(frame_actual=frame_principal, funcion_retorno=lambda: Salas(ventana=ventana, infoPelicula=pelicula_info, idUsuario=id_usuario))

    # Configurar el frame_principal para permitir la expansión
    frame_principal.grid_rowconfigure(0, weight=1)
    frame_principal.grid_columnconfigure(0, weight=1)
    frame_principal.grid_columnconfigure(1, weight=1)

    return frame_principal
