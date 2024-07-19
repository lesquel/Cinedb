from tkinter import filedialog, messagebox
from hooks.Peticiones.GetUser import GetUserId  # Importar la función GetUserId desde el módulo GetUser
from hooks.Peticiones.apdate.updateSillas import updateSillas  # Importar la función updateSillas desde el módulo updateSillas
from jinja2 import Template
import webbrowser
def Guardar_tiket(matriz, idUsuario, infoPelicula, funcion, sala):
    """
    Guarda un tiquete en formato HTML con la información relevante de la función seleccionada.

    Args:
    - matriz: Matriz de sillas seleccionadas.
    - idUsuario: ID del usuario que realiza la compra del tiquete.
    - infoPelicula: Información de la película seleccionada.
    - funcion: Información de la función de cine seleccionada.
    - sala: Información de la sala de cine seleccionada.
    """
    # Obtener las sillas seleccionadas por el usuario
    from index import Index  # Importar la clase Index desde el módulo index
    sillas_seleccionadas = []
    for i, v in enumerate(matriz):
        for j, v2 in enumerate(v):
            if v2 == idUsuario or v2 == "S":
                sillas_seleccionadas.append((i, j))
                matriz[i][j] = idUsuario

    # Plantilla HTML para el tiquete
    plantilla_html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Reservación Intercine</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background-color: #f5f5f5;
            }
            .ticket-container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                width: 100vw;
            }
            .ticket {
                background-color: #ffffff;
                border-radius: 15px;
                border: 1px solid #dcdcdc;
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
                padding: 20px;
                max-width: 500px;
                width: 100%;
                text-align: center;
            }
            .highlight {
                background-color: #ff4b2b;
                color: #ffffff;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
                margin-bottom: 20px;
                font-size: 24px;
                letter-spacing: 1px;
            }
            .content p {
                margin: 10px 0;
            }
            .content strong {
                display: block;
                margin-top: 20px;
                font-size: 18px;
            }
            .movie-details {
                margin-top: 10px;
                font-size: 16px;
                color: #333;
            }
            hr {
                border: none;
                border-top: 1px solid #dcdcdc;
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
        <div class="ticket-container">
            <div class="ticket">
                <div class="highlight">INTERCINE</div>
                <div class="content">
                    <hr>
                    <p><strong>DISFRUTA TU PELICULA</strong></p>
                    <p>--{{ nombre_pelicula }}--</p>
                    <hr>
                    <p><strong>Usuario:</strong> {{ usuario }}</p>
                    <p><strong>Hora:</strong> {{ hora_funcion }}</p>
                    <p><strong>Sala:</strong> {{ sala }}</p>
                    <p><strong>Asientos Reservados:</strong></p>
                    {% for fila, columna in asientos %}
                        <p class="movie-details">Fila: {{ fila }}, Columna: {{ columna }}</p>
                    {% endfor %}
                    <hr>
                </div>
                <div class="highlight">Gracias por tu compra</div>
            </div>
        </div>
    </body>
    </html>
    """

    # Función para seleccionar la ruta de guardado del archivo
    def seleccionar_ruta_guardado():
        ruta_archivo = filedialog.asksaveasfilename(
            defaultextension=".html",  # Extensión por defecto
            filetypes=[("Archivos HTML", "*.html"), ("Todos los archivos", "*.*")],  # Tipos de archivos permitidos
            title="Guardar tiquete como"  # Título del diálogo
        )
        if ruta_archivo:
            # Reemplazar los marcadores de posición en la plantilla con los datos reales
            template = Template(plantilla_html)
            contenido_html = template.render(
                nombre_pelicula=infoPelicula['nombre'],
                usuario=GetUserId(idUsuario)['nombre'],
                hora_funcion=funcion['fecha'],
                asientos=sillas_seleccionadas,
                sala=sala['nombre']
            )
            # Escribir la información del tiquete en el archivo seleccionado
            with open(ruta_archivo, 'w') as file:
                file.write(contenido_html)
        webbrowser.open(ruta_archivo)
        

    # Llamar a la función para seleccionar la ruta de guardado
    seleccionar_ruta_guardado()

    # Obtener la información del usuario actual
    infoUser = GetUserId(idUsuario)

    # Actualizar las sillas seleccionadas en el sistema
    updateSillas(id=funcion["id"], sillas=matriz, idUsuario=idUsuario)

    # Mostrar mensaje de éxito
    messagebox.showinfo("Guardado", "El tiquete se guardó con éxito")

    # Redirigir al índice después de guardar el tiquete
    index = Index(ventana=infoPelicula["ventana"], infoUser=infoUser)
