import customtkinter as ctk
from components.Text import Text
from components.Img import Img
from layout import Layout

def Perfil(ventana, infoUser):
    """
    Crea y muestra el perfil de usuario en una ventana.

    Args:
    - ventana: La ventana principal donde se mostrará el perfil.
    - infoUser: Un diccionario que contiene la información del usuario.

    Returns:
    - frame: El marco principal que contiene la interfaz del perfil.
    """
    # Crear el marco principal usando Layout
    frame = Layout(ventana=ventana)
    
    # Añadir el menú lateral dependiendo del rol de usuario
    if infoUser["admin"]:
        from components.Nav import NavAdmin
        NavAdmin(frame, [{"ventana": ventana, "infoUser": infoUser}])
    else:
        from components.Nav import Nav
        Nav(frame, [{"ventana": ventana, "infoUser": infoUser}])

    # Crear el marco para la información del usuario
    frame_infouser = ctk.CTkFrame(frame)
    frame_infouser.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    # Añadir imagen redondeada de perfil
    img_perfil = Img(frame_infouser, url=infoUser["img"])
    if img_perfil:
        img_perfil.grid(row=0, column=0, padx=20, pady=10, columnspan=2)

    # Crear sub-marcos para organizar la información del usuario
    frame1 = ctk.CTkFrame(frame_infouser)
    frame1.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
    
    # Añadir nombre de usuario y contraseña
    Text(frame1, texto=f"Usuario: {infoUser['nombre']}", tamanio=16).grid(row=1, column=1, padx=5, pady=10)
    Text(frame1, texto=f"Contraseña: {infoUser['contra']}", tamanio=16).grid(row=2, column=1, padx=5, pady=10)
    
    # Crear otro sub-marco para el nombre real y edad
    frame2 = ctk.CTkFrame(frame_infouser)
    frame2.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
    Text(frame2, texto=f"Nombre Real: {infoUser['name']}", tamanio=16).grid(row=3, column=1, padx=5, pady=10)
    Text(frame2, texto=f"Edad: {infoUser['edad']}", tamanio=16).grid(row=5, column=1, padx=5, pady=10)
    
    # Crear otro sub-marco para el correo electrónico
    frame3 = ctk.CTkFrame(frame_infouser)
    frame3.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")
    Text(frame3, texto=f"Correo: {infoUser['correo']}", tamanio=16).grid(row=4, column=1, padx=5, pady=10)

    # Botón para editar perfil
    from Editar_perfil import Editar_perfil
    editar = ctk.CTkButton(frame_infouser, text="Editar", width=120, height=40, command=lambda: Editar_perfil(ventana=ventana, infoUser=infoUser))
    editar.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    return frame
