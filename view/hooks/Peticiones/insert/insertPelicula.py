

def insertPelicula(entries, label_imagen, main_frame, ventana, infoUser):
    """
    Inserta una nueva película mediante una solicitud GET a una API local.

    Args:
    - entries (dict): Diccionario de entradas donde se obtienen los datos de la película.
    - label_imagen (tk.Label): Etiqueta de imagen para mostrar la imagen de la película.
    - main_frame (tk.Frame): Marco principal de la interfaz gráfica donde se muestra la tabla de películas.
    - ventana (tk.Tk): Ventana principal de la aplicación.
    - infoUser (dict): Información del usuario actual.

    Returns:
    - dict: Respuesta JSON de la API.

    """
    import requests
    from tkinter import messagebox
    import customtkinter as ctk
    from components.GeneroEntry import obtener_id_genero
    from components.tablaCrud.tablaPelicula import TablaPelicula
    # Obtener los valores de los campos de entrada
    nombre_pelicula = entries["nombre"].get()
    id_genero = obtener_id_genero(entries["genero"].get())
    duracion_pelicula = entries["duracion"].get()
    trailer_pelicula = entries["trailer"].get()
    descripcion_pelicula = entries["descripcion"].get()
    imagen_pelicula = entries["img"].get()

    # Imprimir los valores para verificar
    print(f"Nombre: {nombre_pelicula}, Género: {id_genero}, Duración: {duracion_pelicula}, Trailer: {trailer_pelicula}, Descripción: {descripcion_pelicula}, Imagen: {imagen_pelicula}")
    
    # Construir la URL de la solicitud GET para insertar la película
    url_insertar_pelicula = f"http://localhost:8080/insertPelicula?nombre={nombre_pelicula}&genero_id={id_genero}&dura={duracion_pelicula}&trailers={trailer_pelicula}&descri={descripcion_pelicula}&img={imagen_pelicula}"
    
    # Enviar la solicitud GET a la API
    response = requests.get(url_insertar_pelicula)


    # Mostrar mensaje de éxito utilizando messagebox
    messagebox.showinfo("Información", "La película se ha insertado correctamente")

    # Actualizar la tabla de películas en la interfaz gráfica
    TablaPelicula(main_frame=main_frame, infoUser=infoUser, ventana=ventana)

    # Retornar la respuesta JSON de la API
    return response.json()
