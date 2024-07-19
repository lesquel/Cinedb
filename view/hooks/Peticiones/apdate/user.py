import requests
from tkinter import messagebox
from Perfil import Perfil  # Asumiendo que Perfil está correctamente importado
from hooks.Peticiones.GetUser import GetUserId  # Asumiendo que GetUserId está correctamente importado

def update_user(id, nombre, contra, img, name, correo, edad, ventana):
    """
    Actualiza la información de usuario mediante una solicitud GET a la API local.

    Args:
    - id: ID del usuario a actualizar.
    - nombre: Nuevo nombre del usuario.
    - contra: Nueva contraseña del usuario.
    - img: Nueva imagen del usuario.
    - name: Nuevo nombre completo del usuario.
    - correo: Nuevo correo electrónico del usuario.
    - edad: Nueva edad del usuario.
    - ventana: Ventana principal donde se muestra el perfil actualizado.

    Returns:
    - None

    Notes:
    - Muestra un mensaje de información sobre la actualización exitosa.
    - Actualiza la pantalla de perfil del usuario con la información actualizada.
    """
    # Construir la URL para la solicitud GET de actualización de usuario
    url = f"http://localhost:8080/updateUsuario?id={id}&nombre={nombre}&contra={contra}&img={img}&name={name}&correo={correo}&edad={edad}"
    
    # Realizar la solicitud GET a la API local
    response = requests.get(url)
    
    # Mostrar mensaje de información sobre la actualización exitosa
    messagebox.showinfo("Actualización exitosa", "Tus datos han sido actualizados con éxito.")
    
    # Obtener la información actualizada del usuario
    user = GetUserId(idUsuario=id)
    
    # Mostrar el perfil actualizado en la ventana principal
    Perfil(ventana=ventana, infoUser=user)
