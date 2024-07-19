import requests

def GetSalas(idSala):
    """
    Obtiene detalles de una sala por su ID desde la API.

    Args:
    - idSala (int): ID de la sala.

    Returns:
    - dict: Datos de la sala en formato JSON.
    """
    res = requests.get(f"http://localhost:8080/getSalas?idSalas={idSala}")
    return res.json()

def GetAllSalas():
    """
    Obtiene todas las salas disponibles desde la API.

    Returns:
    - list: Lista de todas las salas en formato JSON.
    """
    res = requests.get(f"http://localhost:8080/getSalasAll")
    return res.json()
