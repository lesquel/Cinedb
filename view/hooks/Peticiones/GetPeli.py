import requests
from hooks.ModelRequest import ModelRequest

def GetAllPeli(page, limit=5):
    """
    Obtiene una lista de películas paginadas desde la API.

    Args:
    - page (int): Número de página a obtener.
    - limit (int, optional): Límite de resultados por página. Por defecto es 5.

    Returns:
    - ModelRequest: Objeto que maneja la petición y devuelve el resultado JSON de la API.
    """
    def peticion(page, limit):
        res = requests.get(f"http://localhost:8080/getPeliculas?page={page}&limit={limit}")
        return res.json()
    
    return ModelRequest(peticion, page, limit)

def GetPeliId(idPelicula):
    """
    Obtiene los detalles de una película por su ID desde la API.

    Args:
    - idPelicula (int): ID de la película.

    Returns:
    - ModelRequest: Objeto que maneja la petición y devuelve los detalles de la película en JSON.
    """
    def peticion(idPelicula):
        res = requests.get(f"http://localhost:8080/getPeliculaId?id={idPelicula}")
        return res.json()
    
    return ModelRequest(peticion, idPelicula)

def GetPeliTodasAll():
    """
    Obtiene todas las películas disponibles en la base de datos desde la API.

    Returns:
    - ModelRequest: Objeto que maneja la petición y devuelve todas las películas en JSON.
    """
    def peticion():
        res = requests.get(f"http://localhost:8080/getPeliculasAll")
        return res.json()
    
    return ModelRequest(peticion)

def GetPeliByNombre(nombre):
    """
    Busca películas por su nombre desde la API.

    Args:
    - nombre (str): Nombre de la película a buscar.

    Returns:
    - ModelRequest: Objeto que maneja la petición y devuelve las películas encontradas por nombre en JSON.
    """
    def peticion(nombre):
        res = requests.get(f"http://localhost:8080/getPeliculasByNombre?nombre={nombre}")
        return res.json()
    
    return ModelRequest(peticion, nombre)

def GetPeliByGenero(idGenero):
    """
    Obtiene películas por su género desde la API.

    Args:
    - idGenero (int): ID del género de las películas a buscar.

    Returns:
    - ModelRequest: Objeto que maneja la petición y devuelve las películas encontradas por género en JSON.
    """
    def peticion(idGenero):
        res = requests.get(f"http://localhost:8080/getPeliculasByGenero?id={idGenero}")
        return res.json()
    
    return ModelRequest(peticion, idGenero)
