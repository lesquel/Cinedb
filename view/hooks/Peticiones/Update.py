import requests
import urllib.parse
import json

def UpdateData(id, sillas, idUsuario):
    """
    Actualiza datos de sillas en la API utilizando una solicitud GET con sillas en formato JSON.

    Args:
    - id (int): ID de la entrada de datos a actualizar.
    - sillas (list): Lista de listas que representa el estado de las sillas.
    - idUsuario (str or int): ID del usuario para marcar asientos reservados.

    Returns:
    - dict or None: Datos de respuesta en formato JSON si la actualización fue exitosa, None si falla.
    """
    # Convertir la lista de listas a una cadena JSON
    for f, v in enumerate(sillas):
        for c, v2 in enumerate(v):
            if v2 == 'S':
                sillas[f][c] = idUsuario
            elif v2 == 'R':
                sillas[f][c] = 'L'

    # Escapar la cadena JSON para usarla en la URL
    sillas_json = json.dumps(sillas)
    sillas_escapadas = urllib.parse.quote(sillas_json)

    # Construir la URL de la solicitud GET
    url = f"http://localhost:8080/UpdateSillas?id={id}&sillas={sillas_escapadas}"
    
    try:
        # Realizar la solicitud GET
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Devolver la respuesta en formato JSON
            return response.json()
        else:
            # Manejar el caso de error en la respuesta
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        # Manejar posibles errores en la solicitud HTTP
        print(f"HTTP Request failed: {e}")
        return None
