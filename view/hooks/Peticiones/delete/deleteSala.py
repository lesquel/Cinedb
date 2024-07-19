import requests
from tkinter import messagebox

def deleteSala(id, main_frame, infoUser, ventana):
    """
    Elimina una sala de cine de la base de datos y actualiza la tabla de salas en la interfaz gráfica.

    Args:
    - id: ID de la sala que se va a eliminar.
    - main_frame: Marco principal de la aplicación donde se muestra la tabla de salas.
    - infoUser: Información del usuario actual.
    - ventana: Ventana principal de la aplicación.

    Returns:
    - None

    Notes:
    - Muestra un mensaje de confirmación antes de proceder con la eliminación.
    - Realiza una solicitud HTTP GET para eliminar la sala por su ID.
    - Actualiza la tabla de salas después de la eliminación.
    """
    # Mostrar un mensaje de confirmación para la eliminación
    confirmar = messagebox.askyesno("Eliminar", "¿Estás seguro de eliminar esta sala?")
    
    from components.tablaCrud.tablaSalas import TablaSala
    if confirmar:
        # Construir la URL para la solicitud GET
        url = f"http://localhost:8080/deleteSala?id={id}"
        
        # Realizar la solicitud GET para eliminar la sala
        requests.get(url)
        
        # Actualizar la tabla de salas después de la eliminación
        TablaSala(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
