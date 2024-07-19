import requests

def insertComentario(idPelicula, comentario, parent, idUsuario):
    """
    Inserta un comentario sobre una película utilizando una solicitud GET a una API local.

    Args:
    - idPelicula (int): ID de la película sobre la cual se va a comentar.
    - comentario (str): Texto del comentario que se va a insertar.
    - parent: Objeto padre donde se mostrarán los comentarios actualizados.
    - idUsuario (int): ID del usuario que está realizando el comentario.

    Returns:
    - None

    Note:
    - Esta función espera que la API responda adecuadamente a la solicitud GET para insertar el comentario.
    """
    # Construir la URL para la solicitud GET
    url = f"http://localhost:8080/insertComentario?idPelicula={idPelicula}&comentario={comentario}&idUsuario={idUsuario}"
    
    from components.Comentarios import Comentarios  # Asegúrate de que la importación sea correcta y apunte al archivo correcto
    # Enviar la solicitud GET a la API
    response = requests.get(url)
    
    # Imprimir la respuesta (solo para depuración)
    print(response.text)
    
    # Actualizar los comentarios en la interfaz gráfica
    Comentarios(parent=parent, idPelicula=idPelicula, idUsuario=idUsuario)
