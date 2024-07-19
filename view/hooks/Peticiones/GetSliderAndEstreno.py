import requests

def GetEstreno(id):
    """
    Obtiene detalles de un estreno por su ID desde la API.

    Args:
    - id (int): ID del estreno.

    Returns:
    - dict: Datos del estreno en formato JSON.
    """
    response = requests.get(f"http://localhost:8080/getEstrenos?id={id}")
    return response.json()

def GetEstrenoAll():
    """
    Obtiene todos los estrenos disponibles desde la API.

    Returns:
    - list: Lista de todos los estrenos en formato JSON.
    """
    response = requests.get(f"http://localhost:8080/getEstrenosAll")
    return response.json()

def GetEstrenoPage(page, limit):
    """
    Obtiene una página específica de estrenos desde la API.

    Args:
    - page (int): Número de página.
    - limit (int): Cantidad de estrenos por página.

    Returns:
    - list: Lista de estrenos de la página especificada en formato JSON.
    """
    response = requests.get(f"http://localhost:8080/getEstrenosPagination?page={page}&limit={limit}")
    return response.json()
