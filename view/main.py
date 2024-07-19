import customtkinter as ctk
from tkinter import messagebox
from login import login

def on_closing():
    if messagebox.askokcancel("Salir", "¿Quieres salir de la aplicación?"):
        main_window.destroy()

# Configuración inicial de customtkinter
ctk.set_appearance_mode("dark")  # Establece el modo de apariencia en tema oscuro
ctk.set_default_color_theme("dark-blue")  # Establece el tema de color por defecto en azul oscuro

# Crear la ventana principal
main_window = ctk.CTk()  # Instancia de la ventana principal
main_window.title("Cine")  # Título de la ventana

# Obtener la resolución de la pantalla
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

# Configurar la ventana para ocupar toda la pantalla, descontando la barra de tareas
window_geometry = f"{screen_width}x{screen_height - 25}+0+0"
main_window.geometry(window_geometry)

# Deshabilitar el cambio de tamaño de la ventana
main_window.resizable(False, False)

# Establecer la función para manejar el cierre de la ventana
main_window.protocol("WM_DELETE_WINDOW", on_closing)

# Iniciar la pantalla de login pasando la ventana principal como parámetro
login(main_window)

# Iniciar el bucle principal de la aplicación
main_window.mainloop()
