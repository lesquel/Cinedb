import requests

def apdateSala(id, nombre, filas, columnas, ventana, infoUser, ventanaHelp, main_frame):
    """
    Actualiza la información de una sala mediante una solicitud GET a la API local y refresca la tabla de salas.

    Args:
    - id: ID de la sala a actualizar.
    - nombre: Nuevo nombre de la sala.
    - filas: Nueva cantidad de filas de asientos en la sala.
    - columnas: Nueva cantidad de columnas de asientos en la sala.
    - ventana: Objeto ventana donde se muestra la interfaz gráfica.
    - infoUser: Información del usuario actual.
    - ventanaHelp: Ventana de ayuda que se cerrará después de actualizar.
    - main_frame: Marco principal donde se encuentra la tabla de salas.

    Returns:
    - None
    """
    from components.tablaCrud.tablaSalas import TablaSala
    # Construir la URL para la solicitud GET
    url = f"http://localhost:8080/updateSala?id={id}&nombre={nombre}&fillas={filas}&columnas={columnas}"

    # Realizar la solicitud GET a la API local
    requests.get(url)

    # Cerrar la ventana de ayuda
    ventanaHelp.destroy()

    # Actualizar la tabla de salas para reflejar los cambios
    TablaSala(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
