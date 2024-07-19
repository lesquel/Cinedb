import customtkinter as ctk

def RegresarFunc(frame_actual, funcion_retorno):
    """
    Crea un botón de 'Regresar' en el marco actual. Al hacer clic en el botón, se destruye el marco actual y se ejecuta la función de retorno.

    Args:
        frame_actual (CTkFrame): El marco actual donde se añadirá el botón 'Regresar'.
        funcion_retorno (function): La función que se ejecutará después de destruir el marco actual.
    """
    def regresar():
        frame_actual.destroy()
        funcion_retorno()
    
    boton_regresar = ctk.CTkButton(frame_actual, text="Regresar", command=regresar)
    boton_regresar.place(relx=0, rely=0, anchor='nw')
