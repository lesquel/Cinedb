def destuirTodo(ventana):
    """
    Destruye todos los widgets secundarios de una ventana de Tkinter.

    Args:
    - ventana: Objeto de ventana de Tkinter (Tk o Toplevel) cuyos widgets secundarios se desean destruir.
    """
    for child in ventana.winfo_children():
        child.destroy()
