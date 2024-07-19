import requests
from components.tablaCrud.tablaSalas import TablaSala

def insertSala(nombre, filas, columnas, ventana, infoUser, main_frame):
    """
    Inserta una nueva sala mediante una solicitud GET a una API local.

    Args:
    - nombre (str): Nombre de la sala a insertar.
    - filas (int): Número de filas de la sala.
    - columnas (int): Número de columnas de la sala.
    - ventana (tk.Tk): Ventana principal de la aplicación.
    - infoUser (dict): Información del usuario actual.
    - main_frame (tk.Frame): Marco principal de la interfaz gráfica donde se muestra la tabla de salas.

    Returns:
    - dict: Respuesta JSON de la API.

    """
    # Construir la URL de la solicitud GET para insertar la sala
    url = f"http://localhost:8080/introSala?nombre={nombre}&fillas={filas}&columnas={columnas}"
    
    # Enviar la solicitud GET a la API
    response = requests.get(url)

    # Actualizar la tabla de salas en la interfaz gráfica
    TablaSala(main_frame=main_frame, infoUser=infoUser, ventana=ventana)

    # Retornar la respuesta JSON de la API
    return response.json()
