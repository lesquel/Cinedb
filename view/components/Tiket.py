import customtkinter as ctk
from tkinter import messagebox
from components.Text import Text
from components.Button import Button
from hooks.Guardar_tiket import Guardar_tiket

def Tiket(parent, matriz, idUsuario, infoPelicula, funcion, sala):
    """
    Muestra información de un ticket de reserva de película en un cuadro de texto enriquecido.
    
    Args:
        parent (CTkFrame): El marco padre donde se colocará el contenido del ticket.
        matriz (list): Una matriz que representa los asientos disponibles y reservados.
        idUsuario (str): El ID del usuario que realiza la reserva.
        infoPelicula (dict): Información de la película reservada.
        funcion (dict): Detalles de la función de cine (fecha, hora, etc.).
        sala (dict): Información de la sala de cine.

    """
    # Verificar si hay asientos disponibles ("S" representa un asiento disponible)
    if not any("S" in fila for fila in matriz):
        messagebox.showinfo("Error", "No hay asientos disponibles.")
        return

    # Crear etiqueta para el título del ticket
    Text(parent=parent, texto="Ticket", tamanio=16, row=1, column=0, padx=10, pady=10)
    
    # Crear un cuadro de texto enriquecido para mostrar la información del ticket
    textBox = ctk.CTkTextbox(parent, height=150, width=200)
    textBox.grid(row=2, column=0, padx=40, pady=40, sticky="nsew")
    
    # Insertar información de la película, sala y función en el cuadro de texto
    textBox.insert("end", f"Película: {infoPelicula['nombre']}\n")
    textBox.insert("end", f"Sala: {sala['nombre']}\n")
    textBox.insert("end", f"Fecha: {funcion['fecha']}\n")
    textBox.insert("end", f"Duración: {infoPelicula['dura']}H\n")
    textBox.insert("end", "Sillas:\n")

    # Insertar las coordenadas de los asientos reservados por el usuario
    for i, fila in enumerate(matriz):
        for j, asiento in enumerate(fila):
            if asiento == "S" or asiento == idUsuario:
                textBox.insert("end", f"{i} {j}\n")

    # Botón para reservar y cargar el ticket
    Button(parent=parent, texto="Reservar y Cargar", tamanio=16, row=3, column=0, eventoClick=lambda: Guardar_tiket(matriz=matriz, idUsuario=idUsuario, infoPelicula=infoPelicula, funcion=funcion, sala=sala))
