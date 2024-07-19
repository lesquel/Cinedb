import requests

def insertUser(nombre, img, edad, usuario, correo, contrasena):
    """
    Inserta un nuevo usuario mediante una solicitud POST a una API local.

    Args:
    - nombre (str): Nombre del usuario.
    - img (str): URL o ruta de la imagen del usuario.
    - edad (int): Edad del usuario.
    - usuario (str): Nombre de usuario para iniciar sesión.
    - correo (str): Correo electrónico del usuario.
    - contrasena (str): Contraseña del usuario.

    Returns:
    - dict or None: Respuesta JSON de la API si la inserción fue exitosa, None si ocurrió un error.

    """
    # http://localhost:8080/introUsuario?nombre=1&contra=1&img=1&name=1&correo=1&admin=1
    # Construir la URL para la solicitud POST
    url = f"http://localhost:8080/introUsuario?nombre={nombre}&contra={contrasena}&img={img}&name={usuario}&correo={correo}"
    
    
    # Realizar la solicitud POST con los datos proporcionados
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Devolver la respuesta en formato JSON
        return response.json()
    else:
        # Manejar el caso de error en la respuesta
        print(f"Error: {response.status_code} - {response.text}")
        return None
