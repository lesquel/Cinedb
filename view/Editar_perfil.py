import customtkinter as ctk
import threading
from layout import Layout
from components.Img import Img
from components.Nav import Nav
from components.Regresar import RegresarFunc
from components.AbrirImg import ImgAbrir
from hooks.Peticiones.apdate.user import update_user
from Perfil import Perfil

def Editar_perfil(ventana, infoUser):
    """
    Función para crear la interfaz de edición de perfil del usuario.

    Args:
    - ventana: La ventana principal de la aplicación.
    - infoUser: Información del usuario actual.

    Returns:
    - frame: El marco principal que contiene la interfaz de edición de perfil.
    """
    frame = Layout(ventana=ventana)

    # Añadir el menú lateral para regresar al perfil
    RegresarFunc(frame_actual=frame, funcion_retorno=lambda: Perfil(ventana=ventana, infoUser=infoUser))

    # Obtener datos del usuario para editar
    id_usuario = infoUser["id"]
    nombre_usuario = infoUser["nombre"]
    contrasena_usuario = infoUser["contra"]
    imagen_usuario = infoUser["img"]
    nombre_real_usuario = infoUser["name"]
    correo_usuario = infoUser["correo"]
    edad_usuario = infoUser["edad"]

    def crear_input(frame, dato, nombre_label, fila, columna):
        """
        Función para crear un campo de entrada con su respectiva etiqueta en un marco.

        Args:
        - frame: Marco donde se añadirá el campo de entrada.
        - dato: Valor inicial del campo de entrada.
        - nombre_label: Texto de la etiqueta asociada al campo de entrada.
        - fila: Fila donde se posicionará en el marco.
        - columna: Columna donde se posicionará en el marco.

        Returns:
        - frame_input: El marco que contiene la etiqueta y el campo de entrada.
        - label: La etiqueta creada.
        - input_field: El campo de entrada creado.
        """
        frame_input = ctk.CTkFrame(frame)
        frame_input.grid(row=fila, column=columna, padx=20, pady=20, sticky="nsew")

        label = ctk.CTkLabel(frame_input, text=nombre_label, width=200, height=35)
        label.grid(row=0, column=0, padx=10, pady=10)

        input_field = ctk.CTkEntry(frame_input, width=200, height=35)
        input_field.insert(0, dato)
        input_field.grid(row=0, column=1, padx=10, pady=10)

        return frame_input, label, input_field

    # Crear campos de entrada para cada dato del usuario
    frame_nombre, label_nombre, input_nombre = crear_input(frame, dato=nombre_usuario, nombre_label="Nombre", fila=1, columna=0)
    frame_contrasena, label_contrasena, input_contrasena = crear_input(frame, dato=contrasena_usuario, nombre_label="Contraseña", fila=2, columna=0)
    frame_imagen, label_imagen, input_imagen = crear_input(frame, dato=imagen_usuario, nombre_label="Imagen", fila=3, columna=0)
    ImgAbrir(frame_imagen, input_imagen, row=0, column=0)  # Componente para seleccionar imagen

    frame_nombre_real, label_nombre_real, input_nombre_real = crear_input(frame, dato=nombre_real_usuario, nombre_label="Nombre real", fila=4, columna=0)
    frame_correo, label_correo, input_correo = crear_input(frame, dato=correo_usuario, nombre_label="Correo", fila=5, columna=0)
    frame_edad, label_edad, input_edad = crear_input(frame, dato=edad_usuario, nombre_label="Edad", fila=6, columna=0)

    def actualizar_usuario():
        update_user(
            id=id_usuario,
            nombre=input_nombre.get(),
            contra=input_contrasena.get(),
            img=input_imagen.get(),
            name=input_nombre_real.get(),
            correo=input_correo.get(),
            edad=input_edad.get(),
            ventana=ventana
        )

    # Botón para guardar cambios
    guardar_btn = ctk.CTkButton(frame, text="Guardar", width=120, height=40, command=lambda: threading.Thread(target=actualizar_usuario).start())
    guardar_btn.grid(row=7, column=1, padx=10, pady=10, sticky="e")

    return frame

