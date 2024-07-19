from layout import Layout
import customtkinter as ctk
from components.Text import Text
from components.Img import Img
from components.Button import Button
from components.salas.funciones import Funciones
from hooks.Peticiones.GetFunciones import GetFuncionesIdDePelicula
from hooks.AbrirTrailer import AbrirTrailer
from hooks.Peticiones.getGenero import getGenero
from components.Regresar import RegresarFunc
from hooks.Peticiones.GetUser import GetUserId

def Salas(ventana, infoPelicula, idUsuario):
    """
    Crea una interfaz de usuario para mostrar información de la película y funciones disponibles.

    Args:
    - ventana: La ventana principal sobre la cual se construirá la interfaz.
    - infoPelicula: Un diccionario con información de la película.
    - idUsuario: El identificador del usuario actual.

    Returns:
    - frame: El marco principal de la interfaz.
    """
    from index import Index
    # Información de la película
    info = {
        "ventana": ventana,
        "id": infoPelicula["id"],
        "img": infoPelicula["img"],
        "nombre": infoPelicula["nombre"],
        "descri": infoPelicula["descri"],
        "dura": infoPelicula["dura"],
        "genero": infoPelicula["genero"],
        "trailer": infoPelicula["trailer"]
    }
    
    # Obtener funciones de la película
    funciones = GetFuncionesIdDePelicula(idPelicula=infoPelicula["id"])

    # Crear el marco principal utilizando la plantilla de Layout
    frame = Layout(ventana=ventana)
    
    # Crear frame1 y frame2 como hijos de frame
    frame1 = ctk.CTkFrame(frame, width=600, height=600)
    frame1.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")
    frame1.grid_columnconfigure(0, weight=0)
    frame1.grid_columnconfigure(1, weight=1) 
    
    frame2 = ctk.CTkFrame(frame)
    frame2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    # Mostrar imagen de la película
    Img(frame1, infoPelicula["img"])

    # Agregar componentes al frame principal (frame1)
    Text(parent=frame1, texto=f"Película: {infoPelicula['nombre']}", tamanio=20, row=1, column=0, padx=10, pady=20)
    Text(parent=frame1, texto=f"Descripción: {infoPelicula['descri']}", tamanio=16, row=2, column=0, padx=10, pady=20).configure(wraplength=400)
    
    frameInfoPequena = ctk.CTkFrame(frame1)
    frameInfoPequena.grid(row=3, column=0, padx=10, pady=20, sticky="nsew")
    Text(parent=frameInfoPequena, texto=f"Duración: {infoPelicula['dura']} H", tamanio=16, row=0, column=0, padx=10, pady=20)
    
    # Obtener el nombre del género de la película
    genero = getGenero(info['genero'])
    Text(parent=frameInfoPequena, texto=f"Género: {genero['nombre']}", tamanio=16, row=0, column=1, padx=10, pady=20)
    
    # Botón para abrir el tráiler de la película
    Button(frameInfoPequena, texto="Ver Tráiler", tamanio=16, eventoClick=lambda url=infoPelicula["trailer"]: AbrirTrailer(url)).grid(row=0, column=2, padx=10, pady=20)

    # Mostrar funciones de la película en frame2
    Funciones(parent=frame2, idUsuario=idUsuario, frame=frame, ventana=ventana, funciones=funciones, info=info)

    # Botón para regresar a la página principal
    infoUser = GetUserId(idUsuario)
    RegresarFunc(frame_actual=frame, funcion_retorno=lambda: Index(ventana=ventana, infoUser=infoUser))

    return frame
