import requests
import json

def GetFuncionesIdDePelicula(idPelicula):
    """
    Obtiene las funciones asociadas a una película específica por su ID.

    Args:
    - idPelicula (int): El ID de la película de la cual se desean obtener las funciones.

    Returns:
    - list: Una lista de diccionarios que contienen los datos de las funciones obtenidas desde la API.
            Cada función puede incluir información sobre las sillas en formato JSON.

    """
    # Realizar la solicitud GET para obtener las funciones por ID de película
    response = requests.get(f"http://localhost:8080/getFunciones?idPelicula={idPelicula}")
    
    # Convertir la respuesta JSON en un diccionario de Python
    funciones = response.json()
    
    # Verificar si la respuesta está vacía
    if not funciones:
        return []
    
    # Convertir el campo 'sillas' de cada función de JSON a objeto Python
    for i, funcion in enumerate(funciones):
        funciones[i]["sillas"] = json.loads(funcion["sillas"])
    
    return funciones

def getAllFunciones():
    """
    Obtiene todas las funciones disponibles en la base de datos.

    Returns:
    - list: Una lista de diccionarios que contienen los datos de todas las funciones obtenidas desde la API.
            Cada función puede incluir información sobre las sillas en formato JSON.

    """
    # Realizar la solicitud GET para obtener todas las funciones
    response = requests.get(f"http://localhost:8080/getFuncionesAll")
    
    # Convertir la respuesta JSON en un diccionario de Python
    funciones = response.json()
    
    # Convertir el campo 'sillas' de cada función de JSON a objeto Python
    for i, funcion in enumerate(funciones):
        funciones[i]["sillas"] = json.loads(funcion["sillas"])
    
    return funciones
