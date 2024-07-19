import requests

def apdateFuncion(id, fecha, idSala, idPeliculas, ventana, infoUser, ventanaHelp, main_frame):
    """
    Actualiza una función de cine mediante una solicitud GET a la API local y actualiza la tabla de funciones en la interfaz gráfica.

    Args:
    - id: ID de la función a actualizar.
    - fecha: Nueva fecha para la función.
    - idSala: ID de la sala asociada a la función.
    - idPeliculas: ID de la película asociada a la función.
    - ventana: Objeto ventana donde se muestra la interfaz gráfica.
    - infoUser: Información del usuario actual.
    - ventanaHelp: Ventana de ayuda que se cierra después de la actualización.
    - main_frame: Marco principal de la tabla de funciones donde se refrescará la información.

    Returns:
    - dict: Respuesta JSON de la solicitud GET.
    """
    from components.tablaCrud.tablaFunciones import TablaFunciones
    # Cerrar la ventana de ayuda
    ventanaHelp.destroy()

    # Construir la URL para la solicitud GET
    url = f"http://localhost:8080/updateFunciones?id={id}&idSala={idSala}&idPeliculas={idPeliculas}&fecha={fecha}"

    # Realizar la solicitud GET a la API local
    res = requests.get(url)

    # Actualizar la tabla de funciones en la interfaz gráfica
    TablaFunciones(main_frame=main_frame, infoUser=infoUser, ventana=ventana)

    # Devolver la respuesta JSON de la solicitud GET
    return res.json()
