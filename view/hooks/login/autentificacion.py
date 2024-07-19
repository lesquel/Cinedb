
def autentificacion(ventana, usuario, contrasena):
    from tkinter import messagebox
    from hooks.Peticiones.GetUser import GetUser
    from index import Index
    """
    Realiza la autenticación de usuarios y redirige según el rol.

    Args:
    - ventana: Objeto ventana donde se mostrarán los mensajes de error.
    - usuario: Nombre de usuario ingresado para autenticación.
    - contrasena: Contraseña ingresada para autenticación.

    Returns:
    - Instancia de la ventana Index correspondiente, dependiendo del rol del usuario.
    """

    # Validación de campos vacíos
    if usuario == "":
        messagebox.showinfo("Error", "Introduzca el usuario")
        return
    if contrasena == "":
        messagebox.showinfo("Error", "Introduzca la contraseña")
        return

    # Obtener información del usuario desde la base de datos o API
    infoUser = GetUser(usuario, contrasena)

    # Verificar si se obtuvo información del usuario
    if not infoUser:
        messagebox.showinfo("Error", "Usuario o contraseña incorrectos")
        return

    # Redireccionar según el rol del usuario
    
    frame = Index(ventana, infoUser=infoUser)
    return frame