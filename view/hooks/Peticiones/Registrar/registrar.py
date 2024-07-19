from tkinter import messagebox
from hooks.Peticiones.insert.insertUser import insertUser

def registrar(main_frame, datosEntry):
    """
    Registra un nuevo usuario utilizando los datos ingresados en los campos de entrada.

    Args:
    - main_frame (tk.Frame): Marco principal de la ventana donde se están ingresando los datos.
    - datosEntry (list): Lista de objetos Entry (campos de entrada) que contienen los datos del usuario
                         en el orden: [nombre, img, edad, usuario, correo, contrasena].

    Returns:
    - None

    """
    # Obtener los datos de los campos de entrada
    nombre = datosEntry[0].get()
    img = datosEntry[1].get()
    edad = datosEntry[2].get()
    usuario = datosEntry[3].get()
    correo = datosEntry[4].get()
    contrasena = datosEntry[5].get()

    # Llamar a la función insertUser para registrar el nuevo usuario
    insertUser(nombre=nombre, img=img, edad=edad, usuario=usuario, correo=correo, contrasena=contrasena)
    
    # Mostrar un mensaje de éxito al usuario
    messagebox.showinfo("Registro exitoso", "Tus datos han sido registrados con éxito.")
    
    # Destruir el marco principal después de completar el registro
    main_frame.destroy()
