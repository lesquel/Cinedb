import requests

def GetUser(usuario, contrasena):
    """
    Obtiene detalles de un usuario por nombre de usuario y contraseña desde la API.

    Args:
    - usuario (str): Nombre de usuario.
    - contrasena (str): Contraseña del usuario.

    Returns:
    - dict: Datos del usuario en formato JSON.
    """
    res = requests.get(f"http://localhost:8080/getUsuario?nombre={usuario}&contra={contrasena}")
    json_data = res.json()
    return json_data

def GetUserId(idUsuario):
    """
    Obtiene detalles de un usuario por su ID desde la API.

    Args:
    - idUsuario (int): ID del usuario.

    Returns:
    - dict: Datos del usuario en formato JSON.
    """
    res = requests.get(f"http://localhost:8080/getUsuarioId?id={idUsuario}")
    json_data = res.json()
    return json_data
