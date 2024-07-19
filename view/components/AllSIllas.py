# view/components/AllSIllas.py
from .Sillas import Sillas
import hooks.Cambiar_Guardar as Cambiar_Guardar
from datos.UrlImgs import UrlImgs
import customtkinter as ctk

def AllSIllas(matriz, frame, idUsuario):
    """
    Función para crear una interfaz que muestre una matriz de sillas con diferentes estados y funcionalidades.

    Parameters:
    - matriz (list of list): Matriz representando el estado de cada silla.
    - frame (ctk.CTkFrame): Marco principal donde se colocará la interfaz.
    - idUsuario (str/int): Identificador del usuario actual.
    """

    # Configurar el frame principal para permitir la expansión
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Crear un nuevo frame dentro del frame principal
    fra = ctk.CTkFrame(frame)
    fra.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")
    fra.grid_columnconfigure(0, weight=1)  # Permitir expansión en columna
    fra.grid_rowconfigure(0, weight=1)     # Permitir expansión en fila
    
    def ejecutar2(b, r, c):
        """
        Función para manejar el evento de clic en una silla y actualizar la matriz.

        Parameters:
        - b (Button): Botón que fue clickeado.
        - r (int): Fila de la silla en la matriz.
        - c (int): Columna de la silla en la matriz.
        """
        nonlocal matriz
        matriz = Cambiar_Guardar.Cambiar_Guardar(b=b, r=r, c=c, matriz=matriz)
        fra.destroy()
        AllSIllas(matriz=matriz, frame=frame, idUsuario=idUsuario)

    # Configurar el grid del contenedor 'fra' para que las celdas se expandan
    for i in range(len(matriz)):
        fra.grid_rowconfigure(i, weight=1)  # Permitir expansión de filas
    for j in range(len(matriz[0])):
        fra.grid_columnconfigure(j, weight=1)  # Permitir expansión de columnas

    # Crear los botones para la matriz de sillas
    for i, f in enumerate(matriz):
        for j, c in enumerate(f):
            if c == "L":
                b, r, c = Sillas(parent=fra, tamanio=16, row=i, column=j, bg_color="#8888ff", imagen_url=UrlImgs["azul"])
                b.configure(command=lambda b=b, r=i, c=j: ejecutar2(b, r, c))
            elif c == "S":
                Sillas(parent=fra, tamanio=16, row=i, column=j, bg_color="#888888", imagen_url=UrlImgs["rojo"])
            elif c == "R":
                b, r, c = Sillas(parent=fra, tamanio=16, row=i, column=j, bg_color="#88ff88", imagen_url=UrlImgs["verde"])
                b.configure(command=lambda b=b, r=i, c=j: ejecutar2(b, r, c))
            elif c == idUsuario:
                b, r, c = Sillas(parent=fra, tamanio=16, row=i, column=j, bg_color="#ffff00", imagen_url=UrlImgs["amarillo"])
                b.configure(command=lambda b=b, r=i, c=j: ejecutar2(b, r, c))
            else:  # Asientos ocupados por otros usuarios
                Sillas(parent=fra, tamanio=16, row=i, column=j, bg_color="#ff8888", imagen_url=UrlImgs["negro"])

    # Configurar el frame principal para permitir la expansión
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
