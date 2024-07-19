import requests
from io import BytesIO
from PIL import Image
import customtkinter as ctk
from concurrent.futures import ThreadPoolExecutor

# Crear un único ThreadPoolExecutor para gestionar todos los hilos
executor = ThreadPoolExecutor()

def download_and_process_image(url, tamanio):
    """
    Descarga y procesa una imagen desde una URL.

    Args:
        url (str): URL de la imagen.
        tamanio (int): Tamaño al que se redimensionará la imagen.

    Returns:
        Image or None: Imagen procesada o None si ocurrió un error.
    """
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        img = Image.open(BytesIO(res.content))
        img = img.resize((tamanio, tamanio))
        return img
    except (requests.RequestException, IOError) as e:
        print(f"Error downloading or processing image: {e}")
        return None

def update_image(f, img, tamanio, row, column):
    """
    Actualiza una imagen en el GUI.

    Args:
        f (Frame): El marco donde se actualizará la imagen.
        img (Image): La imagen a actualizar.
        tamanio (int): Tamaño de la imagen.
        row (int): Fila en el grid donde se colocará la imagen.
        column (int): Columna en el grid donde se colocará la imagen.
    """
    if img is not None and f.winfo_exists():
        ctk_img = ctk.CTkImage(light_image=img, size=(tamanio, tamanio))
        label = ctk.CTkLabel(f, image=ctk_img, text="", compound=ctk.TOP)
        label.image = ctk_img
        label.grid(padx=10, pady=10, row=row, column=column)
    else:
        print(f"Failed to update image at row {row}, column {column}")

def handle_image(f, future, tamanio, row, column):
    """
    Maneja la actualización de la imagen de forma asíncrona.

    Args:
        f (Frame): El marco donde se actualizará la imagen.
        future (Future): Objeto Future que contiene la imagen descargada.
        tamanio (int): Tamaño de la imagen.
        row (int): Fila en el grid donde se colocará la imagen.
        column (int): Columna en el grid donde se colocará la imagen.
    """
    try:
        img = future.result()
        if f.winfo_exists():
            f.after(0, update_image, f, img, tamanio, row, column)
        else:
            print(f"Frame no longer exists for image at row {row}, column {column}")
    except Exception as e:
        print(f"Error handling image: {e}")

def Img(f, url, tamanio=250, row=0, column=0):
    """
    Descarga y muestra una imagen en un marco de tkinter de manera asíncrona.

    Args:
        f (Frame): El marco donde se mostrará la imagen.
        url (str): URL de la imagen.
        tamanio (int): Tamaño de la imagen.
        row (int): Fila en el grid donde se colocará la imagen.
        column (int): Columna en el grid donde se colocará la imagen.
    """
    future = executor.submit(download_and_process_image, url, tamanio)
    future.add_done_callback(lambda fut: handle_image(f, fut, tamanio, row, column))
