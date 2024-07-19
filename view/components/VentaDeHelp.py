import customtkinter as ctk

def VentaDeHelp(ventana, infoUser):
    """
    Crea una ventana secundaria para la venta de ayuda.

    Args:
        ventana (CTkFrame): El marco principal donde se añadirá la ventana secundaria.
        infoUser (dict): Información del usuario actual.

    Returns:
        CTkFrame: El marco interno de la ventana secundaria.
    """
    # Crear la ventana secundaria (Toplevel)
    ventanaActualizar = ctk.CTkToplevel(ventana)
    ventanaActualizar.title("Actualizar género")
    ventanaActualizar.resizable(False, False)  # Evitar que la ventana se pueda redimensionar
    ventanaActualizar.transient(ventana)  # Hacer que la ventana secundaria sea modal
    
    # Crear un marco dentro de la ventana secundaria para organizar contenido
    frame = ctk.CTkFrame(ventanaActualizar)
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
    return frame
