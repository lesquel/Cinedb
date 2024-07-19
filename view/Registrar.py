import customtkinter as ctk

def Registrar(ventana):
    """
    Crea una ventana de registro para nuevos usuarios.

    Args:
    - ventana: La ventana principal a partir de la cual se abrirá la ventana de registro.

    Returns:
    - None
    """
    # Crear una nueva ventana para el registro
    main_frame = ctk.CTkToplevel(ventana)
    main_frame.title("Registro")
    main_frame.geometry("700x700")
    main_frame.resizable(False, False)
    main_frame.transient(ventana)  # Hace que la ventana de registro sea dependiente de la ventana principal

    # Título del formulario de registro
    ctk.CTkLabel(main_frame, text="Formulario de Registro", font=("Arial", 24, "bold")).grid(row=1, column=0, columnspan=3, pady=10, padx=10)

    # Función para crear un marco con etiqueta y entrada
    def crear_marco_etiqueta_entrada(texto_etiqueta):
        """
        Crea un marco con una etiqueta y una entrada de texto.

        Args:
        - texto_etiqueta: El texto que se mostrará en la etiqueta.

        Returns:
        - entrada: El widget de entrada creado.
        """
        marco = ctk.CTkFrame(main_frame)
        marco.grid(sticky="ew", padx=10, pady=5)
        etiqueta = ctk.CTkLabel(marco, text=texto_etiqueta, font=("Arial", 16))
        etiqueta.grid(row=0, column=0, padx=10, sticky="e")
        entrada = ctk.CTkEntry(marco, font=("Arial", 16), width=200)
        entrada.grid(row=0, column=1, padx=10, sticky="w")
        return entrada

    # Campos del formulario
    nombre_entry = crear_marco_etiqueta_entrada("Nombre:")
    img_entry = crear_marco_etiqueta_entrada("Imagen (Ruta):")
    edad_entry = crear_marco_etiqueta_entrada("Edad:")
    usuario_entry = crear_marco_etiqueta_entrada("Nombre de Usuario:")
    correo_entry = crear_marco_etiqueta_entrada("Correo:")
    contrasena_entry = crear_marco_etiqueta_entrada("Contraseña:")

    # Importar la función para seleccionar una imagen
    from components.AbrirImg import ImgAbrir
    ImgAbrir(frame=main_frame, img_entry=img_entry, row=3, column=2)  # Botón para seleccionar una imagen

    # Función para manejar el clic del botón "Registrar"
    from hooks.Peticiones.Registrar.registrar import registrar
    registrar_button = ctk.CTkButton(main_frame, text="Registrar", font=("Arial", 16),
                                     command=lambda: registrar(main_frame,
                                                               [nombre_entry, img_entry, edad_entry,
                                                                usuario_entry, correo_entry, contrasena_entry]))
    registrar_button.grid(row=8, column=0, columnspan=2, pady=20)

    # Función para cerrar la ventana de registro
    def cerrar():
        main_frame.destroy()

    # Botón para cerrar la ventana de registro
    cerrar_button = ctk.CTkButton(main_frame, text="Cerrar", font=("Arial", 16), command=cerrar)
    cerrar_button.grid(row=9, column=0, columnspan=2, pady=10)

    main_frame.protocol("WM_DELETE_WINDOW", cerrar)  # Manejar el evento de cierre de la ventana

