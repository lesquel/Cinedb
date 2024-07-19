from tkinter import filedialog
from PIL import Image, ImageTk
import customtkinter as ctk
import requests
from io import BytesIO

def ImgAbrir(frame, img_entry, row, column):
    """
    Función para crear una interfaz que permita seleccionar y mostrar imágenes en un marco de Tkinter.

    Parameters:
    - frame (ctk.CTkFrame): Marco donde se colocará la interfaz.
    - img_entry (ctk.CTkEntry): Campo de entrada donde se puede escribir la ruta de la imagen o URL.
    - row (int): Fila en la que se colocará la interfaz dentro del marco.
    - column (int): Columna en la que se colocará la interfaz dentro del marco.

    Returns:
    - ctk.CTkLabel: Etiqueta donde se muestra la imagen seleccionada.
    """

    # Función interna para crear una etiqueta inicial vacía para mostrar la imagen
    def crear_label():
        label = ctk.CTkLabel(main_frame, image=None, text="")
        label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        return label

    # Función para seleccionar una imagen usando un cuadro de diálogo de archivo
    def seleccionar_imagen():
        ruta_imagen = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg;*.jpeg;*.png")])
        if ruta_imagen:
            cargar_imagen(ruta_imagen)

    # Función para seleccionar una imagen usando la ruta escrita en el campo de entrada
    def seleccionar_imagen_por_entry(event):
        ruta_imagen = img_entry.get()
        if ruta_imagen:
            cargar_imagen(ruta_imagen)

    # Función para cargar y mostrar la imagen desde una ruta o URL
    def cargar_imagen(ruta):
        global photo  # Variable global para mantener la referencia de la imagen y evitar que sea eliminada por el recolector de basura
        try:
            # Verificar si la ruta es una URL
            if ruta.startswith("http://") or ruta.startswith("https://"):
                response = requests.get(ruta)
                response.raise_for_status()  # Asegurar que la descarga fue exitosa
                imagen = Image.open(BytesIO(response.content))
            else:
                imagen = Image.open(ruta)  # Cargar la imagen desde una ruta local

            # Redimensionar la imagen a 300x300 píxeles
            imagen = imagen.resize((300, 300))

            # Convertir la imagen a un objeto `PhotoImage` compatible con Tkinter
            photo = ImageTk.PhotoImage(imagen)

            # Mostrar la imagen en la etiqueta `label_imagen`
            label_imagen.configure(image=photo)
            label_imagen.image = photo  # Guardar referencia para evitar que se elimine por el recolector de basura

            # Actualizar el campo de entrada `img_entry` con la ruta de la imagen cargada
            img_entry.delete(0, ctk.END)
            img_entry.insert(0, ruta)

        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

    # Configuración del marco principal donde se colocará la interfaz
    main_frame = ctk.CTkFrame(frame, fg_color="transparent")
    main_frame.grid(row=row, column=column, sticky="nsew")

    # Botón para seleccionar una imagen desde el sistema de archivos
    btn_seleccionar = ctk.CTkButton(main_frame, text="Seleccionar Imagen", command=seleccionar_imagen)
    btn_seleccionar.grid(row=1, column=0, pady=20, padx=10)

    # Asignar evento de teclado para cargar la imagen desde el campo de entrada `img_entry`
    img_entry.bind("<Return>", seleccionar_imagen_por_entry)

    # Crear y retornar la etiqueta `label_imagen` inicial vacía
    label_imagen = crear_label()
    return label_imagen
