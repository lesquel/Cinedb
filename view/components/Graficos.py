import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading

def crear_grafico_barras(frame, data, labels, title="Gráfico de Barras", x_label="X", y_label="Y", row=0, column=0):
    """
    Crea un gráfico de barras y lo inserta en un widget Tkinter.

    Parameters:
    - frame (ctk.CTkFrame): El frame de Tkinter donde se insertará el gráfico.
    - data (list): Lista de valores para las barras.
    - labels (list): Lista de etiquetas para las barras.
    - title (str): Título del gráfico.
    - x_label (str): Etiqueta del eje X.
    - y_label (str): Etiqueta del eje Y.
    - row (int): Fila del grid donde se insertará el gráfico.
    - column (int): Columna del grid donde se insertará el gráfico.
    """
    fig, ax = plt.subplots()

    ax.bar(labels, data)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    widget = canvas.get_tk_widget()
    widget.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

def obtener_datos_y_crear_grafico(frame, data, labels, row, column, title, x_label, y_label):
    """
    Obtiene los datos y crea el gráfico en el hilo principal.

    Parameters:
    - frame (ctk.CTkFrame): El frame de Tkinter donde se insertará el gráfico.
    - data (list): Lista de valores para las barras.
    - labels (list): Lista de etiquetas para las barras.
    - row (int): Fila del grid donde se insertará el gráfico.
    - column (int): Columna del grid donde se insertará el gráfico.
    - title (str): Título del gráfico.
    - x_label (str): Etiqueta del eje X.
    - y_label (str): Etiqueta del eje Y.
    """
    def actualizar_grafico():
        crear_grafico_barras(frame, data, labels, title, x_label, y_label, row, column)
    
    frame.after(0, actualizar_grafico)

def Graficos(frame, data, labels, row, column, title="Gráfico de Barras", x_label="X", y_label="Y"):
    """
    Ejecuta la función obtener_datos_y_crear_grafico en un hilo separado.

    Parameters:
    - frame (ctk.CTkFrame): El frame de Tkinter donde se insertará el gráfico.
    - data (list): Lista de valores para las barras.
    - labels (list): Lista de etiquetas para las barras.
    - row (int): Fila del grid donde se insertará el gráfico.
    - column (int): Columna del grid donde se insertará el gráfico.
    - title (str): Título del gráfico.
    - x_label (str): Etiqueta del eje X.
    - y_label (str): Etiqueta del eje Y.
    """
    thread = threading.Thread(target=obtener_datos_y_crear_grafico, args=(frame, data, labels, row, column, title, x_label, y_label))
    thread.start()
