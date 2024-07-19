import requests
import json
from hooks.Peticiones.GetSalas import GetSalas

def cerateSillas(filas, columnas):
    """
    Crea una matriz de sillas inicializadas como libres ('L').

    Args:
    - filas (int): Número de filas de la sala.
    - columnas (int): Número de columnas de la sala.

    Returns:
    - list: Matriz de sillas inicializadas.
    """
    sillas = []
    for i in range(filas):
        sillas.append(['L'] * columnas)
    return sillas

def insertFuncion(fecha, idSala, idPeliculas, ventana, infoUser, main_frame):
    """
    Inserta una nueva función de cine mediante una solicitud GET a una API local.

    Args:
    - fecha (str): Fecha de la función en formato adecuado para la API.
    - idSala (int): ID de la sala de cine donde se realizará la función.
    - idPeliculas (int): ID de la película que se proyectará en la función.
    - ventana: Objeto ventana donde se está realizando la inserción.
    - infoUser: Información del usuario actual.
    - main_frame: Marco principal donde se mostrará la tabla de funciones actualizada.

    Returns:
    - dict: Respuesta JSON de la API sobre el resultado de la inserción.

    Note:
    - Esta función espera que la API responda adecuadamente a la solicitud GET para insertar la función.
    """
    # Obtener información de la sala para crear la lista de sillas
    infoSala = GetSalas(idSala=idSala)
    
    # Crear la lista de sillas inicializadas como libres ('L')
    sillas = cerateSillas(filas=infoSala["fillas"], columnas=infoSala["columnas"])
    
    # Convertir la lista de sillas a formato JSON
    sillas_json = json.dumps(sillas)
    
    # Construir la URL para la solicitud GET
    url = f"http://localhost:8080/introFunciones?fecha={fecha}&idSala={idSala}&idPeliculas={idPeliculas}&sillas={sillas_json}"
    print(url)
    from components.tablaCrud.tablaFunciones import TablaFunciones
    TablaFunciones(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    # Enviar la solicitud GET a la API
    res = requests.get(url)
    response = res.json()
    return response
  
