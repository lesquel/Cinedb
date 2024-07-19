import requests
import json

def updateSillas(id, sillas, idUsuario):
    """
    Actualiza la información de las sillas de una sala mediante una solicitud POST a la API local.

    Args:
    - id: ID de la sala o función a la que pertenecen las sillas.
    - sillas: Matriz de sillas a actualizar.
    - idUsuario: ID del usuario que realiza la actualización.

    Returns:
    - res: Respuesta de la solicitud POST a la API.

    Notes:
    - La función modifica 'R' por 'L' y 'S' por el idUsuario antes de enviar la actualización.
    """
    # Modificar la matriz de sillas según ciertos criterios
    for f, v in enumerate(sillas):
        for c, v2 in enumerate(v):
            if v2 == 'R':
                sillas[f][c] = 'L'  # Cambiar 'R' por 'L'
            elif v2 == 'S':
                sillas[f][c] = idUsuario  # Asignar idUsuario a las sillas 'S'

    # Convertir la matriz de sillas a formato JSON
    sillas_json = json.dumps(sillas)

    # Realizar la solicitud POST a la API local para actualizar las sillas
    url = f"http://localhost:8080/UpdateSillas?id={id}&sillas={sillas_json}"
    res = requests.post(url)

    return res