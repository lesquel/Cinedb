import requests
from tkinter import messagebox
from components.tablaCrud.tablaFunciones import TablaFunciones

def deleteFuncion(id, main_frame, infoUser, ventana):
    """
    Elimina una función de la base de datos y actualiza la tabla de funciones en la interfaz gráfica.

    Args:
    - id: ID de la función que se va a eliminar.
    - main_frame: Marco principal de la aplicación donde se muestra la tabla de funciones.
    - infoUser: Información del usuario actual.
    - ventana: Ventana principal de la aplicación.

    Returns:
    - JSON: Respuesta de la solicitud HTTP DELETE.

    Notes:
    - Muestra un mensaje de confirmación antes de proceder con la eliminación.
    - Actualiza la tabla de funciones llamando a TablaFunciones después de eliminar la función.
    """
    # Mostrar un cuadro de diálogo de confirmación
    respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar esta función?")
    if not respuesta:
        return None
    
    # Realizar la solicitud DELETE para eliminar la función por su ID
    url = f"http://localhost:8080/deleteFunciones?id={id}"
    response = requests.delete(url)
    
    # Actualizar la tabla de funciones en la interfaz gráfica
    TablaFunciones(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
    
    return response.json()
