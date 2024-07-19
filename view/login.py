from layout import Layout
import customtkinter as ctk
from components.Text import Text
from tkinter import messagebox
from hooks.login.autentificacion import autentificacion
from components.ImgLocal import Img
from datos.UrlImgs import UrlImgsLogin
from Registrar import Registrar

def login(ventana):
    """
    Función para crear la pantalla de inicio de sesión.

    Args:
    - ventana: La ventana principal de la aplicación.

    Returns:
    - main_frame: El marco principal que contiene toda la interfaz de inicio de sesión.
    """
    # Crear y configurar el marco principal usando Layout
    main_frame = Layout(ventana=ventana)

    # Crear el marco para la imagen
    img_frame = ctk.CTkFrame(main_frame)
    img_frame.grid(row=0, column=0, padx=150, pady=150, sticky="nsew")

    # Mostrar imagen de logo de Intercine
    img = Img(url_or_path=UrlImgsLogin["intercine"], size=300)
    labelimg = ctk.CTkLabel(img_frame, image=img, text="", compound=ctk.TOP)
    labelimg.grid(row=0, column=0, padx=10, pady=10)
    Text(img_frame, texto="Intercine", row=1, column=0, tamanio=30)

    # Crear el marco para el formulario
    form_frame = ctk.CTkFrame(main_frame)
    form_frame.grid(row=0, column=1, padx=100, pady=150, sticky="nsew")

    # Título del formulario
    Text(form_frame, texto="Ingresa a Intercine", row=0, column=0, tamanio=20)

    # Campos de entrada de usuario y contraseña
    Text(form_frame, texto="Usuario", row=1, column=0, tamanio=16)
    usuario_entry = ctk.CTkEntry(form_frame, font=("Arial", 16), width=200, height=35)
    usuario_entry.grid(row=1, column=1, padx=10, pady=10)

    Text(form_frame, texto="Contraseña", row=2, column=0, tamanio=16)
    contrasena_entry = ctk.CTkEntry(form_frame, show="*", font=("Arial", 16), width=200, height=35)
    contrasena_entry.grid(row=2, column=1, padx=10, pady=10)

    # Función para manejar el evento de "Entrar"
    def Entrar():
        """
        Función para manejar el evento de inicio de sesión.
        """
        usuario = usuario_entry.get()
        contrasena = contrasena_entry.get()
        autentificacion(ventana, usuario, contrasena)

    # Botones en el formulario
    entrar_btn = ctk.CTkButton(form_frame, text="Entrar", width=120, height=40, fg_color="blue", command=Entrar)
    entrar_btn.grid(row=3, column=1, padx=10, pady=20, sticky="e")

    registrar_btn = ctk.CTkButton(form_frame, text="Registrar", width=120, height=40, fg_color="blue", command=lambda: Registrar(ventana))
    registrar_btn.grid(row=3, column=0, padx=10, pady=20, sticky="e")

    cerrar_btn = ctk.CTkButton(form_frame, text="Cerrar", width=120, height=40, fg_color="red", command=ventana.destroy)
    cerrar_btn.grid(row=4, column=1, padx=10, pady=10, sticky="e")

    return main_frame
